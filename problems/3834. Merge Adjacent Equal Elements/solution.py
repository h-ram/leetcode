class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
    
        if len(nums) < 2:
            return nums

        result = []
        for num in nums:
            while result and result[-1] == num:
                num = result.pop() * 2
            result.append(num)
        return result