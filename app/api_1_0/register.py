# -*- coding: utf-8 -*-
import json

from flask import request

from app import db
from ..models import User
from . import api
from api_constants import *


@api.route('/register')
def register():
    data = {STATUS: []}
    username = request.args.get('username')
    password = request.args.get('password')
    cellphone = request.args.get('cellphone')
    identity = request.args.get('identity')
    email = request.args.get('email')
    if User.query.filter_by(cellphone=cellphone).first():
        data[STATUS].append(CELLPHONE_EXISTS)
    if User.query.filter_by(username=username).first():
        data[STATUS].append(USERNAME_EXISTS)
    if not data[STATUS] and username and password:
        user = User(
            username=username,
            password=password,
            cellphone=cellphone,
            identity=identity
        )
        if email:
            user.email = email
        try:
            db.session.add(user)
            db.session.commit()
        except Exception:
            db.session.rollback()
            data[STATUS].append(SQL_EXCEPTION)
        else:
            data[STATUS].append(SUCCESS)
            data['user'] = {
                'username': username,
                'cellphone': cellphone,
                'identity': identity,
                'email': email
            }
    return json.dumps(data)