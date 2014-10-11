#-*- coding:utf-8 -*-
from flask import Flask,session,redirect,url_for,escape,request
import json, urllib

import config

def auth_sso():
    token = request.cookies.get(config.SSO_TOKEN)
    url = "https://sso.jk.cn/auth/auth_sso_token_api?token_cookie=%s" % token
    result = urllib.urlopen(url)
    json_data=json.loads([i for i in result][0])
    result.close
    if json_data['success'] != "true":
        return False
    else:
        return json_data['userinfo']
