from dns.model.dns_record import Dns_record
from dns.model.domain import Domain
from lib.logger import Logger

from lib.tools import ipFormatChk

def get_dns_record_list_by_domain_id_and_record_lib(domain_id, record):
    tmp_list = []
    dns_record_list = Dns_record.get_dns_record_list_by_domain_id_and_record(domain_id, record)
    for dns_record in dns_record_list:
        tmp_dict = {}
        tmp_dict['id'] = dns_record[0]
        tmp_dict['domain_id'] = dns_record[1]
        tmp_dict['name'] = dns_record[2]
        tmp_dict['line'] = "default"
        tmp_dict['ttl'] = dns_record[3]
        tmp_dict['type'] = dns_record[4]
        tmp_dict['value'] = dns_record[5]
        tmp_dict['state'] = dns_record[7]
        if dns_record[4] == "A" and ipFormatChk(dns_record[5]):
            tmp_list.append(tmp_dict)
        elif dns_record[4] == "CNAME":
            tmp_list.append(tmp_dict)
    return tmp_list

def get_dns_record_list_by_domain_id_lib(domain_id):
    tmp_list = []
    dns_record_list = Dns_record.get_dns_record_list_by_domain_id(domain_id)
    for dns_record in dns_record_list:
        tmp_dict = {}
        tmp_dict['id'] = dns_record[0]
        tmp_dict['domain_id'] = dns_record[1]
        tmp_dict['name'] = dns_record[2]
        tmp_dict['line'] = "default"
        tmp_dict['ttl'] = dns_record[3]
        tmp_dict['type'] = dns_record[4]
        tmp_dict['value'] = dns_record[5]
        tmp_dict['state'] = dns_record[7]
        if dns_record[4] == "A" and ipFormatChk(dns_record[5]):
            tmp_list.append(tmp_dict)
        elif dns_record[4] == "CNAME":
            tmp_list.append(tmp_dict)
    return tmp_list

def update_dns_record_lib(domain_id, record_id, record, ttl, type, value, line):
    Logger.action_log(str([domain_id, record_id, record, ttl, type, value, line]))
    if type=="A":
        if Dns_record.type_a_count(domain_id, record, value) > 0:
            return ["false", "A record already exists"]
        elif Dns_record.type_cname_all_count(domain_id, record) > 0:
            return ["false", "CNAME record already exists"]
        elif not ipFormatChk(value):
            return ["false", "The A record value ipaddr not legal"]
        else:
            result = Dns_record.update_dns_record(domain_id, record_id, record, ttl, type, value, line)
            return ["true", result]
    elif type == "CNAME":
        if Dns_record.type_cname_count(domain_id, record, value) > 0:
            return ["false", "CNAME record already exists"]
        elif Dns_record.type_a_all_count(domain_id, record) > 0:
            return ["false", "A record already exists"]
        else:
            result = Dns_record.update_dns_record(domain_id, record_id, record, ttl, type, value, line)
            return ["true", result]

def add_dns_record_lib(domain_id, record, ttl, type, value, line):
    Logger.action_log(str([domain_id, record, ttl, type, value, line]))
    if type=="A":
        if Dns_record.type_a_count(domain_id, record, value) > 0:
            return ["false", "A record already exists"]
        elif Dns_record.type_cname_all_count(domain_id, record) > 0:
            return ["false", "CNAME record already exists"]
        elif not ipFormatChk(value):
            return ["false", "The A record value ipaddr not legal"]
        else:
            result = Dns_record.add_dns_record(domain_id, record, ttl, type, value, line)
            return ["true", result]
    elif type == "CNAME":
        if Dns_record.type_cname_count(domain_id, record, value) > 0:
            return ["false", "CNAME record already exists"]
        elif Dns_record.type_a_all_count(domain_id, record) > 0:
            return ["false", "A record already exists"]
        else:
            result = Dns_record.add_dns_record(domain_id, record, ttl, type, value, line)
            return ["true", result]

def stop_dns_record_lib(domain_id, record_id):
    Logger.action_log(str([domain_id, record_id]))
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    result = Dns_record.change_dns_record_state(domain_id, record_id, '0')
    return ["true", "success"]

def start_dns_record_lib(domain_id, record_id):
    Logger.action_log(str([domain_id, record_id]))
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    result = Dns_record.change_dns_record_state(domain_id, record_id, '1')
    return ["true", "success"]

def del_dns_record_lib(domain_id, record_id):
    Logger.action_log(str([domain_id, record_id]))
    domain_info = Domain.get_domain_by_domain_id(domain_id)
    if not domain_info:
        return ["false","no this domain"]
    result = Dns_record.del_dns_record(domain_id, record_id)
    return ["true", "success"]
