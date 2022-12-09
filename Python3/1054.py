# 1054.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 18:50
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1054 完全数

url: http://www.hfoj.net/problem/1054
"""

m, n = list(map(int, input().split()))

for i in range(m, n + 1):
    if i == 1:  # 排除1
        continue
    nums = []
    for j in range(1, int(i ** 0.5 + 1)):
        if i % j == 0:
            nums.append(j)
            if j != 1 and j != i ** 0.5:  # 因数是成对出现的，只需遍历一半就好了
                nums.append(i // j)

    if sum(nums) == i:
        print(i)
