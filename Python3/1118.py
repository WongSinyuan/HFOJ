# Python31118.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2023-02-24 23:41
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1118 溶液模拟器

url: http://www.hfoj.net/problem/1118
"""

var = [
    [
        [
            [
                [Cv.append,
                 [lambda _: 0, Cv.pop][len(Cv) > 1]][f[0] == "Z"](
                    -1 if f[0] == "Z" else
                    list(
                        map(
                            lambda Cv0, CvI: (
                                int(Cv0[0] + CvI[0]),
                                float((Cv0[0] * Cv0[1] + CvI[0] * CvI[1]) / (Cv0[0] + CvI[0]))
                            ),
                            [Cv[-1]],
                            [list(map(float, f.split()[1:]))]
                        )
                    )[0]
                ) for f in [input()]
            ],
            print("%d %.5f" % Cv[-1])
        ] for _ in range(int(input()))
    ] for Cv in [
        list(
            map(
                lambda x: (int(x[0]), float(x[1])),
                [input().split()]
            )
        )
    ]
]

# 以下是正常解法
Cv = list(map(lambda x: (int(x[0]), float(x[1])), [input().split()]))
for _ in range(int(input())):
    f = input()
    if f[0] == "Z":
        if len(Cv) > 1:
            Cv.pop()
    else:
        Cv += list(
            map(
                lambda CV0, CVI: (
                    int(CV0[0] + CVI[0]),
                    (CV0[0] * CV0[1] + CVI[0] * CVI[1]) / (CV0[0] + CVI[0])
                ),
                [Cv[-1]],
                [list(map(float, f.split()[1:]))]
            )
        )
    print("%d %.5f" % Cv[-1])
