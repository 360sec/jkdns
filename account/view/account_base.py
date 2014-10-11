#!/usr/bin/python
#****************************************************************#
# ScriptName: account_base.py
# Create Date: 2014-08-29 15:58
# Modify Date: 2014-08-29 15:58
#***************************************************************#
from account import blue_print

from flask import request, g, render_template, url_for, redirect, abort, session

import config

from account.lib.user_lib import auth_user

@blue_print.route("/sso")
def sso():
    return render_template("sso.html")

@blue_print.route("/login")
def login():
    auth_result = auth_user()
    if not auth_result[0]:
        return render_template("account_login.html")
    else:
        return redirect(config.INDEXPAGE)
    
@blue_print.route("/logout")
def logout():
    if config.RUN_METHOD == "sso":
        return redirect(config.SSO_WEBSITE+"/auth/logout?redirect_url="+config.LOCAL_WEBSITE)
    else:
        session.pop('user_id', None)
        return redirect("/account/login")
