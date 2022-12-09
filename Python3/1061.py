# 1061.py
# -*- encoding: utf-8 -*-
# @Author: Wong Sinyuan
# @Contact: 1404951910@qq.com
# @Datetime: 2022-12-07 19:24
# @Software: PyCharm
# @Project: HFOJ
# @GitHub: https://github.com/WongSinyuan/HFOJ

"""
HFOJ #1061 商品排序

url: http://www.hfoj.net/problem/1061
"""

print(  # 搁着盖房子呢
    "\n".join(
        map(
            str,
            sorted(
                list(
                    map(
                        lambda _: int(
                            input()
                        ),
                        range(
                            int(
                                input()
                            )
                        )
                    )
                )
            )
        )
    )
)
