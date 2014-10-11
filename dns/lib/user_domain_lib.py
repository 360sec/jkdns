from dns.model.user_domain import User_domain
from dns.model.domain import Domain

def get_domain_list_by_user_id(user_id):
    tmp_list = []
    user_domain_list = User_domain.get_user_domain_list_by_user_id(user_id)
    for user_domain in user_domain_list:
        try:
            tmp_dict = {}
            domain = Domain.get_domain_by_domain_id(user_domain[2])
            tmp_dict['domain_id'] = domain[0]
            tmp_dict['domain_name'] = domain[1]
            tmp_dict['type'] = domain[2]
            tmp_list.append(tmp_dict)
        except:
            print "error"
    return tmp_list
