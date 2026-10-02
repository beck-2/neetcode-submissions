class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_map = {}
        for i in range (len(nums)):
            if ((target-nums[i]) in my_map):
                return [my_map[target-nums[i]], i]
            my_map[nums[i]] = i
