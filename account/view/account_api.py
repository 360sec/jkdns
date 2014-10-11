#!/usr/bin/python
#****************************************************************#
# ScriptName: account_base.py
# Create Date: 2014-08-29 15:58
# Modify Date: 2014-08-29 15:58
#***************************************************************#
from account import blue_print

from flask import request, g, render_template, url_for, redirect, abort, session

import hashlib, json

from account.lib.userinfo_lib import check_login_lib
from account.model.userinfo import Userinfo

@blue_print.route("/login_api", methods=["GET","POST"])
def login_api():
    tmp_dict = {}
    tmp_dict['success'] = "false"
    set_cookie = 0
    if request.method == "POST":
        try:
            username = request.form['username']
            password = request.form['password']
            h=hashlib.md5()
            h.update(password)
            md5_password=h.hexdigest()
            if check_login_lib(username, md5_password):
                userinfo = Userinfo.get_userinfo_by_username(username)
                session['user_id'] = userinfo[0]
                tmp_dict['success'] = "true"
            else:
                tmp_dict['msg'] = "username or password error"
        except Exception,e:
            print e
            tmp_dict['msg'] = "no post data"
    else:
        tmp_dict['msg'] = "no post data"
    return json.dumps(tmp_dict)
