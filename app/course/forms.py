# -*- coding: utf-8 -*-
import time
from flask.ext.wtf import Form
from flask.ext.login import current_user
from wtforms import DateTimeField, StringField, \
    SelectField, IntegerField, TextAreaField
from ..models import ClassOrder, ClassComment

class TimeForm(Form):
    time = DateTimeField('time', format='%Y/%m/%d %H:%M')

    def create_ord(self, id):
        class_order = ClassOrder(unified_id=current_user.get_unified_id(),
                                 class_id=id,
                                 created=time.time(),
                                 time=time.mktime(self.time.data.timetuple()),
                                 name=u'',
                                 age=u'',
                                 sex=True,
                                 mobile='',
                                 email='',
                                 address=u'',
                                 remark=u'')
        return class_order


class DetailForm(Form):
    name = StringField('name')
    age = StringField('age')
    sex = SelectField('sex', choices=[(1, 'male'), (0, 'female')], coerce=int)
    cellphone = StringField('cellphone')
    address = StringField('address')

    def set_ord(self, order):
        order.name = self.name.data
        order.age = self.age.data
        order.sex = bool(self.sex.data)
        order.mobile = self.cellphone.data
        order.address = self.address.data
        return order


class ConfirmForm(Form):
    remark = TextAreaField()


class CommentForm(Form):
    stars = IntegerField('stars')
    body = TextAreaField('body')

    # TODO: validate body text.

    def create_class_comment(self, id):
        comment = ClassComment(class_id=id,
                               user_id=current_user.id,
                               stars=self.stars.data,
                               body=self.body.data,
                               created=time.time())
        return comment

