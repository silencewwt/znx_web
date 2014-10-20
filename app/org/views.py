# -*- coding: utf-8 -*-
from . import org
from .. import db
from ..models import Organization
from .forms import RegistrationForm
from flask.ext.login import login_user
from flask import redirect, url_for, render_template, flash, request


@org.route('/login', methods=['POST'])
def login():
    return render_template('auth/login.html')


@org.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        organization = Organization(cellphone=form.cellphone.data,
                            password=form.password.data)
        db.session.add(organization)
        db.session.commit()
        # token = user.generate_confirmation_token()
        # TODO: Add token.
        #send_email(user.email, 'Confirm Your Account',
        #           'auth/mail/confirm', user=user)
        #flash('A confirmation email has been sent to you by email.')
        return redirect(url_for('main.login'))
    return render_template('organ_regiter_py.html', form=form)
