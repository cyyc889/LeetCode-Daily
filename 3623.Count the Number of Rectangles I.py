from typing import List
from collections import Counter

MOD = 10**9 + 7

class Solution:
    def countTrapezoids(self, points: List[List[int]]) -> int:
        # 1. 按 y 分组计数
        cnt_y = Counter()
        for x, y in points:
            cnt_y[y] += 1

        # 2. 计算每条水平线上的线段数 C(c, 2)
        seg_counts = []
        for c in cnt_y.values():
            if c >= 2:
                seg_counts.append(c * (c - 1) // 2)

        # 不足两条水平线，必然无法形成梯形
        if len(seg_counts) < 2:
            return 0

        # 3. 使用前缀和计算 sum_{i<j} seg[i] * seg[j]
        ans = 0
        prefix = 0
        for p in seg_counts:
            ans = (ans + prefix * p) % MOD
            prefix = (prefix + p) % MOD

        return ans
