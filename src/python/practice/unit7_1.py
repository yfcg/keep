# !/usr/bin/env python
# encoding:utf-8

import time

f = open('/Users/huangjianqiang/Desktop/file_test.txt', 'w')
f.write("中国是一个伟大的国家！")
# f.seek(2)
i = 1
while i < 31:
    time.sleep(1)
    print "休眠{}秒".format(i)
    i += 1
