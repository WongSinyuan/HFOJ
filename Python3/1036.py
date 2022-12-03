# 1036.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-09-17 18:23
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1036
url: http://www.hfoj.net/problem/1036
"""

letters = "abcdefghijklmnopqrstuvwxyz"
nums = [letters.index(s) for s in input()]
nums_ = nums.copy()


def find_last_min(l: list, index_=0) -> int:
    if not l:
        return 0
    min_num = min(l)
    index = 0
    while l.count(min_num) > 1 or l.index(min_num) == 0:
        l.remove(min_num)
        index += 1
        if l.count(min_num) == 0:
            return find_last_min(l, index_=index)
    return index + l.index(min_num) + index_


def find_second_min(l: list):
    for i in range(len(l)):
        if l[i] > l[find_last_min(l.copy())]:
            return i
    return -1


index1 = find_last_min(nums.copy())
index2 = find_second_min(nums.copy())

if index1 != 0 and index2 != -1:
    nums.pop(index1)
    nums.pop(index2)
    nums.insert(index1, nums_[index2])
    nums.insert(index2, nums_[index1])

print("".join([letters[i] for i in nums]))
