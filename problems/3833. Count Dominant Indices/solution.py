class Solution:
    def dominantIndices(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        for i in range(n):
            if nums[i] > sum(nums[i:]) // (n-i):
                count += 1
        return count