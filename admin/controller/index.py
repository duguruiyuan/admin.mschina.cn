# coding : utf-8
from flask import render_template,request
from . import ad



@ad.route("/index")
def index():
    return render_template("index.html")