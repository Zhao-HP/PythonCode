#! /usr/bin/env python
# -*- coding: UTF-8 -*-

# 将数据库字段名修改为以小驼峰命名方式
def changeFieldName(fieldName):
    s = str(fieldName).split("_")
    resultStr = s.pop()
    for i in s:
        resultStr += i.capitalize()

    return resultStr


# 将查询结果解析为传入的对象
def parseResultToDomain(result, field, Object):
    fieldDict = {}
    for i in range(len(result)):
        fieldDict[changeFieldName(field[i][0])] = result[i]

    for item in dir(Object):
        if not item.startswith('__'):
            if fieldDict.get(item) is not None:
                setattr(Object, item, fieldDict[item])

    return Object
