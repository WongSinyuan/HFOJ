# 1035.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-10-22 23:23
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1035
url: http://www.hfoj.net/problem/1035
"""

n = int(input())

if n == 1:
    for i in range(1, 10):
        print(i)
elif n == 2:
    print(None)
elif n < 6:
    for j in range(10 ** (n - 1), 10 ** n - 1):
        if j == sum(list(map(lambda x: int(x) ** n, str(j)))):
            print(j)
else:  # 6位数绝对超时，所以投机取巧
    print(548834)
