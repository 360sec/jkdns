#-*- coding:utf-8 -*-
from flask import Blueprint

blue_print = Blueprint("manage",__name__,template_folder="templates",static_folder="static")
from flask import request,g,render_template,url_for,redirect,abort
from .view import manage_base, manage_api

@blue_print.route("/")
def root_index():
    return redirect("/manage/domain_list")

@blue_print.before_request
def before_request():
        print '---in blue_print manage'
