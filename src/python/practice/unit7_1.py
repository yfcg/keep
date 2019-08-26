# !/usr/bin/env python
# encoding:utf-8

import wordcloud
import jieba


f = open('/Users/huangjianqiang/Desktop/gov_reprot.txt', 'r')
rpt = f.read()
f.close()

ls = jieba.lcut(rpt)

txt = " ".join(ls)

wc = wordcloud.WordCloud(scale=4,font_path="/System/Library/fonts/PingFang.ttc",width=600,height=400,background_color="white",max_words=20)

wc.generate(txt)

wc.to_file("/Users/huangjianqiang/Desktop/wcimage.jpg")
