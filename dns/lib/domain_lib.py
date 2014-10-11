from dns.model.domain import Domain
from dns.model.user_domain import User_domain

def get_all_domain_dict_lib():
    tmp_list = []
    domain_list = Domain.get_all_domain()
    for domain in domain_list:
        tmp_dict = {}
        tmp_dict['domain_id'] = domain[0]
        tmp_dict['domain_name'] = domain[1]
        tmp_dict['type'] = domain[2]
        tmp_list.append(tmp_dict)
    return tmp_list

def if_user_id_have_domain_rights(user_id, domain_id):
    result = User_domain.get_user_domain_by_user_id_and_domain_id(user_id, domain_id)
    if len(result) == 1:
        return True
    else:
        return False
