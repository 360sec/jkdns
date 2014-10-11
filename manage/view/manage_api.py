#-*- coding:utf-8 -*-
from flask import Flask ,request, g, render_template, url_for, redirect, abort
from manage import blue_print
from lib.logger import Logger
import config
import json

from lib.mail import send_mail
from account.lib.user_lib import auth_user
from dns.lib.user_domain_lib import get_domain_list_by_user_id
from dns.lib.domain_lib import get_all_domain_dict_lib, if_user_id_have_domain_rights
from dns.lib.dns_record_lib import add_dns_record_lib, stop_dns_record_lib, start_dns_record_lib, del_dns_record_lib, update_dns_record_lib
from dns.lib.dnspod_lib import add_dnspod_record_lib, stop_dnspod_record_lib, start_dnspod_record_lib, del_dnspod_record_lib, update_dnspod_record_lib

from dns.model.domain import Domain

@blue_print.route("/update_record_api", methods=["GET","POST"])
def update_record_api():
    tmp_dict = {}
    tmp_dict['success'] = "False"
    auth_result = auth_user()
    if not auth_result[0]:
        tmp_dict['msg'] = "no sso auth"
        return json.dumps(tmp_dict)
    else:
        userinfo = auth_result[1]
    if request.method == "POST":
        try:
            domain_id = request.form['domain_id']
            record_id = request.form['record_id']
            domain_info = Domain.get_domain_by_domain_id(domain_id)
            name = request.form['name']
            type = request.form['type']
            line = request.form['line']
            line = line.encode('utf-8')
            value = request.form['value']
            ttl = request.form['ttl']
            if if_user_id_have_domain_rights(userinfo['user_id'], domain_id):
                Logger.action_log(userinfo['username']+" update record ")
                if domain_info[2] == "dnspod":
                    result = update_dnspod_record_lib(domain_id, record_id, name, type, line, value, ttl)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
                elif domain_info[2] == "local_bind":
                    result = update_dns_record_lib(domain_id, record_id, name, ttl, type, value, line)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
            else:
                tmp_dict['msg'] = "no this domain rights"
                return json.dumps(tmp_dict)
        except Exception,e:
            print e
            tmp_dict['msg'] = "unknown error"
            return json.dumps(tmp_dict)
    else:
        tmp_dict['msg'] = "no post data"
        return json.dumps(tmps_dict)

@blue_print.route("/add_record_api", methods=["GET","POST"])
def add_record_api():
    tmp_dict = {}
    tmp_dict['success'] = "False"
    auth_result = auth_user()
    if not auth_result[0]:
        tmp_dict['msg'] = "no sso auth"
        return json.dumps(tmp_dict)
    else:
        userinfo = auth_result[1]
    if request.method == "POST":
        try:
            domain_id = request.form['domain_id']
            domain_info = Domain.get_domain_by_domain_id(domain_id)
            name = request.form['name']
            type = request.form['type']
            line = request.form['line']
            line = line.encode('utf-8')
            value = request.form['value']
            ttl = request.form['ttl']
            if if_user_id_have_domain_rights(userinfo['user_id'], domain_id):
                Logger.action_log(userinfo['username']+" add record ")
                if domain_info[2] == "dnspod":
                    result = add_dnspod_record_lib(domain_id, name, type, line, value, ttl)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
                elif domain_info[2] == "local_bind":
                    result = add_dns_record_lib(domain_id, name, ttl, type, value, line)
                    tmp_dict['success'] = result[0]
                    print result[1]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
            else:
                tmp_dict['msg'] = "no this domain rights"
                return json.dumps(tmp_dict)
        except Exception,e:
            print e
            tmp_dict['msg'] = "unknown error"
            return json.dumps(tmp_dict)
    else:
        tmp_dict['msg'] = "no post data"
        return json.dumps(tmps_dict)
    
@blue_print.route("/stop_record_api", methods=["GET","POST"])
def stop_record_api():
    tmp_dict = {}
    tmp_dict['success'] = "False"
    auth_result = auth_user()
    if not auth_result[0]:
        tmp_dict['msg'] = "no sso auth"
        return json.dumps(tmp_dict)
    else:
        userinfo = auth_result[1]
    if request.method == "POST":
        try:
            domain_id = request.form['domain_id']
            domain_info = Domain.get_domain_by_domain_id(domain_id)
            record_id = request.form['record_id']
            if if_user_id_have_domain_rights(userinfo['user_id'], domain_id):
                Logger.action_log(userinfo['username']+" stop record ")
                if domain_info[2] == "dnspod":
                    result = stop_dnspod_record_lib(domain_id, record_id)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
                elif domain_info[2] == "local_bind":
                    result = stop_dns_record_lib(domain_id, record_id)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
            else:
                tmp_dict['msg'] = "no this domain rights"
                return json.dumps(tmp_dict)
        except Exception,e:
            print e
            tmp_dict['msg'] = "unknown error"
            return json.dumps(tmp_dict)
    else:
        tmp_dict['msg'] = "no post data"
        return json.dumps(tmps_dict)
    
@blue_print.route("/start_record_api", methods=["GET","POST"])
def start_record_api():
    tmp_dict = {}
    tmp_dict['success'] = "False"
    auth_result = auth_user()
    if not auth_result[0]:
        tmp_dict['msg'] = "no sso auth"
        return json.dumps(tmp_dict)
    else:
        userinfo = auth_result[1]
    if request.method == "POST":
        try:
            domain_id = request.form['domain_id']
            domain_info = Domain.get_domain_by_domain_id(domain_id)
            record_id = request.form['record_id']
            if if_user_id_have_domain_rights(userinfo['user_id'], domain_id):
                Logger.action_log(userinfo['username']+" start record ")
                if domain_info[2] == "dnspod":
                    result = start_dnspod_record_lib(domain_id, record_id)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
                elif domain_info[2] == "local_bind":
                    result = start_dns_record_lib(domain_id, record_id)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
            else:
                tmp_dict['msg'] = "no this domain rights"
                return json.dumps(tmp_dict)
        except Exception,e:
            print e
            tmp_dict['msg'] = "unknown error"
            return json.dumps(tmp_dict)
    else:
        tmp_dict['msg'] = "no post data"
        return json.dumps(tmps_dict)
    
@blue_print.route("/del_record_api", methods=["GET","POST"])
def del_record_api():
    tmp_dict = {}
    tmp_dict['success'] = "False"
    auth_result = auth_user()
    if not auth_result[0]:
        tmp_dict['msg'] = "no sso auth"
        return json.dumps(tmp_dict)
    else:
        userinfo = auth_result[1]
    if request.method == "POST":
        try:
            domain_id = request.form['domain_id']
            domain_info = Domain.get_domain_by_domain_id(domain_id)
            record_id = request.form['record_id']
            if if_user_id_have_domain_rights(userinfo['user_id'], domain_id):
                Logger.action_log(userinfo['username']+" del record ")
                if domain_info[2] == "dnspod":
                    result = del_dnspod_record_lib(domain_id, record_id)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
                elif domain_info[2] == "local_bind":
                    result = del_dns_record_lib(domain_id, record_id)
                    tmp_dict['success'] = result[0]
                    tmp_dict['msg'] = result[1]
                    return json.dumps(tmp_dict)
            else:
                tmp_dict['msg'] = "no this domain rights"
                return json.dumps(tmp_dict)
        except Exception,e:
            print e
            tmp_dict['msg'] = "unknown error"
            return json.dumps(tmp_dict)
    else:
        tmp_dict['msg'] = "no post data"
        return json.dumps(tmps_dict)
