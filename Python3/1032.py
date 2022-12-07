# 1032.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 23:30
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1032 推荐电影

url: http://www.hfoj.net/problem/1032
"""

# 这个不是题解！！但是不知道哪错了。希望大佬指导一下
m = int(input())
good = []
bad = []
common = []

for i in range(m):
    a, b, w = list(map(float, input().split()))
    s = a * w + (1 - w) * b
    if s != int(s):
        s = int(s) + 1
    if s <= 2:
        bad.append((s, str(i + 1)))
    elif s >= 8:
        good.append((s, str(i + 1)))
    else:
        common.append((s, str(i + 1)))

good.sort(reverse=True)
bad.sort()

print(" ".join([i[1] for i in good[:20]]) if good else "No movies")
print(" ".join([i[1] for i in bad[:20]]) if bad else "No movies")
print(len(common))
