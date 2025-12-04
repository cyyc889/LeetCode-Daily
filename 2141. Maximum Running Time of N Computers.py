# 解题的核心思想是找到以平均时间为边界的短板效应
class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        batteries.sort(reverse = True)
        s = sum(batteries)
        for b in batteries:
            if b <= s//n:
                return s // n
            s -= b
            n -= 1
