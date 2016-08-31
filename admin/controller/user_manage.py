# coding : utf-8
from flask import render_template,request,json
from . import ad
import requests
from flask_paginate import Pagination
from admin.config import Conf

'''
用户管理模块:包括普通用户管理和房东的管理
'''


@ad.route("/user_manage")
def user_manage():
    page = request.args.get('page')
    if page == None:
        page = '1'

    try:
        response = requests.get(url=Conf.API_ADDRESS  + "/api/v1.0/get_all_users/" + page)
        response_data = json.loads(response.content)
        if response_data['code'] == 1:
            page = response_data['page']
            pages = response_data['pages']
            total = response_data['total']
            entities = response_data['message']

            pagination = Pagination(page=page, total=total, pages=pages)
            return render_template("user/user_manage.html", pagination=pagination, entities=entities)

    except Exception as e:
        return render_template("user/user_manage.html")
    return render_template("user/user_manage.html")

@ad.route("/hs_manage")
def hs_manage():
    return render_template("user/hs_manage.html")

