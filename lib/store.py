import os ,time
import commands
import datetime

import MySQLdb
from MySQLdb import IntegrityError

import config

def init_db():
    cmd = """mysql -h%s -P%s -u%s -p%s < %s""" \
        % (config.DB_HOST, config.DB_PORT, 
            config.DB_USER, config.DB_PASSWD,
            os.path.join(os.path.dirname(__file__), "schema.sql"))
    status, output = commands.getstatusoutput(cmd)

    if status != 0:
        print "init_db fail, output is: %s" % output

    return status

def connect_db(config_):
    try:
        conn = MySQLdb.connect(
            host=config_.DB_HOST,
            port=config_.DB_PORT,
            user=config_.DB_USER,
            passwd=config_.DB_PASSWD,
            db=config_.DB_NAME,
            use_unicode=True,
            charset="utf8")
        return conn
    except Exception, e:
        print "Fatal: connect db fail:%s" % e
        return None

class DB(object):
    def __init__(self, config_):
        self.config = config_
        self._conn = connect_db(config_)

    def connect(self):
        self._conn = connect_db(self.config)
        return self._conn

    def execute(self, *a, **kw):
        cursor = kw.pop('cursor', None)
        try:
            cursor = cursor or self._conn.cursor()
            cursor.execute(*a, **kw)
        except (AttributeError, MySQLdb.OperationalError):
            self._conn and self._conn.close()
            self.connect()
            cursor = self._conn.cursor()
            cursor.execute(*a, **kw)
        return cursor
        
    def insert(self, *a, **kw):
        cursor = None
        try:
            cursor = self.execute(*a, **kw)
            id_ = cursor.lastrowid
            db_conn.commit()
            return id_
        except IntegrityError:
            db_conn.rollback()
        finally:
            cursor and cursor.close()

    def update(self, *a, **kw):
        cursor = None
        try:
            cursor = self.execute(*a, **kw)
            id_ = cursor.lastrowid
            db_conn.commit()
            ret = cursor.rowcount
            return ret
        except IntegrityError:
            db_conn.rollback()
        finally:
            cursor and cursor.close()

    def delete(self, *a, **kw):
        cursor = None
        try:
            cursor = self.execute(*a, **kw)
            id_ = cursor.lastrowid
            db_conn.commit()
            ret = cursor.rowcount
            return ret
        except IntegrityError:
            db_conn.rollback()
        finally:
            cursor and cursor.close()

    def query_all(self, *a, **kw):
        cursor = None
        ret = None
        try:
            cursor = self.execute(*a, **kw)
            ret = cursor.fetchall()
            self._conn.commit()
        except IntegrityError:
            pass
        finally:
            cursor and cursor.close()
        return ret
    
    def query_many(self, num, *a, **kw):
        cursor = None
        ret = None
        try:
            cursor = self.execute(*a, **kw)
            ret = cursor.fetch_many(num)
        except MySQLdb.Error, e:
            pass
        finally:
            cursor and cursor.close()
            return ret

    def commit(self):
        if self._conn:
            try:
                self._conn.commit()
            except MySQLdb.OperationalError:
                self._conn and self._conn.close()
                self.connect()
                self._conn and self._conn.commit()

    def rollback(self):
        if self._conn:
            try:
                self._conn.rollback()
            except MySQLdb.OperationalError:
                self._conn and self._conn.close()
                self.connect()
                self._conn and self._conn.rollback()

db_conn = DB(config)
