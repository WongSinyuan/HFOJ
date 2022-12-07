# 1030.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 18:49
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1030 优惠购物

url: http://www.hfoj.net/problem/1030
"""

s, m = input().split()  # 虽然题目是两行输入，但是实践证明，实际是一行，我会向老师反映此情况。
m = int(m)
if s == "V":
    print("{}\n{:.2f}".format(*[[["YES", m * 0.75], ["NO", m * 0.8]][m <= 1000], ["NO", m * 0.85]][m <= 500]))
else:
    print("{}\n{:.2f}".format(*[["YES", m * 0.9], ["NO", m * 0.9]][m <= 500]))
