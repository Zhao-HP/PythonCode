#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import json
import datetime


class DateEncoder(json.JSONEncoder):
    """
    解决dict 转json 时 datetime 转换失败
    使用方法：json.dumps(data, cls=DateEncoder)
    """

    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)
