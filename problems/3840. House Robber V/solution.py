class Solution:
    def rob(self, nums: List[int], colors: List[int]) -> int:
        n_houses = len(nums)
        
        previous1 = nums[0]
        previous2 = 0
        for i in range(1, n_houses):
            if colors[i] == colors[i-1]:
                choice = nums[i] + previous2
            else:
                choice = nums[i] + previous1
            current = max(previous1, choice)
            previous2 = previous1
            previous1 = current
        return previous1



# 1 1 1 1 1 1 1
# 0 0 x 0 0
# x 0 x 0