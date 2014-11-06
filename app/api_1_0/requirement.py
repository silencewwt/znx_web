# -*- coding: utf-8 -*-
import json
import time

from flask import request

from app import db
from ..models import Register, City
from . import api
from api_constants import *


@api.route('/requirement_list')
def requirement_list():
    data = {'registers': []}
    page = request.values.get('page', 1, type=int)
    register_list = Register.query.order_by(-Register.created).paginate(page, PER_PAGE, False).items
    for register in register_list:
        register_dict = {
            'name': register.name[0] + u'同学',
            'mobile': register.mobile[:3] + '*' * 4 + register.mobile[-4:],
            'need': register.need,
            'time': register.created
        }
        data['registers'].append(register_dict)
    data['status'] = SUCCESS
    return json.dumps(data)


@api.route('/requirement_sign_up')
def requirement_sign_up():
    data = {}
    name = request.args.get('name', '').encode('utf8')
    city = request.args.get('city', '').encode('utf8')
    need = request.args.get('need', '').encode('utf8')
    mobile = request.args.get('mobile')
    city = City.query.filter_by(city=city).first()
    if name and mobile and need and city:
        register = Register(
            name=name,
            mobile=mobile,
            need=need,
            city_id=city.id,
            created=time.time()
        )
        db.session.add(register)
        db.session.commit()
        data['status'] = SUCCESS
    else:
        data['status'] = PARAMETER_ERROR
    return json.dumps(data)