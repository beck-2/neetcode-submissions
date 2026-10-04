class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #use recursion: either we include this num or we don't
        res=[[]]
        for num in nums: #for every number in input array
            res += [subset + [num] for subset in res] # for every subset already in the array, make a new subset with the current number tacked on
        return res

        """ dont fully understand this bit manipulation version
        #can we treat each one as like true or false??
        #O(n*2^n) time is cooked, O(n) space
        #use recursion???? or nah just pattern these hoes in correctly
        #whats the number of power sets again lol... 2^len(nums)
        n=len(nums)
        res=[]
        for i in range(1<<n):
            subset=[nums[j] for j in range(n) if (i & (1 << j))]
            res.append(subset)
        return res
        """