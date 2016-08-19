# coding:utf-8
from flask import Blueprint

ad = Blueprint('ad', __name__)

from . import login
from . import index
from . import test

