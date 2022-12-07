# 1073.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:45
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1073 等价图像

url: http://www.hfoj.net/problem/1073
"""

print("NY"[
          list(map(
              lambda m1, m2: list(map(
                  lambda p1, p2: len(p1) == len(p2) and sum(p1[0]) == sum(p2[0]),
                  list(filter(
                      lambda x: sum(x) != 0,
                      [list(map(int, input().split())) for _ in range(m1)])),
                  list(filter(
                      lambda x: sum(x) != 0,
                      [list(map(int, input().split())) for _ in range(m2)]))))[0],
              *list(map(lambda x: [int(x)], input().split()))[::2]))[0]])
# 说实话，咱根本不愿意看这些shit
