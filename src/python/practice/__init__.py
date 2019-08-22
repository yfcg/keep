#!/usr/bin/env python
# encoding:utf-8
import sys
import json

datadict = {"city": "", "country": "中国", "groupid": 0,
             "headimgurl": "http://thirdwx.qlogo.cn/mmopen/IGDmSicwOvQ3mXpm1lkSbOQRRAfdIxibQFNMoeHTHEVXzBO6DPibDZN8ibbVgCZz5R2BAsecNhqvicTWIN7xP3o1JBHBxBn1eOeGy/132",
             "language": "zh_CN", "nickname": "思怡💋", "openid": "oe3h80nsXfwBi5WcwXSdCFtCVXkA", "province": "重庆",
             "remark": "", "sex": 2, "subscribe": 1, "subscribe_time": 1522822271,
             "unionid": "oITCTv6NlWf03McBVienBQSQoOsQ"}
print json.dumps(datadict, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))
print "黄建强在Temp上的更改"
print "\n{0:=^111}\n".format("分割线")
