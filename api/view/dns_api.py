#-*- coding:utf-8 -*-
from flask import request,g,render_template,url_for,redirect,abort
from api  import blue_print
import json

from dns.model.domain import Domain
from dns.model.dns_record import Dns_record

from dns.lib.domain_lib import get_all_domain_dict_lib
from dns.lib.dns_record_lib import get_dns_record_list_by_domain_id_lib, get_dns_record_list_by_domain_id_and_record_lib
from dns.lib.dnspod_lib import get_dnspod_record_list_by_domain_id_lib, get_dnspod_domain_list_list_by_domain_id_lib, get_dnspod_record_list_by_domain_id_and_record_lib

import config

@blue_print.route("/get_all_domain_api")
def get_all_domain():
    tmp_dict = {}
    tmp_dict['success'] = "true"
    tmp_dict['domain_list'] = get_all_domain_dict_lib()
    return json.dumps(tmp_dict)

@blue_print.route("/get_dns_record_by_domain_name_api", methods=["GET","POST"])
def get_dns_record_by_domain_name_api():
    tmp_dict = {}
    tmp_dict['success'] = "false"
    if request.method == "POST":
        domain_name = request.form['domain_name']
        domain_info = Domain.get_domain_by_domain_name(domain_name)
        if domain_info:
            if domain_info[2] == "local_bind":
                tmp_dict['success'] = "true"
                tmp_dict['dns_record_list'] = get_dns_record_list_by_domain_id_lib(domain_info[0])
            elif domain_info[2] == "dnspod":
                tmp_dict['success'] = "true"
                tmp_dict['dns_record_list'] = get_dnspod_record_list_by_domain_id_lib(domain_info[0])
        else:
            tmp_dict['msg'] = "no this domain_name"
    else:
        tmp_dict['msg'] = "no post data"
    return json.dumps(tmp_dict)

@blue_print.route("/get_dns_record_by_domain_id_api", methods=["GET","POST"])
def get_dns_record_by_domain_id_api():
    tmp_dict = {}
    tmp_dict['success'] = "false"
    if request.method == "POST":
        domain_id = request.form['domain_id']
        domain_info = Domain.get_domain_by_domain_id(domain_id)
        if domain_info:
            if domain_info[2] == "local_bind":
                tmp_dict['success'] = "true"
                tmp_dict['dns_record_list'] = get_dns_record_list_by_domain_id_lib(domain_id)
            elif domain_info[2] == "dnspod":
                tmp_dict['success'] = "true"
                tmp_dict['dns_record_list'] = get_dnspod_record_list_by_domain_id_lib(domain_id)
        else:
            tmp_dict['msg'] = "no this domain_name"
    else:
        tmp_dict['msg'] = "no post data"
    return json.dumps(tmp_dict)

@blue_print.route("/get_domain_line_list_by_domain_id_api", methods=["GET","POST"])
def get_domain_line_list_by_domain_id_api():
    tmp_dict = {}
    tmp_dict['success'] = "false"
    if request.method == "POST":
        domain_id = request.form['domain_id']
        domain_info = Domain.get_domain_by_domain_id(domain_id)
        if domain_info:
            if domain_info[2] == "local_bind":
                tmp_dict['success'] = "true"
                tmp_dict['domain_line_list'] = config.LOCAL_BIND_LINE
            elif domain_info[2] == "dnspod":
                tmp_dict['success'] = "true"
                tmp_dict['domain_line_list'] = get_dnspod_domain_list_list_by_domain_id_lib(domain_id)
        else:
            tmp_dict['msg'] = "no this domain_id"
    else:
        tmp_dict['msg'] = "no post data"
    return json.dumps(tmp_dict)

@blue_print.route("/get_domain_line_list_by_domain_name_api", methods=["GET","POST"])
def get_domain_line_list_by_domain_name_api():
    tmp_dict = {}
    tmp_dict['success'] = "false"
    if request.method == "POST":
        domain_name = request.form['domain_name']
        domain_info = Domain.get_domain_by_domain_name(domain_name)
        if domain_info:
            if domain_info[2] == "local_bind":
                tmp_dict['success'] = "true"
                tmp_dict['domain_line_list'] = config.LOCAL_BIND_LINE
            elif domain_info[2] == "dnspod":
                tmp_dict['success'] = "true"
                tmp_dict['domain_line_list'] = get_dnspod_domain_list_list_by_domain_id_lib(domain_info[0])
        else:
            tmp_dict['msg'] = "no this domain_name"
    else:
        tmp_dict['msg'] = "no post data"
    return json.dumps(tmp_dict)

@blue_print.route("/get_dns_record_info_api", methods=["GET","POST"])
def get_dns_record_info_api():
    tmp_dict = {}
    tmp_dict['success'] = "false"
    if request.method == "POST":
        domain_name = request.form['domain_name']
        record = request.form['record']
        domain_info = Domain.get_domain_by_domain_name(domain_name)
        if domain_info:
            if domain_info[2] == "local_bind":
                tmp_dict['success'] = "true"
                tmp_dict['record_list'] = get_dns_record_list_by_domain_id_and_record_lib(domain_info[0], record)
            elif domain_info[2] == "dnspod":
                tmp_dict['success'] = "true"
                tmp_dict['record_list'] = get_dnspod_record_list_by_domain_id_and_record_lib(domain_info[0], record)
        else:
            tmp_dict['msg'] = "no this domain_name"
    else:
        tmp_dict['msg'] = "no post data"
    return json.dumps(tmp_dict)
