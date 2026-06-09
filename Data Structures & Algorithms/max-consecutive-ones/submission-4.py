class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0 
        current_count = 0
        for num in nums:
            current_count = current_count + 1 if num==1 else 0
            max_count = max(max_count, current_count)
        return max_count