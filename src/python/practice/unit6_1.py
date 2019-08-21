# /usr/bin/env python
# encoding:utf-8
'''
@theme:集合类型及操作
@author:huangjianqiang
@created:2019-08-21
@dec:集合是多个元素的无序组合；每个元素唯一，不存在相同元素；集合元素不可更改，不能是可变数据类型
1、集合用大括号 {} 表示，元素间用逗号分隔
2、建立集合类型用 {} 或 set()方法
3、建立空集合必须且只能使用set()方法，因为{}默认是字典类型，是创建空字典的方法
'''

A = {"python", 100, "A"}
B = {"python", 300, "B"}
print "集合间操作"

# 集合间操作1    并差交补 | - & ^
C = A|B
D = A-B
E = A&B
F = A^B
# 集合间操作2    S<=T 或 S<T 判断集合S和T的子集关系;S>=T 或 S>T 判断集合S和T的包含关系
print A > B

for item in F:
    print item

print "集合处理方法"
# 集合处理方法
ls = ["python","java","python","C","Python"]
s = set(ls)
ls = list(s)
for l in ls:
    print l
