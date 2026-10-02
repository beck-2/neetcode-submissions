class Solution:
    def findMin(self, nums: List[int]) -> int:
        #ok this array is sorted... can we use modified binary search?
        #all elements are unique... make O(logn) solution
        #we're just finding the index it was rotated at (since that's the min)
        #we lowkey have to look around the value.. split it in thirds?
        #if we find a place where the left element is larger than the right, we've found our min! so it's a regular binary search except we gotta consider 2 els
        l, r = 0, len(nums) - 1
        while l < r:
            m = l + (r - l) // 2
            if nums[m] < nums[r]:
                r = m
            else:
                l = m + 1
        return nums[l]