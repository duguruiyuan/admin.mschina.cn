# coding:utf-8
from flask import Flask
from admin.config import Conf
from admin.controller import ad as ad_blueprint
import redis


def create_app():

    app = Flask(__name__)
    app.config.from_object(Conf)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    app.config['ALLOW_FOLDER'] = True
    app.secret_key = app.config['SECRET_KEY']

    app.debug = app.config['DEBUG']

    app.session_redis = redis.Redis(host=app.config['REDIS_HOST'], port=app.config['REDIS_PORT'],
                                    db=app.config['SESSION_DB'], password=app.config['REDIS_PASSWORD'])


    # 蓝图
    app.register_blueprint(ad_blueprint)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=app.debug, host=Conf.SERVICE_HOST, port=Conf.SERVICE_PORT)