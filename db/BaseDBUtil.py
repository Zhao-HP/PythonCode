#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import pymysql


class BaseDBUtil(object):
    def __init__(self, host, username, password, db, port=3306, charset='utf8'):
        # 获得数据库连接
        self.connect = pymysql.connect(
            host=host,
            port=port,
            user=username,
            passwd=password,
            db=db,
            charset=charset,
            cursorclass=pymysql.cursors.DictCursor
        )
        self.connect.autocommit(True)
        self.cursor = self.connect.cursor()

    # 执行查询语句
    def executeSelectSql(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchall()

    # 执行查询一条记录的语句
    def executeSelectOneSql(self, sql, args=None):
        self.cursor.execute(sql, args)
        return self.cursor.fetchone()

    # 执行改删增SQL
    def executeOtherSql(self, sql, **args):
        self.cursor.execute(sql, **args)
