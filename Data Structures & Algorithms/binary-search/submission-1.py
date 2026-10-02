class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #array is already sorted! iterative binary search
        l, r = 0, len(nums)-1

        while l <=r:
            m=l+((r-l)//2) #prevent overflow
            if nums[m] <target:
                l=m+1 #answer must be in top of array
            elif nums[m] > target:
                r=m-1 #answer must be in bottom part of the array
            elif nums[m] == target:
                return m
        return -1
        
        

        
        