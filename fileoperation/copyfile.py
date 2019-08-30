#!/usr/bin/env python3
import sys

# 如果输入的格式错误，会输出异常并提示正确的输入
if len(sys.argv) < 3:
    print("Wrong parameter.")
    print("./copyfile.py file1 file2")
    sys.exit(1)

f1 = open(sys.argv[1])
s = f1.read()
f1.close()
f2 = open(sys.argv[2], 'w')
f2.write(s)
f2.close()
