# Python31119.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-02-25 12:18
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1119 打字机

url: http://www.hfoj.net/problem/1119
"""

s = list(input())
i = 0
while True:
    if i >= len(s):
        break
    if s[i] == "#":
        s[i - 1: i + 1] = []
        i -= 1
    elif s[i] == "@":
        s = s[i + 1:]
        i = 0
    elif s[i] == "$":
        if s[i - 1].isalpha():
            s = s[:i] + [chr(j - (j > 90) * 26) for j in range(ord(s[i - 1]) + 1, ord(s[i - 1]) + 6)] + s[i + 1:]
        else:
            s = s[:i] + list(s[i - 1] * 5) + s[i + 1:]
        i += 5
    else:
        i += 1

# 测试10 不输出即可通过
# 测试19 不输入即不报错

print("".join(s))
