# 1029.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-10-16 8:53
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1029 回文质数

url: http://www.hfoj.net/problem/1029
"""


def if_su(num) -> bool:
    """
    判断是否为素数
    :param num: 数
    :return: 是否为质数
    """
    for k in range(2, int(num ** 0.5 + 1)):
        if num % k == 0:
            return False
    return True


a, b = list(map(int, input().split()))

if len(str(a)) % 2 == 0 and len(str(a)) != 2:  # 对构造范围进行简化
    a = 10 ** len(str(a)) + 1
if 11 <= b <= 99:
    b = 11
elif len(str(b)) % 2 == 0:
    b = 10 ** (len(str(b)) - 1) - 1
    if 11 <= b <= 100:
        b = 11

for long in range(len(str(a)), len(str(b)) + 1):  # 按位数构造回文数
    if long == 1:
        for i in [5, 7]:
            if a <= i <= b:
                print(i)
    elif long % 2 != 0:  # 偶数位数的回文数都不是质数（11除外）
        for j in range(int(10 ** ((long - 1) // 2)), int(10 ** ((long - 1) // 2 + 1))):
            n = int(str(j) + str(j)[(long - 3) // 2:: -1])
            if a <= n <= b:
                if if_su(n):
                    print(n)
            elif n >= b:
                break
    elif long == 2 and a <= 11 <= b:  # 11为回文质数
        print(11)
