#!/usr/bin/env python
#-*- coding:utf-8 -*-
import os

from flask import Flask, g, redirect, url_for, request, session, render_template

app = Flask(__name__)
app.config.from_object("config")

from account import blue_print as account_bp
from api import blue_print as api_bp
from manage import blue_print as manage_bp

app.register_blueprint(account_bp,url_prefix="/account")
app.register_blueprint(api_bp,url_prefix="/api")
app.register_blueprint(manage_bp,url_prefix="/manage")

@app.route("/sso")
def sso():
    return render_template("sso.html")

@app.route("/")
def main_index():
    return redirect(url_for("manage.domain_list"))

if __name__ == "__main__":
    app.debug = True
    app.run(host="0.0.0.0", port=80);
