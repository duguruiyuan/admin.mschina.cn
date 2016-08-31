# coding : utf-8
from flask import render_template,request,json,jsonify
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

#编辑房源
@ad.route("/user/do_update_userById",methods=['POST'])
def do_update_userById():
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"code": 0, "message": "参数错误"})
    user_account = request.json.get("user_account")
    user_password = request.json.get("user_password")
    user_mobile = request.json.get("user_mobile")
    user_type = request.json.get("user_type")

    data = json.dumps({
                       "user_id": user_id,
                       "user_account": user_account,
                       "user_password": user_password,
                       "user_mobile": user_mobile,
                       "user_type": user_type
                       })
    response = requests.put(Conf.API_ADDRESS+"/api/v1.0/update_userBaseById/"+user_id,
                            data=data,
                            headers={"content-type": "application/json"})
    response_data = json.loads(response.content)
    # code = 0编辑失败
    if response_data["code"] == 0:
        return jsonify(response_data)

    # code = 1 编辑成功
    if response_data["code"] == 1:
        return jsonify({"code": 1, "message": "success"})

