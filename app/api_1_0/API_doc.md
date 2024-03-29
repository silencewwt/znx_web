Android API
====

mobile_confirm
---
    URL:
        /api/v1.0/mobile_confirm?mobile=
    method:
        get
    parameters:
        mobile
    json:
        {"status": 0}
        
        status: 0 for success, 5003 for message confirm fail

register
----
    URL:
        /api/v1.0/register?&password=&mobile=&identity=&email=&verify_code=
    method:
        get
    parameters:
        password
        mobile
        email
        identity: uuid
        verify_code
    json:
        {"status": 0, "user": {"username": "", "mobile": "", "identity": "", "email": "", "unified": "", "chat_line": ""}}
        
        status: 0 for success, 1007 for verify code incorrect, 1002 for existing mobile, 1004 for existing username
        user: a dictionary of user's information
            username
            mobile
            identity
            email
            unified
            chat_line: the last id for chat_line

login
----
    URL:
        /api/v1.0/login?mobile=&password=&identity=
    method:
        get
    parameters:
        username
        password
        identity: mobile + uuid + 0
    json:
        {"status": 0,
         "user": {"username": "", "mobile": "", "email": "", "identity": "", "chat_line": "", "unified": ""}}
        
        status: 0 for success, 1000 for login failed
        user: a dictionary of user's information
            username: if login fail, username, mobile, email, identity won't return
            mobile
            email
            identity
            chat_line
            unified

reset_password
---
    URL:
        /api/v1.0/reset_password?mobile=&password=&verify_code=
    method:
        get
    parameters:
        mobile
        password
        verify_code
    json:
        {"status": 0}
        
        status: 0 for success, 1007 for verify code incorrect, 1003 for user not exist

organization_filter
---
    URL:
        /api/v1.0/organization_filter?city=&district=&profession&page=&type=
        /api/v1.0/organization_filter?distance=&latitude=&longitude=&page=&type=
    method:
        get
    parameters:
        city: unicode name of a city 
        district: unicode name of a district, if value is 'all', will return all organizations in the city by pagination
        profession: unicode name of  profession, if value is 'all', will return all organizations in the city by pagination
        distance: optional, nearby distance. if value is not empty, latitude and longitude can't be empty, return nearby organizations
        latitude: optional
        longitude: optional
        page: default first page
        type: unicode of 学校 or 机构 or other type
    json:
        {"status": 0,
         "organizations": [{"id": "", "name": "", "city": "", "district": "", "photo": "", "logo": "", "intro": ""}]}
         
        status: 0 for success, 5001 for parameter error
        organizations: a list of organizations
            id
            name: unicode
            city: unicode
            district: unicode
            photo: url of photo
            logo: url of logo
            intro: unicode

organization_search
---
    URL:
        /api/v1.0/organization_search?name=&distance=&longitude=&latitude=&page=
    method:
        get
    parameters:
        name: key of search organization
        distance: optional, nearby distance. if value is not empty, latitude and longitude can't be empty
        longitude
        latitude
    json:
        {"status": 0,
         "organizations": [{"id": "", "name": "", "city": "", "district": "", "photo": "", "logo": "", "intro": "", "distance": ""}]}
        
        status: 0 for success
        organizations: a list of organizations
            id
            name
            city
            district
            photo
            logo
            intro
            distance

organization_detail
---
    URL:
        /api/v1.0/organization_detail?organization=
    method:
        get
    parameters:
        organization: id of organization
    json:
        {"status": 0,
         "organization": {"id": "", "name": "", "city": "", "district": "", "photo": "", "logo": "", "intro": "",
            "address": "", "mobile": "", "comments_count": "", "stars": "", "traffic": ""}}
         
        status: 0 for success, 2000 for organization not exist
        organization
            id
            name
            city
            district
            photo: url of photo
            logo: url of logo
            intro
            address
            mobile
            comments_count
            stars: a float number for stars
            traffic: nearby traffic information

organization_comment
---
    URL:
        /api/v1.0/organization_comment?organization=&user_id&comment=&stars=
    method:
        get
    parameters:
        organization: id of organization
        user_id
        comment
        stars
    json:
        {"status": 0}
        
        status: 0 for success, 2000 for organization not exist, 5001 for parameter error

organization_comment_list
---
    URL:
        /api/v1.0/organization_comment_list?organization=&page=
    method:
        get
    parameters:
        organization: id of organization
        page
    json:
        {"status": 0,
         "organization_comments": [{"comment": "", "created": "", "stars": "", "username": ""}]}
        
        status: 0 for success, 2000 for organization not exist, 5001 for parameter error
        organization_comments: a list of organization_comments
            comment
            stars
            created: unix timestamp, seconds from 1970.1.1 00:00:00
            username

class_list
---
    URL:
        /api/v1.0/class_list?organization=&page=
    method:
        get
    parameters:
        organization: id of organization
        page
    json:
        {"status": 0,
         "classes": [{"id": "", "name": "", "age": "", "price": "", "days": ""}]}
        
        status: 0 for success
        classes: a list of classes
            id
            name
            age
            price
            days

class_detail
---
    URL:
        /api/v1.0/class_detail?class=
    method:
        get
    parameters:
        class: id of class
    json:
        {"status": 0,
         "class": {"id": "", "name": "", "age": "", "price": "", "intro": "", "is_tastable": "", "consult_time": "",
            "comments_count": "", "days": "", "stars": ""}}
        
        status: 0 for success, 2001 for class not exist
        class: a dict of class
            id
            name
            age
            price
            intro
            is_tastable
            consult_time
            start_time
            end_time
            comments_count
            days
            stars

class_sign_up
---
    URL:
        /api/v1.0/class_sign_up?class=&user_id=&name=&mobile=&age=&sex=&address=&remark=&email=&time=
    method:
        get
    parameters:
        class: id of class
        user_id
        name
        mobile
        age
        sex
        address
        remark
        email
        time: unix timestamp, time of class
    json:
        {"status": 0}
        
        status: 0 for success, 5002 for lack of parameters

class_comment
---
    URL:
        /api/v1.0/class_comment?class=&user_id&comment=&stars=
    method:
        get
    parameters:
        class: id of class
        user_id
        comment
        stars
    json:
        {"status": 0}
        
        status: 0 for success, 2001 for class not exist, 5000 for sql exception, 5001 for parameter error

class_comment_list
---
    URL:
        /api/v1.0/class_comment_list?class=&page=
    method:
        get
    parameters:
        class: id of class
        page
    json:
        {"status": 0,
         "class_comments": [{"comment": "", "created": "", "stars": "", "username": ""}]}
        
        status: 0 for success, 2001 for class not exist, 5001 for parameter error
        class_comments: a list of class_comments
            comment
            stars
            created
            username

activity_list
---
    URL:
        /api/v1.0/activity_list?organization=&page=
    method:
        get
    parameters:
        organization: id of organization
        page
    json:
        {"status": 0,
         "activities": [{"id": "", "name": "", "age": "", "price": "", "start_time": "", "end_time": ""}]}
        
        status: 0 for success
        activities: a list of activities
            id
            name
            age
            price
            start_time
            end_time

activity_detail
---
    URL:
        /api/v1.0/activity_detail?activity=
    method:
        get
    parameters:
        activity: id of activity
    json:
        {"status": 0,
         "activity": {"id": "", "name": "", "age": "", "price": "", "intro": "", "start_time": "", "end_time": "",
            "comments_count": "", "stars": ""}}
        
        status: 0 for success, 2002 fot activity not exist
        activity: a dict of activity
            id
            name
            age
            price
            intro
            is_tastable
            consult_time
            start_time
            end_time
            comments_count
            stars

activity_sign_up
---
    URL:
        /api/v1.0/activity_sign_up?class=&user_id=&name=&mobile=&age=&sex=&address=&remark=&email=
    method:
        get
    parameters:
        activity: id of activity
        user_id
        name
        mobile
        age
        sex: 0 for female, 1 for male
        address
        remark
        email: optional
    json:
        {"status": 0}
        
        status: 0 for success, 5002 for lack of parameters
    
activity_comment
---
    URL:
        /api/v1.0/activity_comment?activity=&user_id&comment=&stars=
    method:
        get
    parameters:
        activity: id of activity
        user_id
        comment
        stars
    json:
        {"status": 0}
        
        status: 0 for success, 2002 for activity not exist, 5000 for sql exception, 5001 for parameter error

activity_comment_list
---
    URL:
        /api/v1.0/activity_comment_list?activity=&page=
    method:
        get
    parameters:
        activity: id of activity
        page
    json:
        {"status": 0,
         "activity_comments": [{"comment": "", "created": "", "stars": "", "username": ""}]}
        
        status: 0 for success, 2002 for activity not exist, 5001 for parameter error
        activity_comments: a list of activity_comments
            comment
            stars
            created
            username

order_list_or_detail
---
    URL:
        /api/v1.0/order_list?user_id=&page=
    method:
        get
    parameters:
        user_id
        page
    json:
        {"status": 0,
         "class_orders": [{"class_order_id": "", "created": "", "class_name": "", "org_name": "", "user_name": "",
         "age": "", "user_sex": "", "user_mobile": "", "user_address": "", "user_remark": "", "comments_count": "",
         "user_age": "", "price": "", "days": ""}],
         "activity_orders": [{"activity_order_id": "", "created": "", "activity_name", "", "org_name": "",
         "user_name": "", "age": "", "user_sex": "", "user_mobile": "", "email": "", "user_address": "",
         "user_remark": "", "comments_count": "", "user_age": "", "price": "", "start_time": "", "end_time": ""}]}
         
         status: 0 for success, 1003 for user not exist
         class_orders/activity_orders
            class_order_id/activity_order_id
            created
            class_name/activity_name
            start_time/end_time/days
            price
            org_name
            user_name: user's name
            user_age
            user_sex: 0 for female, 1 for male
            user_mobile
            user_email
            user_address: address of activity or organization
            user_remark: user's remark of this class
            comments_count

order_synchronize
---
    URL:
        /api/v1.0/order_synchronize?user_id=&uuid=
    method:
        get
    parameters:
        user_id
        uuid
    json:
        {"status":0}
        
        status: 0 for success, 1003 for user not exist

requirement_list
---
    URL:
        /api/v1.0/requirement_list?page=
    method:
        get
    parameters:
        page
    json:
        {"status": 0, "registers": [{"name": "", "mobile": "", "need": "", "time": ""}]}
        
        status: 0 for success, 5001 for parameter error
        registers: a list of registers
            name
            mobile
            need
            time

requirement_sign_up
---
    URL:
        /api/v1.0/requirement_sign_up?name=&mobile=&need=&city=
    method:
        get
    parameters:
        username
        mobile
        need
        city
    json:
        {"status": 0}
        
        status: 0 for success, 5000 for sql exception 5001 for parameter error
        
get_district_profession
---
    URL:
        /api/v1.0/get_district_profession?city=
    method:
        get
    parameters:
        city
    json:
        {"status": 0, "districts": [""], "professions": [""]}
        
        status: 0 for success, 3000 for city not exist
        districts: a list of districts in city
        professions: a list of all professions

get_cities
---
    URL:
        /api/v1.0/get_cities
    method:
        get
    json:
        {"status": 0, "cities": [""]}
        
        status: 0 for success
        cities: a list of the unicode name of all cities

chat_get
---
    URL:
        /api/v1.0/chat_get?user_id=&last_id=&unified=
    method:
        get
    parameters:
        user_id
        last_id
        unified
    json:
        {"status": 0, "chat_lines": ["chat_line": "", "content": "", "created": "", "org_id": "", "org_name": ""]}
        
        status: 0 for success, 5001 for parameter error
        chat_lines: a list of chat line
            chat_line
            content
            created
            org_id
            org_name

chat_post
---
    URL:
        /api/v1.0/chat_post?user_id=&unified=&content=&org_id=
    method:
        get
    parameters:
        user_id
        unified
        content
        org_id
    json:
        {"status": 0}
        
        status: 0 for success, 5001 for parameter error

CONSTANTS
---
    SUCCESS = 0

    LOGIN_FAILED = 1000
    MOBILE_NOT_EXIST = 1001
    MOBILE_EXIST = 1002
    USER_NOT_EXIST = 1003
    USERNAME_EXIST = 1004
    ACCESS_RESTRICTED = 1005
    ORDER_NOT_EXIST = 1006
    VERIFY_CODE_INCORRECT = 1007
    
    ORGANIZATION_NOT_EXIST = 2000
    CLASS_NOT_EXIST = 2001
    ACTIVITY_NOT_EXIST = 2002
    
    CITY_NOT_EXIST = 3000
    PROFESSION_NOT_EXIST = 3001
    TYPE_NOT_EXIST = 3002
    
    SQL_EXCEPTION = 5000
    PARAMETER_ERROR = 5001
    LACK_OF_PARAMETER = 5002
    MESSAGE_CONFIRM_FAIL = 5003
    