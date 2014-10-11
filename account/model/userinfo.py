#!/usr/bin/python
#****************************************************************#
# ScriptName: userinfo.py
# Create Date: 2014-08-29 15:46
# Modify Date: 2014-08-29 15:46
#***************************************************************#

from lib.store import db_conn
import config

class Userinfo(object):
    def __init__(self, user_id, username, md5_password):
        self.user_id = user_id
        self.username = username

    @classmethod
    def get_userinfo_by_username(cls, username):
        sql = "select user_id, username, md5_password from userinfo where username=%s"
        rows = db_conn.query_all(sql, username)
        if len(rows) == 1:
            return rows[0]
        else:
            return False
        
    @classmethod
    def get_userinfo_by_user_id(cls, user_id):
        sql = "select user_id, username, md5_password from userinfo where user_id=%s"
        rows = db_conn.query_all(sql, user_id)
        if len(rows) == 1:
            return rows[0]
        else:
            return False
