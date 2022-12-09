# 1104.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-08 22:31
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1104 生日相同问题

url: http://www.hfoj.net/problem/1104
"""
bir = {}

for _ in range(int(input())):
    name, m, d = input().split()
    if bir.get(m + " " + d):
        bir[m + " " + d].append(name)
    else:
        bir[m + " " + d] = [name]

if any(map(lambda x: len(x) > 1, bir.values())):
    for date in sorted(bir.keys(),
                       key=lambda x: int(x.split()[0]) * 12 + int(x.split()[1])):
        names = sorted(bir[date],
                       key=lambda x: (len(x),
                                      sum(list(map(lambda i, a:
                                                   (list(map(chr, range(97, 123))).index(i) + 1) * (26 ** a),
                                                   x.lower(),
                                                   range(len(x) - 1, -1, -1))))))
        if len(names) > 1:
            print(date, " ".join(names))  # 又不知道为什么答案错误
else:
    print(None)
