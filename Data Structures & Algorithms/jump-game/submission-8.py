class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        # slightly rewrite code to make more concise
        debt=0
        for i in range (len(nums)-1,-1,-1): #go through backwards 
            if nums[i] !=0 and debt<=nums[i]:
                debt=1
            else:
                debt +=1
        return debt==1
        """
        #try a dp approach for fun:
        memo= {}
        def dfs(i):
            if i in memo:
                return memo[i]
            if i == len(nums)-1:
                return True
            if nums[i]==0:
                return False
            end=min(len(nums), i + nums[i] + 1) #otherwise might go outta bounds
            for j in range(i+1,end):
                if dfs(j):
                    memo[i] = True
                    return True
            memo[i] = False
            return False
        return dfs(0)

        
        # what if we carry "jump debt" backwards through the array?
        #no negative jumps so we can one pass ts
        #
        if len(nums)==1:
            return True
        debt=1
        for i in range (len(nums)-2,-1,-1): #go through backwards starting from second to last index
            if nums[i] !=0 and debt<=nums[i]:
                debt=1
            else:
                debt +=1
        if debt==1:
            return True
        return False

            


        
        #naive recursive solution: for each possible index we can jump to, see whether we can reach the end from there. Base case is it reached the end or we landed on a zero.
        #do i need extra info? (ex. passing an index or value??)
        if nums[0] == 0: return False
        if nums[0] == nums[-1] return True
        for i in range(len(nums))
        """