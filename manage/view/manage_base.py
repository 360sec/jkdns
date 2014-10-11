#-*- coding:utf-8 -*-
from flask import Flask ,request, g, render_template, url_for, redirect, abort
from manage import blue_print
import config

import json
from account.lib.user_lib import auth_user
from dns.lib.user_domain_lib import get_domain_list_by_user_id
from dns.lib.domain_lib import get_all_domain_dict_lib, if_user_id_have_domain_rights

from dns.model.domain import Domain

@blue_print.route("/domain_list", methods=["GET","POST"])
def domain_list():
    auth_result = auth_user()
    if not auth_result[0]:
        return redirect(auth_result[1])
    else:
        userinfo = auth_result[1]
    user_domain_list = get_domain_list_by_user_id(userinfo['user_id'])
    all_domain_list = get_all_domain_dict_lib()
    return render_template("manage_domain_list.html", userinfo=userinfo, user_domain_list=user_domain_list, all_domain_list=all_domain_list)

@blue_print.route("/domain", methods=["GET","POST"])
def domain():
    auth_result = auth_user()
    if not auth_result[0]:
        return redirect(auth_result[1])
    else:
        userinfo = auth_result[1]
    domain_id = request.args.get('domain_id', '')
    if not Domain.test_if_domain_id_exists(int(domain_id)):
        return redirect("/manage/domain_list")
    user_domain_list = get_domain_list_by_user_id(userinfo['user_id'])
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if if_user_id_have_domain_rights(userinfo['user_id'], domain_id):
        return render_template("manage_domain_have_rights.html", userinfo=userinfo, user_domain_list=user_domain_list, domain_info=domain_info)
    else:
        return render_template("manage_domain_no_rights.html", userinfo=userinfo, user_domain_list=user_domain_list, domain_info=domain_info)
