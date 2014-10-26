# -*- coding: utf-8 -*-
import os
import time
from uuid import uuid4
from . import org
from .. import db
from ..models import Organization, Type,\
    Profession, Property, Size, Location, Class, Activity, City
from .forms import RegistrationForm, DetailForm, CertificationForm, LoginForm
from ..user.forms import LoginForm as UserLoginForm
from flask.ext.login import login_user, login_required, current_user
from flask import redirect, url_for, render_template,\
    flash, current_app, request
from ..utils.query import get_location

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
            return redirect(request.args.get('next') or url_for('main.index'))
        flash(u'用户名密码错误')
    return render_template('login_choose_py.html',
                           user_form=user_form,
                           org_form=org_form)


@org.route('/register', methods=['GET', 'POST'])
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
        return redirect(url_for('main.index'))
    return render_template('organ_regiter_py.html', form=form)


@org.route('/detail', methods=['GET', 'POST'])
@login_required
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
        # TODO: correct choose form.
    form.location = get_location()
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
        print form.location_id.data
        # token = user.generate_confirmation_token()
        # TODO: Add token.
        # TODO: add macro in template for errors.
        #send_email(user.email, 'Confirm Your Account',
        #           'auth/mail/confirm', user=user)
        #flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main.index'))
    return render_template('organ_regiter2_py.html', form=form)


@org.route('/certification', methods=['GET', 'POST'])
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

        certification = uuid4().hex
        ext = form.certification.data.filename.rsplit('.', 1)[-1]
        file_path = os.path.join(path, certification+'.'+ext)
        form.certification.data.save(file_path)

        photo = uuid4().hex
        ext = form.photo.data.filename.rsplit('.', 1)[-1]
        file_path = os.path.join(path, photo+'.'+ext)
        form.photo.data.save(file_path)
        current_user.authorization = certification
        current_user.photo = photo
        db.session.add(current_user)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('organ_regiter3_py.html', form=form)


@org.route('/home/<int:id>')
def home(id):
    org = Organization.query.get_or_404(id)
    classes = Class.query.filter_by(organization_id=id).all()
    activities = Activity.query.filter_by(organization_id=id).all()
    return render_template('organindex_py.html',
                           org=org,
                           classes=classes,
                           activities=activities)
from .forms import CourseForm
@org.route('/course/add', methods=['GET', 'POST'])
def add_course():
    course_form=CourseForm()
    course_form.create_choices()
    if course_form.validate_on_submit():
        course = course_form.create_course()
        db.session.add(course)
        db.session.commit()
        return redirect(url_for('main.index'))
    return render_template('origanclassadd_py.html', form=course_form)


@org.route('/activity/add')
def add_activity():
    return render_template('origanactadd_py.html')
