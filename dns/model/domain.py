from lib.store import db_conn
import config

class Domain(object):
    def __init__(self, domain_id, domain_name, type):
        self.domain_id = domain_id
        self.domain_name = domain_name
        self.domain_type = domain_type

    @classmethod
    def test_if_domain_name_exists(cls, domain_name):
        sql = "select count(domain_id) from domain where domain_name=%s"
        rows = db_conn.query_all(sql, domain_name)
        if rows[0][0] == 1:
            return True
        else:
            return False
 
    @classmethod
    def test_if_domain_id_exists(cls, domain_id):
        sql = "select count(domain_id) from domain where domain_id=%s"
        rows = db_conn.query_all(sql, domain_id)
        if rows[0][0] == 1:
            return True
        else:
            return False
       
    @classmethod
    def get_domain_id_by_domain_name(cls, domain_name):
        sql = "select domain_id from domain where domain_name=%s"
        rows = db_conn.query_all(sql, domain_name)
        if len(rows) == 1:
            return rows[0][0]
        else:
            return False
 
    @classmethod
    def get_domain_by_domain_id(cls, domain_id):
        sql = "select domain_id, domain_name, type from domain where domain_id=%s"
        rows = db_conn.query_all(sql, domain_id)
        if len(rows) == 1:
            return rows[0]
        else:
            return False

    @classmethod
    def get_domain_by_domain_name(cls, domain_name):
        sql = "select domain_id, domain_name, type from domain where domain_name=%s"
        rows = db_conn.query_all(sql, domain_name)
        if len(rows) == 1:
            return rows[0]
        else:
            return False
       
    @classmethod
    def get_all_domain(cls):
        sql = "select domain_id, domain_name, type from domain order by domain_name"
        rows = db_conn.query_all(sql)
        return rows
