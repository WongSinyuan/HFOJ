# 1027.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 18:35
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1027 榕榕计算邮资

url: http://www.hfoj.net/problem/1027
"""
g, t = input().split()
print(8 + (0 if int(g) <= 1000 else 4 * ((int(g) - 1001) // 500 + 1)) + (0 if t == "n" else 5))
