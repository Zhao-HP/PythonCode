#! /usr/bin/env python
# -*- coding: UTF-8 -*-
import logging.handlers
import logging
import os
import sys

logFormatStr = '[%(asctime)s]-[%(levelname)s]-[%(filename)s]-[line:%(lineno)d]: %(message)s'
logDateFmtStr = '%Y-%m-%d %H:%M:%S'

logging.basicConfig(
    level=logging.INFO,
    format=logFormatStr,
    datefmt=logDateFmtStr
)


def debug(msg, *args, **kwargs):
    logging.debug(msg, *args, **kwargs)


def info(msg, *args, **kwargs):
    logging.info(msg, *args, **kwargs)


def error(msg, *args, **kwargs):
    logging.error(msg, *args, **kwargs)


class LogUtil(object):
    def __init__(self, name="All"):
        # 初始化logger
        self.log = logging.getLogger(name)
        # 设置日志文件保存路径，common同级目录中的logs文件夹
        self.logPath = os.path.abspath(os.path.join(os.getcwd(), "logs"))
        if not os.path.exists(self.logPath):
            os.makedirs(self.logPath)
        # 日志文件的绝对路径
        self.logName = os.path.join(self.logPath, 'app.log')
        # print(f"日志保存路径{logPath}")
        # 设置日志文件容量，转换为字节
        self.logSize = 1024 * 1024 * int(8)  # 8M
        # 设置日志文件保存个数
        self.logNum = int(3)
        # 日志格式，可以根据需要设置
        self.fmt = logging.Formatter(logFormatStr)

        # 日志输出到文件，设置日志名称，大小，保存个数,编码
        self.handle1 = logging.handlers.RotatingFileHandler(self.logName, maxBytes=self.logSize,
                                                            backupCount=self.logNum, encoding='utf-8')
        self.handle1.setFormatter(self.fmt)
        self.log.addHandler(self.handle1)

        # 日志输出到屏幕，便于实时观察
        self.handle2 = logging.StreamHandler(stream=sys.stdout)
        self.handle2.setFormatter(self.fmt)
        self.log.addHandler(self.handle2)

        # 设置日志等级，这里设置为INFO，表示只有INFO级别及以上的会打印
        self.log.setLevel(logging.INFO)

    # 日志接口，可根据需要定义更多接口
    def info(self, msg, *args, **kwargs):
        self.log.info(msg, *args, **kwargs)
        return

    def warning(self, msg):
        self.log.warning(msg)
        return

    def error(self, msg):
        self.log.error(msg)
        return

    def debug(self, msg):
        self.log.debug(msg)
        return
