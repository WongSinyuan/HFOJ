# 1029.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-10-16 8:53
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1029
url: http://www.hfoj.net/problem/1029
"""

a, b = [int(i) for i in input().split()]

if len(str(a)) % 2 == 0 and len(str(a)) != 2:
    a = 10 ** len(str(a)) + 1

if 11 <= b <= 99:
    b = 11
elif len(str(b)) % 2 == 0:
    b = 10 ** (len(str(b)) - 1) - 1
    if 11 <= b <= 100:
        b = 11


def if_su(num):
    for i in range(2, int(num ** 0.5 + 1)):
        if num % i == 0:
            return False
    return True


for long in range(len(str(a)), len(str(b)) + 1):
    if long == 1:
        for i in [5, 7]:
            if a <= i <= b:
                print(i)
    elif long % 2 != 0:
        for j in range(int(10 ** ((long - 1) // 2)), int(10 ** ((long - 1) // 2 + 1))):
            n = int(str(j) + str(j)[(long - 3) // 2:: -1])
            if a <= n <= b:
                if if_su(n):
                    print(n)
            elif n >= b:
                break
    elif long == 2 and a <= 11 <= b:
        print(11)
