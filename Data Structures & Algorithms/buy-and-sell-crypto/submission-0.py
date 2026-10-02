class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #if the first one is the highest, return zero
        #ideally buy at the low, sell at the high, as long as the high is after the low
        #orrr for each day we can choose to buy or not buy. implement recursion and DP
        #bro we just want the biggest difference between a pair of numbers in the array, WITHOUT absolute value. If it's smaller than zero we return zero.
        #try to make it O(n) time O(1) space
        #brute force it with O(n^2) then use dp? nahh but we dont want extra space
        max_profit = 0
        lhs=0
        rhs=1
        while rhs < len(prices):
            if prices[lhs] < prices[rhs]:
                profit = prices[rhs]-prices[lhs]
                max_profit=max(max_profit, profit)
            else:
                lhs = rhs
            rhs +=1
        return max_profit
        