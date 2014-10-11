from lib.store import db_conn
import config

class User_domain(object):
    def __init__(self, id, user_id, domain_id):
        self.id = id
        self.user_id = user_id
        self.domain_id = domain_id

    @classmethod
    def get_user_domain_list_by_user_id(cls, user_id):
        sql = "select id, user_id, domain_id from user_domain where user_id=%s"
        rows = db_conn.query_all(sql, user_id)
        return rows
    
    @classmethod
    def get_user_domain_by_user_id_and_domain_id(cls, user_id, domain_id):
        sql = "select id, user_id, domain_id from user_domain where user_id=%s and domain_id=%s"
        rows = db_conn.query_all(sql, (user_id, domain_id))
        return rows
