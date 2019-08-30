#!/usr/bin/env python3

import sys

# 转换函数
def Hours(minute):
    if minute < 0:
        raise ValueError("Input number cannot be negative.")
    else:
        print("{} H, {} M".format(int(minute / 60), minute % 60))

# 异常处理及函数调用
try:
    Hours(int(sys.argv[1]))
except:
    print("Parameter Error")
