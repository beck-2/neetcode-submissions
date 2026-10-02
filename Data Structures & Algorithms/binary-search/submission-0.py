import bisect
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #array is already sorted!
        index=bisect.bisect_left(nums,target)
        return index if index < len(nums) and nums[index] == target else -1
        

        
        