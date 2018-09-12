#设置字符集 coding:utf8
from . import home

@home.route("/")
def index():
    return "<h1>home page</h1>"