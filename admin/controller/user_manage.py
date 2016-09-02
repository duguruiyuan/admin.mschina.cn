# coding : utf-8
from flask import render_template,request,json,jsonify
from . import ad
import requests
from flask_paginate import Pagination
from admin.config import Conf
import hashlib

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

#更新用户资料
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

# 添加新用户
#user_password_hash = hashlib.md5(user_password.encode('utf-8')).hexdigest()
@ad.route("/user/insert_user",methods = ["POST"])
def insert_user():
    user_account = request.json.get("user_account")
    if not user_account:
        return jsonify({"code":0,"message":"用户名不能为空"})
    user_password = request.json.get("user_password")
    if not user_password:
        return jsonify({"code": 0, "message": "密码不能为空"})

    user_password_hash = hashlib.md5(user_password.encode('utf-8')).hexdigest()
    user_mobile = request.json.get("user_mobile")
    if not user_mobile:
        return jsonify({"code": 0, "message": "手机号不能为空"})
    user_headimg = request.json.get("user_headimg")
    user_type = request.json.get("user_type")

    data=json.dumps({
        "user_account":user_account,
        "user_password":user_password_hash,
        "user_mobile":user_mobile,
        "user_headimg":user_headimg,
        "user_type":user_type
    })
    # data = json.dumps({"user_account": user_account, "user_password": user_password_hash})
    response_data = requests.post(url=Conf.API_ADDRESS+"/api/v1.0/user_register", data = data, headers={"content-type": "application/json"})
    result_data = json.loads(response_data.content)
    #code =1 注册成功
    if result_data['code'] == 1:
        return jsonify('{"code":"1","message":"success"}')
    #code = 0 注册失败
    if response_data['code'] == 0:
        return jsonify(result_data)
    return jsonify(result_data)

@ad.route("/user/delete_user_by_id",methods = ["POST"])
def delete_user_by_id():
    user_id = request.json.get("user_id")
    if not user_id:
        return jsonify({"code": 0, "message": "参数错误"})
    response = requests.delete(Conf.API_ADDRESS + "/api/v1.0/delete_user_ById/" + str(user_id),headers={"content-type": "application/json"})
    response_data = json.loads(response.content)
    # code = 0删除失败
    if response_data["code"] == 0:
        return jsonify(response_data)

    # code = 1 删除成功
    if response_data["code"] == 1:
        return jsonify({"code": 1, "message": "删除成功"})