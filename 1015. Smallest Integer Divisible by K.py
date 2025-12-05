# 解题且不超时的核心思想是设置特判，且循环变量为长度且范围不超过k
# 一轮循环恰好为 *10 则一轮循环中已包含所有余数
class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k == 1: return 1
        if k % 2 == 0 or k % 5 == 0: return -1
        remain = 0
        # 注意从1开始
        for length in range(1, k + 1):
            remain = (remain * 10 + 1) % k
            if remain == 0:
                return length
        return -1
