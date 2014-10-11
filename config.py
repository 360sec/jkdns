#-*- coding:utf-8 -*-

#-- app config --
#DEBUG = True
DEBUG = False
INDEXPAGE = "/manage/"
SITE_COOKIE = "jkdns"
SSO_WEBSITE = "https://sso.example.com"
SSO_TOKEN = "jkdns_sso_token"
SESSION_COOKIE_NAME = "xop"
SECRET_KEY = "jkdns_secret_key"
LOG_DIR = "/home/jkdns/log/"
SESSION_LIFETIME_DAY = 15
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 15

#RUN_METHOD = "sso"
RUN_METHOD = "local_auth"

LOCAL_WEBSITE = "http://jkdns.example.com"
MAIL_FROM = "dns@idcmail.example.com"

#-- local db config --
DB_HOST = "localhost"
DB_PORT = 3310
DB_USER = "jkdns"
DB_PASSWD = "example"
DB_NAME = "jkdns"

#-- dnspod config --
DNSPOD_URL = "https://dnsapi.cn"
DNSPOD_USER = "example@example.cn"
DNSPOD_PW = "example$"

#-- local_bind config --
LOCAL_BIND_LINE = ['default']
