class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #wanna find the minimum k so i can eat all bananas in h hours
        #O(nlogm) time O(1) space... so we sorting! nah we dont have to
        if len(piles) == 0:
            return 0
        if h<len(piles): return -1 #not valid cuz we dont have enough time
        #basically do we wanna find the value where all the piles can be one-shotted?
        #if I have exactly the amount of hours as piles, my banana eating rate must be the maximum value in the array
        min_k=1 #gotta eat at least one banana per hour
        max_k=max(piles) 
        #now we just check possible k values!
        while min_k<max_k:
            mid=min_k+((max_k-min_k)//2)
            if valid_k(mid, h, piles):
                max_k=mid
            else:
                min_k=mid+1

        return max_k
def valid_k(k:int, h: int, piles:List[int]) -> bool:
    hours = 0
    for pile in piles:
        hours += (pile + k - 1) // k   
        if hours > h:# early exit
            return False
    return True




        