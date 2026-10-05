class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return
        maxsum= nums[0] #relies on nums not being empty
        prevsum = float("-inf")
        for i in range(len(nums)):
            prevsum=max(nums[i], prevsum+nums[i])
            maxsum=max(prevsum, maxsum)
        return maxsum
