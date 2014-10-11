#-*- coding:utf-8 -*-
from flask import Flask, session, redirect, url_for, escape, request

import config

from account.lib.sso_lib import auth_sso
from account.model.userinfo import Userinfo

def auth_user():
    if config.RUN_METHOD == "sso":
        url = request.url
        sso_userinfo = auth_sso()
        if not sso_userinfo:
            redirect_url = "/sso?redirect_url=" + url
            return [False, redirect_url]
        else:
            local_userinfo = Userinfo.get_userinfo_by_username(sso_userinfo['username'])
            if not local_userinfo:
                redirect_url = config.SSO_WEBSITE
                return [False, redirect_url]
            else:
                userinfo = {}
                userinfo['user_id'] = local_userinfo[0]
                userinfo['username'] = local_userinfo[1]
                userinfo['chinese_name'] = sso_userinfo['chinese_name']
                return [True, userinfo]
    else:
        if 'user_id' in session:
            user_id = session['user_id']
            local_userinfo = Userinfo.get_userinfo_by_user_id(user_id)
            userinfo = {}
            userinfo['user_id'] = user_id
            userinfo['username'] = local_userinfo[1]
            return [True, userinfo]
        else:
            return [False, "/account/login"]
