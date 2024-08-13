"""

"""
from typing import List


def base_response(code, msg, data=None):
    """基础返回格式"""
    if data is None:
        data = []
    result = {
        "code": code,
        "message": msg,
        "data": data
    }
    return result


def success(data=None, msg=''):
    """response success format"""
    return base_response(200, msg, data)


def fail(code=-1, msg='', data=None):
    """response fail format"""
    return base_response(code, msg, data)