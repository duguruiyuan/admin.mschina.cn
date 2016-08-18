# coding : utf-8
from flask import render_template
from . import ad
import json

@ad.route("/test")
def test():
    user = { 'nickname': 'Miguel' } # fake user
    posts = [ # fake array of posts
        {
            'author': { 'nickname': 'John' },
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': { 'nickname': 'Susan' },
            'body': 'The Avengers movie was so cool!'
        }
    ]

    posts_all=[{'ho_id': 1, 'ty_id': 1, 'hs_province': '河南', 'hs_city': '濮阳', 'hs_id': 1, 'hs_images': None, 'hs_address': '莽劳而无功枯', 'hs_country': '濮阳', 'hs_hitvalume': '0'}, {'ho_id': 1, 'ty_id': 1, 'hs_province': '浙江', 'hs_city': '杭州', 'hs_id': 2, 'hs_images': 'http://img1.zzkcdn.com/rr177bea245c40fcf79732ce1b1fe4c1/2000x1500.jpg-homepic800x600.jpg', 'hs_address': 'xxxxx', 'hs_country': '存在', 'hs_hitvalume': '0'}, {'ho_id': 1, 'ty_id': 4, 'hs_province': '浙江', 'hs_city': '杭州', 'hs_id': 3, 'hs_images': 'http://img1.zzkcdn.com/rr177bea245c40fcf79732ce1b1fe4c1/2000x1500.jpg-homepic800x600.jpg', 'hs_address': 'xxxxx', 'hs_country': '存在', 'hs_hitvalume': '0'}]
    print(type(posts))
    return render_template("test.html",
        title = 'Home',
        user = user,
        posts = posts_all)

@ad.route("/test1")
def test1():
    lists = [{'ho_id': 1, 'ty_id': 1, 'hs_province': '河南', 'hs_city': '濮阳', 'hs_id': 1, 'hs_images': None, 'hs_address': '莽劳而无功枯', 'hs_country': '濮阳', 'hs_hitvalume': '0'}, {'ho_id': 1, 'ty_id': 1, 'hs_province': '浙江', 'hs_city': '杭州', 'hs_id': 2, 'hs_images': 'http://img1.zzkcdn.com/rr177bea245c40fcf79732ce1b1fe4c1/2000x1500.jpg-homepic800x600.jpg', 'hs_address': 'xxxxx', 'hs_country': '存在', 'hs_hitvalume': '0'}, {'ho_id': 1, 'ty_id': 4, 'hs_province': '浙江', 'hs_city': '杭州', 'hs_id': 3, 'hs_images': 'http://img1.zzkcdn.com/rr177bea245c40fcf79732ce1b1fe4c1/2000x1500.jpg-homepic800x600.jpg', 'hs_address': 'xxxxx', 'hs_country': '存在', 'hs_hitvalume': '0'}]
    print(type(lists))
    print(lists)
    json_str = json.dumps(lists)
    print(type(json_str))
    print(json_str)
    json_data =json.loads(json_str)
    print(type(json_data))
    print(json_data)
    return "hello test1"
    # current_user = session.get('current_user', 'not set')  # json
    # # tmp = HouseOwner.json_to_houseowner(current_user)
    # return render_template('test.html', current_user=current_user['ho_account'])