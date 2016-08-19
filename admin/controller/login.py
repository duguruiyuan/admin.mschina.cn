# coding : utf-8
from flask import render_template,request
from . import ad




@ad.route("/login")
def login():
    return render_template("login.html")

@ad.route("/do_login",methods=['POST'])
def do_login():
    name = request.form.get('username')
    password = request.form.get('password')
    if name=='json' and password=='123':   # 测试
        return render_template("index.html")
    return "hello world"
