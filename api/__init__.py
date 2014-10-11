#-*- coding:utf-8 -*-
from flask import Blueprint

blue_print = Blueprint("api",__name__,template_folder="templates",static_folder="static")
from flask import request,g,render_template,url_for,redirect,abort
from .view import dns_api

@blue_print.route("/")
def root_index():
    return redirect("/")

@blue_print.before_request
def before_request():
        print '---in blue_print api'
