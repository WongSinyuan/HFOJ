# Python31116.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-02-24 22:54
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1116 洗盘子

url: http://www.hfoj.net/problem/1116
"""

from queue import LifoQueue

dirty = LifoQueue()
washed = LifoQueue()
clean = LifoQueue()

N = int(input())
for i in range(N, 0, -1):
    dirty.put(i)

while True:
    m, n = list(map(int, input().split()))
    if m == 1:
        for _ in range(n):
            washed.put(dirty.get())
    else:
        for _ in range(n):
            clean.put(washed.get())
    if dirty.empty() and washed.empty():
        break

for j in range(N):
    print(clean.get())
