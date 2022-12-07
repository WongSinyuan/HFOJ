# 1066.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-03 15:40
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1066 分身数对

url: http://www.hfoj.net/problem/1066
"""
targe = list(map(int, input().split()))[1]
nums = list(map(int, input().split()))
nums.sort()
left, right = 0, len(nums) - 1
count = 0
while left < right:
    if nums[left] + nums[right] == targe:
        count += 1
        left += 1
        right -= 1
    elif nums[left] + nums[right] > targe:
        right -= 1
    else:
        left += 1
print(count)  # 经典双指针
