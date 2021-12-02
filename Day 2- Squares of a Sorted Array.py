class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l = [nums[i] * nums[i] for i in range(0,len(nums))]
        m = sorted(l)
        return m
