#! /usr/bin/env python
# coding=utf-8
import json
from util.Encoder import DateEncoder


# class转化为JSON串
def classToJson(Object):
    return dictToJson(Object.__dict__)


# 将字典转成JSON串
def dictToJson(dict):
    return json.dumps(dict, cls=DateEncoder, sort_keys=True,
                      indent=4, ensure_ascii=False)
