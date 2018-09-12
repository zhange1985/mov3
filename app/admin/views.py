# coding:utf8
from . import admin
from flask import render_template,redirect,url_for


@admin.route("/")
def index():
    return render_template("admin/index.html")

@admin.route("/userlist")
def userlist():
    return "userlist.html";
