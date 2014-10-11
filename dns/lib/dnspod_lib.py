import config
import urllib, json

from lib.logger import Logger
from lib.tools import ipFormatChk

from dns.model.dns_record import Dns_record
from dns.model.domain import Domain

def stop_dnspod_record_lib(domain_id, record_id):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
            break
    if tag == 0:
        return ["false", "no this domain in dnspod"]
    result = change_dnspod_record_status(dnspod_domain_id, record_id, "disable")
    return result

def start_dnspod_record_lib(domain_id, record_id):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
            break
    if tag == 0:
        return ["false", "no this domain in dnspod"]
    result = change_dnspod_record_status(dnspod_domain_id, record_id, "enable")
    return result

def del_dnspod_record_lib(domain_id, record_id):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
            break
    if tag == 0:
        return ["false", "no this domain in dnspod"]
    result = del_dnspod_record(dnspod_domain_id, record_id)
    return result

def update_dnspod_record_lib(domain_id, record_id, name, type, line, value, ttl):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
            break
    if tag == 0:
        return ["false", "no this domain in dnspod"]
    result = update_dnspod_record(dnspod_domain_id, record_id, name, type, line, value, ttl)
    return result

def add_dnspod_record_lib(domain_id, name, type, line, value, ttl):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
            break
    if tag == 0:
        return ["false", "no this domain in dnspod"]
    result = add_dnspod_record(dnspod_domain_id, name, type, line, value, ttl)
    return result

def get_dnspod_record_list_by_domain_id_lib(domain_id):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return []
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
    if tag == 0:
        return []

    tmp_list = []
    dns_record_list = get_dnspod_record_list_by_domain_id(dnspod_domain_id)
    for dns_record in dns_record_list:
        tmp_dict = {}
        tmp_dict['id'] = dns_record['id']
        tmp_dict['domain_id'] = domain_id
        tmp_dict['name'] = dns_record['name']
        tmp_dict['line'] = dns_record['line']
        ttl = dns_record['ttl']
        tmp_dict['ttl'] = ttl
        tmp_dict['type'] = dns_record['type']
        tmp_dict['value'] = dns_record['value']
        tmp_dict['state'] = dns_record['enabled']
        if dns_record['type'] == "A" :
            if ipFormatChk(dns_record['value']):
                tmp_list.append(tmp_dict)
        else:
            tmp_list.append(tmp_dict)
    return tmp_list

def get_dnspod_record_list_by_domain_id_and_record_lib(domain_id, record):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return []
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
    if tag == 0:
        return []
    record_list = get_dnspod_record_list_by_domain_id_lib(domain_id)
    record_id = 0
    tmp_list = []
    for tmp_record in record_list:
        if tmp_record['name'] == record:
            tmp_dict = {}
            record_id = tmp_record['id']
            dns_record = get_dnspod_record_list_by_domain_id_and_record_id(dnspod_domain_id, record_id)
            tmp_dict['id'] = dns_record['id']
            tmp_dict['domain_id'] = domain_id
            tmp_dict['name'] = dns_record['sub_domain']
            tmp_dict['line'] = dns_record['record_line']
            ttl = dns_record['ttl']
            tmp_dict['ttl'] = ttl
            tmp_dict['type'] = dns_record['record_type']
            tmp_dict['value'] = dns_record['value']
            tmp_dict['state'] = dns_record['enabled']
            tmp_list.append(tmp_dict)
    return tmp_list

def get_dnspod_domain_list_list_by_domain_id_lib(domain_id):
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return []
    domain_name = domain_info[1]
    tag = 0
    dnspod_domain_list = get_dnspod_domain_list()
    for dnspod_domain in dnspod_domain_list:
        if dnspod_domain['name'] == domain_name:
            tag = 1
            dnspod_domain_id = dnspod_domain['id']
    if tag == 0:
        return []

    tmp_list = []
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json', 'domain_grade': 'D_Free', 'domain_id': dnspod_domain_id} 
    json_data = curl_dnspod(values, "/Record.Line")
    return json_data['lines']

def get_dnspod_domain_list():
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json'} 
    json_data = curl_dnspod(values, "/Domain.List")
    return json_data['domains']

def add_dnspod_record(domain_id, name, type, line, value, ttl):
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json', 'domain_id': domain_id, 'sub_domain': name, 'record_type':type, 'record_line':line, 'value':value, 'ttl':ttl} 
    json_data = curl_dnspod(values, "/Record.Create")
    Logger.action_log(str(json_data))
    if json_data['status']['code'] == "1":
        return ["true", json_data['record']['id']]
    else:
        return ["false", json_data['status']['message']]

def update_dnspod_record(domain_id, record_id, name, type, line, value, ttl):
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json', 'domain_id': domain_id, 'record_id': record_id, 'sub_domain': name, 'record_type':type, 'record_line':line, 'value':value, 'ttl':ttl} 
    json_data = curl_dnspod(values, "/Record.Modify")
    Logger.action_log(str(json_data))
    if json_data['status']['code'] == "1":
        return ["true", json_data['record']['id']]
    else:
        return ["false", json_data['status']['message']]

def del_dnspod_record(domain_id, record_id):
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json', 'domain_id': domain_id, 'record_id': record_id} 
    json_data = curl_dnspod(values, "/Record.Remove")
    Logger.action_log(str(json_data))
    if json_data['status']['code'] == "1":
        return ["true", ""]
    else:
        return ["false", json_data['status']['message']]

def get_dnspod_record_list_by_domain_id(domain_id):
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json', 'domain_id': domain_id} 
    json_data = curl_dnspod(values, "/Record.List")
    return json_data['records']

def get_dnspod_record_list_by_domain_id_and_record_id(domain_id, record_id):
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json', 'domain_id': domain_id, 'record_id': record_id} 
    json_data = curl_dnspod(values, "/Record.Info")
    return json_data['record']

def curl_dnspod(values, url):
    data = urllib.urlencode(values, url)
    result = urllib.urlopen(config.DNSPOD_URL+url, data)
    json_data=json.loads([i for i in result][0])
    result.close
    return json_data

def change_dnspod_record_status(domain_id, record_id, status):
    values = {'login_email': config.DNSPOD_USER, 'login_password': config.DNSPOD_PW, 'format': 'json', 'domain_id': domain_id, 'record_id': record_id, 'status': status} 
    json_data = curl_dnspod(values, "/Record.Status")
    Logger.action_log(str(json_data))
    if json_data['status']['code'] == "1":
        return ["true", ""]
    else:
        return ["false", json_data['status']['message']]
