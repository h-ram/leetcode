class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        mins = sorted(nums)[:3]
     
        if nums[0] in mins:
            return sum(mins)
        else:
            return sum(mins[:2]) + nums[0]