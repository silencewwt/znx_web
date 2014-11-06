# -*- coding: utf-8 -*-
SUCCESS = 0

LOGIN_FAILED = 1000
MOBILE_NOT_EXIST = 1001
MOBILE_EXIST = 1002
USER_NOT_EXIST = 1003
USERNAME_EXIST = 1004
ACCESS_RESTRICTED = 1005
ORDER_NOT_EXIST = 1006

ORGANIZATION_NOT_EXIST = 2000
CLASS_NOT_EXIST = 2001
ACTIVITY_NOT_EXIST = 2002

CITY_NOT_EXIST = 3000
PROFESSION_NOT_EXIST = 3001

SQL_EXCEPTION = 5000
PARAMETER_ERROR = 5001
LACK_OF_PARAMETER = 5002
MESSAGE_CONFIRM_FAIL = 5003

PER_PAGE = 10
EARTH_CIRCUMFERENCE = 40000


MESSAGE_API_SUCCESS = 2
MESSAGE_API_ACCOUNT = u'cf_zainaxue'
MESSAGE_API_PASSWORD = u'zainaxue'
MESSAGE_API_CONTENT = u'尊敬的在哪学用户，您的验证码为{verify_code}，请您尽快完成操作，感谢您的使用！【在哪学】'
MESSAGE_API_CONTENT_TEST = u'您的验证码是：{verify_code}。请不要把验证码泄露给其他人。'
MESSAGE_API_URL = u'http://106.ihuyi.cn/webservice/sms.php?method=Submit&account={account}&password={password}' \
                  u'&mobile={mobile}&content={content}'
