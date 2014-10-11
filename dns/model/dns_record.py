from lib.store import db_conn
import config

class Dns_record(object):
    def __init__(self, id, domain_id, record, ttl, type, value, create_time, state, line):
        self.id = id
        self.domain_id = domain_id

    @classmethod
    def get_dns_record_list_by_domain_id(cls, domain_id):
        sql = "select id, domain_id, record, ttl, type, value, create_time, state from dns_record where domain_id=%s"
        rows = db_conn.query_all(sql, domain_id)
        return rows

    @classmethod
    def get_dns_record_list_by_domain_id_and_record(cls, domain_id, record):
        sql = "select id, domain_id, record, ttl, type, value, create_time, state from dns_record where domain_id=%s and record=%s"
        rows = db_conn.query_all(sql, (domain_id, record))
        return rows

    @classmethod
    def update_dns_record(cls, domain_id, record_id, record, ttl, type, value, line):
        sql = "update dns_record set record=%s, ttl=%s, type=%s, value=%s, line=%s where domain_id=%s and id=%s"
        rows = db_conn.insert(sql, (record, ttl, type, value, line, domain_id, record_id))
        return True

    @classmethod
    def add_dns_record(cls, domain_id, record, ttl, type, value, line):
        sql = "insert into dns_record (domain_id, record, ttl, type, value, create_time, state, line) values (%s, %s, %s, %s, %s, now(), '1', %s)"
        rows = db_conn.insert(sql, (domain_id, record, ttl, type, value, line))
        sql = "select max(id) from dns_record"
        rows = db_conn.query_all(sql)
        return rows[0][0]

    @classmethod
    def del_dns_record(cls, domain_id, record_id):
        sql = "delete from dns_record where domain_id=%s and id=%s"
        rows = db_conn.query_all(sql, (domain_id, record_id))
        return True

    @classmethod
    def change_dns_record_state(cls, domain_id, record_id, state):
        sql = "update dns_record set state=%s where domain_id=%s and id=%s"
        rows = db_conn.query_all(sql, (state, domain_id, record_id))
        return True

    @classmethod
    def type_a_count(cls, domain_id, record, value):
        sql = "select count(*) from dns_record where domain_id=%s and record=%s and value=%s and type='A'"
        rows = db_conn.query_all(sql, (domain_id, record, value))
        return rows[0][0]

    @classmethod
    def type_a_all_count(cls, domain_id, record):
        sql = "select count(*) from dns_record where domain_id=%s and record=%s and type='A'"
        rows = db_conn.query_all(sql, (domain_id, record))
        return rows[0][0]

    @classmethod
    def type_cname_all_count(cls, domain_id, record):
        sql = "select count(*) from dns_record where domain_id=%s and record=%s and type='CNAME'"
        rows = db_conn.query_all(sql, (domain_id, record))
        return rows[0][0]

    @classmethod
    def type_cname_count(cls, domain_id, record, value):
        sql = "select count(*) from dns_record where domain_id=%s and record=%s and value=%s and type='CNAME'"
        rows = db_conn.query_all(sql, (domain_id, record, value))
        return rows[0][0]
