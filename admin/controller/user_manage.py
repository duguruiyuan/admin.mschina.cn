# coding : utf-8
from flask import render_template,request
from . import ad

'''
用户管理模块:包括普通用户管理和房东的管理
'''


@ad.route("/user_manage")
def user_manage():
    return render_template("user/user_manage.html")

@ad.route("/hs_manage")
def hs_manage():
    return render_template("user/hs_manage.html")

