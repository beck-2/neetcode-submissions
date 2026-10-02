class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #should we find the pivot first then like rearrage the array and do a regular binary search? or can we do this in one pass... basically if that part of the array is sorted AND target is in it, we can search normally
        l, r = 0, len(nums)-1
        while l<=r:
            m=l+((r-l)//2)
            if nums[m]==target:
                return m
            if nums[l] <=nums[m]: # lower half is sorted
                if target > nums[m] or target < nums[l]: #ans is upper half
                    l=m+1
                else: #correct half and sorted
                    r=m-1
            else: #upper half is sorted
                if target<nums[m] or target > nums[r]:#ans is in the lower half
                    r=m-1
                else:
                    l=m+1

            

        return -1
        """
        find min:
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]
        """
