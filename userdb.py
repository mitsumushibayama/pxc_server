import MySQLdb
import config


def get_all_user():
    connector = MySQLdb.connect(
        user = config.user,
        passwd = config.passwd,
        host = config.host,
        db = config.db,
        charset = config.charset)

    cursor = connector.cursor()
    sql = "select * from users;"
    cursor.execute(sql)
    result = cursor.fetchall()

    response_list = []
    for row in result:
        user_id = row[0]
        user_name  = row[1]
        height = row[2]
        gender = row[3]
        user_picture_URL = row[4]

        response = {
            "user_id" : user_id,
            "user_name"  : user_name,
            "height" : height,
            "gender" : gender,
            "user_picture_URL" : user_picture_URL
        }

        response_list.append(response)
    json_response = {"user_information" : response_list}

    cursor.close
    connector.close

    return json_response


def add_user(user):
    connector = MySQLdb.connect(
        user = config.user,
        passwd = config.passwd,
        host = config.host,
        db = config.db,
        charset = config.charset)

    cursor = connector.cursor()
    sql = "insert into users values (%s, %s, %s, %s, %s);"
    cursor.execute(sql, (0, user.name, user.height, user.gender, user.user_pict$
    connector.commit()
    sql = "select * from users;"
    cursor.execute(sql)

    result = cursor.fetchall()

    for row in result:
        user_id = row[0]
        response = {
            "user_id" : user_id
        }

    cursor.close()
    connector.close()

    return response


def get_id_user(user_id):
    connector = MySQLdb.connect(
        user = config.user,
        passwd = config.passwd,
        host = config.host,
        db = config.db,
        charset = config.charset)

    cursor = connector.cursor()
    sql = "select * from users where user_id = %s;"% (user_id)
    cursor.execute(sql)
    result = cursor.fetchall()

    response_list = []
    for row in result:
        user_id = row[0]
        user_name  = row[1]
        height = row[2]
        gender = row[3]
        user_picture_URL = row[4]

    response = {
            "user_id" : user_id,
            "user_name"  : user_name,
            "height" : height,
            "gender" : gender,
            "user_picture_URL" : user_picture_URL
        }

    response_list.append(response)
    json_response = {"user_information" : response_list}

    cursor.close
    connector.close

    return json_response


def update_user(user_id,user):
    connector = MySQLdb.connect(
        user = config.user,
        passwd = config.passwd,
        host = 'config.host,
        db = config.db,
        charset = config.charset)

    cursor = connector.cursor()
    sql = "update users set name='%s', height=%s, gender='%s', user_picture_URL;"% (user.name, user.height, user.gender, user.user_picture_URL)
    cursor.execute(sql)
    connector.commit()
    sql = "select user_id from users where user_id =%s;"% (user_id)
    cursor.execute(sql)
    result = cursor.fetchall()

    for row in result:
        user_id = row[0]
        response = {
            "user_id" : user_id
        }

    return response
