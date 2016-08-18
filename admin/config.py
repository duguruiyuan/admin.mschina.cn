#   发布环境
class ProductionConfig(object):
    DEBUG = False

    SERVICE_HOST = 'admin.mschina.cn'
    SERVICE_PORT = 8090
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT/json/wang'

    REDIS_HOST = 'localhost'
    REDIS_PORT = 80

#   开发环境
class DevelopmentConfig(object):
    DEBUG = True

    SERVICE_HOST = 'admin.mschina.cn'
    SERVICE_PORT = 8090
    SECRET_KEY = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT/json/wang'

    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379
    CACHE_DB = 1
    SESSION_DB = 0
    REDIS_PASSWORD = ''

    API_ADDRESS = "http://127.0.0.1:8080"
    MYSQL_INFO = "mysql+pymysql://root:123@127.0.0.1:3306/mschina?charset=utf8"

Conf = DevelopmentConfig