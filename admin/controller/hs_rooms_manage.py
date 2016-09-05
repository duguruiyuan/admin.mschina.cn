# coding : utf-8
from flask import render_template,request,json,jsonify
from . import ad
import requests
from flask_paginate import Pagination
from admin.config import Conf
import hashlib


@ad.route("/hs_type_manage")
def hs_type_manage():
    page = request.args.get('page')
    if page == None:
        page = '1'
    try:
        response = requests.get(url=Conf.API_ADDRESS + "/api/v1.0/get_all_hs_type/" + page)
        response_data = json.loads(response.content)
        if response_data['code'] == 1:
            page = response_data['page']
            pages = response_data['pages']
            total = response_data['total']
            entities = response_data['message']

            pagination = Pagination(page=page, total=total, pages=pages)
            return render_template("hs_rooms/hs_type_manage.html", pagination=pagination, entities=entities)

    except Exception as e:
        return render_template("hs_rooms/hs_type_manage.html")

@ad.route("/houses_manage")
def houses_manage():
    page = request.args.get('page')
    if page == None:
        page = '1'
    try:
        response = requests.get(url=Conf.API_ADDRESS + "/api/v1.0/get_all_houses/" + page)
        response_data = json.loads(response.content)
        if response_data['code'] == 1:
            page = response_data['page']
            pages = response_data['pages']
            total = response_data['total']
            entities = response_data['message']

            pagination = Pagination(page=page, total=total, pages=pages)
            return render_template("hs_rooms/houses_manage.html", pagination=pagination, entities=entities)

    except Exception as e:
        return render_template("hs_rooms/houses_manage.html")


