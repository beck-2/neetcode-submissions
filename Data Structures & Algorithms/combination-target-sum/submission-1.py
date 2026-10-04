class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        #lowkeeyyyy the value of nums is bounded pretty tightly (2 to 30) can we just make a frequency map then use backtracking for all valid combos?
        #dont actually need frequency map because all nums are unique lol
        #O(2^(t/m)) time and O(t/m)
        res=[]
        #what im abt to do is O(n^2) but i dont care since the overall time complexity is so cooked
        
        def backtrack(curr, curr_sum,ind):
            if curr_sum == target:
                res.append(curr[:]) #cuz lists are passed by reference i think?? we need to copy it
            else: 
                for i in range(ind, len(nums)):
                    if curr_sum + nums[i] > target:
                        continue
                    curr.append(nums[i])
                    backtrack(curr, curr_sum + nums[i], i)   # i, not i+1: reuse allowed
                    curr.pop()

        backtrack([],0,0)
        return res
            
        
        """
        
        for i, num in enumerate(nums):
            
            sub=[num]
            sumSub=num
            while sumSub < target:
                #try addind new stuff, including the current num
        """

        