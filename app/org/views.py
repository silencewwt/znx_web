# -*- coding: utf-8 -*-
import os
import time, datetime
from uuid import uuid4
from . import org
from .. import db
from ..models import Organization, Type, ClassOrder, ActivityOrder, \
    Profession, Location, Class, ClassAge,\
    Activity, City, ClassTime, OrganizationComment, ActivityAge
from .forms import RegistrationForm, DetailForm, \
    CertificationForm, LoginForm, CommentForm
from ..user.forms import LoginForm as UserLoginForm
from flask.ext.login import login_user, login_required, current_user
from flask.ext.principal import identity_changed, Identity
from flask import redirect, url_for, render_template,\
    flash, current_app, request
from ..utils.query import get_location
from ..permission import org_permission, anonymous_permission, user_permission
from ..utils.captcha import send_captcha
from ..utils.validator import generate_dir_path


@org.route('/login', methods=['POST'])
def login():
    user_form = UserLoginForm()
    org_form = LoginForm()
    if org_form.validate_on_submit():
        org = Organization.query.filter_by(
            mobile=org_form.cellphone.data
        ).first() or Organization.query.filter_by(
            name=org_form.cellphone.data).first()

        if org is not None and org.verify_password(user_form.password.data):
            login_user(org, user_form.remember_me.data)
            identity_changed.send(current_app._get_current_object(),
                                  identity=Identity(org.get_id()))
            return redirect(request.args.get('next') or url_for('.course_list'))
        flash(u'用户名密码错误')
    return render_template('login_choose_py.html',
                           user_form=user_form,
                           org_form=org_form)


@org.route('/register', methods=['GET', 'POST'])
@anonymous_permission.require()
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        organization = Organization(mobile=form.cellphone.data,
                            password=form.password.data,
                            created=time.time(),
                            site=u'')
        db.session.add(organization)
        db.session.commit()
        # token = user.generate_confirmation_token()
        # TODO: Add token.
        # TODO: add macro in template for errors.
        #send_email(user.email, 'Confirm Your Account',
        #           'auth/mail/confirm', user=user)
        #flash('A confirmation email has been sent to you by email.')
        login_user(organization)
        identity_changed.send(current_app._get_current_object(),
                              identity=Identity(organization.get_id()))
        return redirect(url_for('.detail'))
    return render_template('organ_regiter_py.html', form=form)

@org.route('/send_sms', methods=['post'])
def send_sms():
    # TODO: add csrf and mobile check.
    # TODO: return 200 401
    mobile = request.values.get('mobile', '', type=str)
    if mobile:
        if send_captcha('org', mobile):
            return 'ok', 200
    return 'false', 401

@org.route('/detail', methods=['GET', 'POST'])
@org_permission.require()
def detail():
    form = DetailForm()
    form.create_choices()
    if form.validate_on_submit():
        form.update_org()
        # token = user.generate_confirmation_token()
        # TODO: Add token.
        # TODO: add macro in template for errors.
        #send_email(user.email, 'Confirm Your Account',
        #           'auth/mail/confirm', user=user)
        #flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('.certification'))
    return render_template('organ_regiter2_py.html', form=form)


@org.route('/certification', methods=['GET', 'POST'])
@org_permission.require()
def certification():
    form = CertificationForm()
    if form.validate_on_submit():
        #organization = Organization(cellphone=form.cellphone.data,
        # #password=form.password.data)
        #db.session.add(organization)
        #db.session.commit()
        # token = user.generate_confirmation_token()
        # TODO: Add token.
        # TODO: add macro in template for errors.
        #send_email(user.email, 'Confirm Your Account',
        #           'auth/mail/confirm', user=user)
        #flash('A confirmation email has been sent to you by email.')
        path = current_app.config['PHOTO_DIR']
        org_id = current_user.id
        relative_path = generate_dir_path(org_id)
        dir_path = os.path.join(path, relative_path)
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        ext = form.certification.data.filename.rsplit('.', 1)[-1]
        certification = uuid4().hex + '.' + ext
        file_path = os.path.join(dir_path, certification)
        form.certification.data.save(file_path)

        ext = form.photo.data.filename.rsplit('.', 1)[-1]
        photo = uuid4().hex + '.' + ext
        file_path = os.path.join(dir_path, photo)
        form.photo.data.save(file_path)

        ext = form.logo.data.filename.rsplit('.', 1)[-1]
        logo = uuid4().hex + '.' + ext
        file_path = os.path.join(dir_path, logo)
        form.logo.data.save(file_path)

        current_user.authorization = os.path.join(relative_path, certification)
        current_user.photo = os.path.join(relative_path, photo)
        current_user.logo = os.path.join(relative_path, logo)
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('org.success'))
    return render_template('organ_regiter3_py.html', form=form)


@org.route('/success')
@org_permission.require()
def success():
    return render_template('origanreg4_py.html')


@org.route('/home/<int:id>', methods=['GET', 'POST'])
def home(id):
    org = Organization.query.get_or_404(id)
    form = CommentForm()
    if form.validate_on_submit():
        if user_permission.can():
            comment = form.create_organization_comment(id)
            org.set_star(comment.stars)
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('org.home', id=id))
        else:
            flash(u'用户登录后才可以评论')
    page = request.args.get('page', 1, type=int)
    org.page_view_inc()
    db.session.commit()
    pagination = OrganizationComment.query.filter_by(organization_id=id).order_by(
        OrganizationComment.created.asc()).paginate(
        page, per_page=current_app.config['ORG_COMMENT_PER_PAGE'],
        error_out=False)
    comments = pagination.items
    return render_template('organindex_py.html',
                           org=org,
                           comments=comments,
                           pagination=pagination,
                           form=form)


from .forms import CourseForm


@org.route('/course/add', methods=['GET', 'POST'])
@org_permission.require()
def add_course():
    course_form = CourseForm()
    course_form.create_choices()
    if course_form.validate_on_submit():
        course_form.create_course()
        return redirect(url_for('.course_list'))
    return render_template('origanclassadd_py.html',
                           form=course_form,
                           add=True)


# TODO: delete course with delete method.
@org.route('/course/delete/<int:id>')
@org_permission.require()
def delete_course(id):
    course = Class.query.get_or_404(id)
    #if ClassOrder.query.filter_by(class_id=id).first():
    #    flash(u'已经有用户选择课程，无法关闭')
    #    return redirect(url_for('org.course_list'))

    course.is_closed = True
    db.session.add(course)
    db.session.commit()
    return redirect(url_for('org.course_list'))


@org.route('/course/edit/<int:id>', methods=['GET', 'POST'])
@org_permission.require()
def edit_course(id):
    Class.query.get_or_404(id)
    course_form = CourseForm()
    course_form.create_choices()
    if course_form.validate_on_submit():
        course = course_form.update_course(id)
        db.session.add(course)
        db.session.commit()

        class_times = ClassTime.query.filter_by(class_id=id).all()
        for class_time in class_times:
            db.session.delete(class_time)
        db.session.flush()
        for time_id in course_form.class_time.data:
            class_time = ClassTime(class_id=course.id, time_id=time_id)
            db.session.add(class_time)

        class_ages = ClassAge.query.filter_by(class_id=id).all()
        for class_age in class_ages:
            db.session.delete(class_age)
        db.session.flush()
        for age_id in course_form.ages.data:
            class_age = ClassAge(class_id=course.id, age_id=age_id)
            db.session.add(class_age)
        db.session.commit()
        return redirect(url_for('.course_list'))
    course_form.init_from_class(id)
    return render_template('origanclassadd_py.html', form=course_form)



@org.route('/course/list')
@org_permission.require()
def course_list():
    courses = Class.query.filter_by(organization_id=current_user.id).all()
    return render_template('origanclasslist_py.html', courses=courses)


from .forms import ActivityForm


@org.route('/activity/add', methods=['GET', 'POST'])
@org_permission.require()
def add_activity():
    form = ActivityForm()
    form.create_choices()
    if form.validate_on_submit():
        form.create_activity()
        return redirect(url_for('.activity_list'))
    return render_template('origanactadd_py.html', form=form)


@org.route('/activity/edit/<int:id>', methods=['GET', 'POST'])
@org_permission.require()
def edit_activity(id):
    Activity.query.get_or_404(id)
    activity_form = ActivityForm()
    activity_form.create_choices()
    if activity_form.validate_on_submit():
        activity = activity_form.update_activity(id)
        db.session.add(activity)
        db.session.commit()
        
        activity_ages = ActivityAge.query.filter_by(activity_id=id).all()
        for activity_age in activity_ages:
            db.session.delete(activity_age)
        db.session.flush()
        for age_id in activity_form.ages.data:
            activity_age = ActivityAge(activity_id=id, age_id=age_id)
            db.session.add(activity_age)
        db.session.commit()

        return redirect(url_for('.activity_list'))
    activity_form.init_from_activity(id)
    return render_template('origanactadd_py.html', form=activity_form)


@org.route('/activity/delete/<int:id>')
@org_permission.require()
def delete_activity(id):
    activity = Activity.query.get_or_404(id)
    #if ClassOrder.query.filter_by(class_id=id).first():
    #    flash(u'已经有用户选择课程，无法关闭')
    #    return redirect(url_for('org.course_list'))

    activity.is_closed = True
    db.session.add(activity)
    db.session.commit()
    return redirect(url_for('org.activity_list'))

@org.route('/activity/list')
@org_permission.require()
def activity_list():
    activities = Activity.query.filter_by(organization_id=current_user.id).all()
    return render_template('origanactlist_py.html', activities=activities)


@org.route('/orders')
@org_permission.require()
@login_required
def order_list():
    id = current_user.id
    class_orders = ClassOrder.query.filter(ClassOrder.class_id.in_(
        db.session.query(Class.id).filter(Class.organization_id==id)
    )).all()

    activity_orders = ActivityOrder.query.filter(ActivityOrder.activity_id.in_(
        db.session.query(Activity.id).filter(Activity.organization_id==id)
    )).all()
    return render_template('origanorderlist_py.html', class_orders=class_orders,
                           activity_orders=activity_orders)


# TODO: add acl
@org.route('/course/order/<int:id>')
def course_order_detail(id):
    class_order = ClassOrder.query.get_or_404(id)
    return render_template('origanorderdet_py.html', order=class_order)


@org.route('/activity/order/<int:id>')
def activity_order_detail(id):
    activity_order = ActivityOrder.query.get_or_404(id)
    return render_template('user_activity_order_det_py.html', order=activity_order)


@org.route('/account', methods=['POST'])
def account():
    mobile = request.values.get('mobile', '', type=str)
    if mobile:
        if Organization.query.filter_by(mobile=mobile).first():
            return 'false', 500
        return 'true', 200
    return 'false', 500
