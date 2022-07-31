from typing import List

# Time Complexity O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            value = target-nums[i]
            if value in seen:
                return [seen[value],i]
            seen[nums[i]] = i

# Brute Force Solution 
# Time Complexity O(n^2)
class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]