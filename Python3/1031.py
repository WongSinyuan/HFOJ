# 1031.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 23:23
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1031 石头剪刀布

url: http://www.hfoj.net/problem/1031
"""

c, p = list(map(str.lower, input().split()))
win, lose = "You win", "You lose"
if c == p:
    print("Draw")
else:
    if c == "r":
        if p == "p":
            print(win)
        else:
            print(lose)
    elif c == "p":
        if p == "s":
            print(win)
        else:
            print(lose)
    else:
        if p == "r":
            print(win)
        else:
            print(lose)
