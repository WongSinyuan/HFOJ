# 1083.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 19:31
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1083 表达式求值

url: http://www.hfoj.net/problem/1083
"""

re = 0
for i in input().split("+"):
    if "*" in i:
        j, k = i.split("*")
        re += int(j) * int(k)
    else:
        re += int(i)

print(re % 10000)  # 不知为何一直报错
