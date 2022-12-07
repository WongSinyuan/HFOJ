# 1052.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 17:18
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1052 阶乘的和

url: http://www.hfoj.net/problem/1052
"""

# 这题的输入样例和输出样例明显弄反了，很可能评分器也有问题。不知道以前那些人是怎样做对的
# 也许我的代码也有问题，请大佬指教
num = 1
re = 0
for i in range(1, int(input()) + 1):  # 运用迭代，大幅缩短时间
    num *= i  # n! = n * (n - 1)!
    re += num
print(re)
