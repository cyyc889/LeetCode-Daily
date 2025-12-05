# 解题的核心思想为数组和与数组差奇偶性相同
class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        return (sum(nums) % 2 == 0) * (len(nums) - 1)
