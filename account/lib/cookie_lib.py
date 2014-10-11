from flask import Flask,session,redirect,url_for,escape,request
import config

def get_token_cookie():
    token = request.cookies.get(config.SITE_COOKIE)
    return token
