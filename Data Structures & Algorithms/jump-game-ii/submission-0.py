class Solution:
    def jump(self, nums: List[int]) -> int:
        #bottom up dp:
        n = len(nums)
        dp = [1000000] * n
        dp[-1] = 0

        for i in range(n - 2, -1, -1):
            end = min(n, i + nums[i] + 1)
            for j in range(i + 1, end):
                dp[i] = min(dp[i], 1 + dp[j])
        return dp[0]


        """
        #will it work to always take the largest valid jump?
        #overall hitting larger jump numbers is good
        #starting from the end, we try to find the leftmost index that can still hit the end? then we try to hop to that??
        #just start with making a memo array of min jumps, starting from END of array
        memo=[None]*len(nums)
        def dfs(i):
            if memo[i] is not None:
                return memo[i]
            
        return dfs(0)



        
        #min jumps!! except the array is always valid
        memo=[None] * len(nums) #initialize array storing min jumps to get to end
        #should we initialize with values of infinity?
        def dfs(i):
            if memo[i] is not None:
                return 
            


        
        goal=len(nums)-1
        minhops=0
        for i in range(len(nums)-2,-1,-1):
            if (nums[i]+i)>=goal:
                goal=i
                minhops+=1
        return minhops
        """