# 1025.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 18:26
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1025 🧑‍⚖️裁判

url: http://www.hfoj.net/problem/1025
"""

s = input()
print("%.3f" % (sum(sorted(list(map(int, s.split())))[1:]) / 2))
print("%.3f" % (sum(sorted(list(map(int, s.replace("8", "3").replace("9", "6").split())))[1:]) / 2))
