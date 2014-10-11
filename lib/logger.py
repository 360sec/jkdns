import os, time
import config

class Logger(object):
    def __init__():
        print "in log"

    @classmethod
    def warning_log(cls, message):
        ISOTIMEFORMAT='%Y-%m-%d %X'
        now=time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
        try:
            log_file = config.LOG_DIR+"/warning.log"
            file_object = open(log_file, 'a+')
            file_object.write(now + " " + str(essage) + "\n")
            file_object.close()
        except Exception, e:
            print e
            return False
        return True
    
    @classmethod
    def action_log(cls, message):
        ISOTIMEFORMAT='%Y-%m-%d %X'
        now=time.strftime(ISOTIMEFORMAT, time.localtime(time.time()))
        try:
            log_file = config.LOG_DIR+"/action.log"
            file_object = open(log_file, 'a+')
            file_object.write(now + " " + str(message) + "\n")
            file_object.close()
        except Exception, e:
            print e
            return False
        return True
