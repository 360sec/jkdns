#-*- coding:utf-8 -*-
from flask import Flask,session,redirect,url_for,escape,request
from account.lib.sso_lib import auth_sso

from account.model.userinfo import Userinfo

def check_login_lib(username, md5_password):
    userinfo = Userinfo.get_userinfo_by_username(username)
    if not userinfo:
        return False
    if userinfo[2] == md5_password:
        return True
    else:
        return False
