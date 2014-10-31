# -*- coding: utf-8 -*-
import os
import time
from uuid import uuid4
from . import org
from .. import db
from ..models import Organization, Type, ClassOrder, ActivityOrder,\
    Profession, Property, Size, Location, Class, Activity, City
from .forms import RegistrationForm, DetailForm, \
    CertificationForm, LoginForm, CommentForm, PhotoForm
from ..user.forms import LoginForm as UserLoginForm
from flask.ext.login import login_user, login_required, current_user
from flask.ext.principal import identity_changed, Identity
from flask import redirect, url_for, render_template,\
    flash, current_app, request, send_file
from ..utils.query import get_location
from ..permission import org_permission, anonymous_permission, user_permission
from ..utils.captcha import send_captcha

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
                            created=time.time())
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
        send_captcha('org', mobile)
    return 'ok', 200

@org.route('/detail', methods=['GET', 'POST'])
@org_permission.require()
def detail():
    form = DetailForm()
    form.type_id.choices = [(t.id, t.type) for t in Type.query.all()]
    form.property_id.choices = [(t.id, t.property)
                                for t in Property.query.all()]
    form.profession_id.choices = [(t.id, t.profession)
                                  for t in Profession.query.all()]
    form.size_id.choices = [(t.id, t.size)
                            for t in Size.query.all()]
    form.location_id.choices = [(t.id, t.district)
                                for t in Location.query.all()]
    form.city_id = City.query.all()
        # TODO: correct choose form.
    form.location = Location.query.all()
    if form.validate_on_submit():
        current_user.type_id = form.type_id.data
        current_user.name = form.name.data
        current_user.profession_id = form.profession_id.data
        current_user.property_id = form.property_id.data
        current_user.size_id = form.size_id.data
        current_user.contact = form.contact.data
        current_user.location_id = form.location_id.data
        current_user.address = form.address.data
        current_user.intro = form.intro.data
        db.session.add(current_user)
        db.session.commit()
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
    certification_form = CertificationForm()
    photo_form = PhotoForm()
    path = current_app.config['PHOTO_DIR']
    if certification_form.validate_on_submit():
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

        ext = certification_form.certification.data.filename.rsplit('.', 1)[-1]
        certification_file = uuid4().hex + '.' + ext
        file_path = os.path.join(path, certification_file)
        certification_form.certification.data.save(file_path)
        current_user.authorization = certification_file
        db.session.add(current_user)
        db.session.commit()

    if photo_form.validate_on_submit():
        ext = photo_form.photo.data.filename.rsplit('.', 1)[-1]
        photo = uuid4().hex + '.' + ext
        file_path = os.path.join(path, photo)
        photo_form.photo.data.save(file_path)

        current_user.photo = photo
        db.session.add(current_user)
        db.session.commit()

    return render_template('organ_regiter3_py.html',
                           certification_form=certification_form,
                           photo_form=photo_form)
@org.route('/pic/<path:filename>')
def pic(filename):
    path = current_app.config['PHOTO_DIR']
    file_path = os.path.join(path, filename)
    return send_file(file_path)

@org.route('/home/<int:id>', methods=['GET', 'POST'])
def home(id):
    org = Organization.query.get_or_404(id)
    classes = Class.query.filter_by(organization_id=id).all()
    activities = Activity.query.filter_by(organization_id=id).all()
    form = CommentForm()
    if form.validate_on_submit():
        if user_permission.can():
            comment = form.create_organization_comment(id)
            db.session.add(comment)
            db.session.commit()
            return redirect(url_for('org.home', id=id))
    return render_template('organindex_py.html',
                           org=org,
                           classes=classes,
                           activities=activities, form=form)


from .forms import CourseForm


@org.route('/course/add', methods=['GET', 'POST'])
@org_permission.require()
def add_course():
    course_form = CourseForm()
    course_form.create_choices()
    if course_form.validate_on_submit():
        course = course_form.create_course()
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('main.index'))
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
        activity = form.create_activity()
        db.session.add(activity)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('origanactadd_py.html', form=form)


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
    ))

    activity_orders = ActivityOrder.query.filter(ActivityOrder.activity_id.in_(
        db.session.query(Activity.id).filter(Activity.organization_id==id)
    ))
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
