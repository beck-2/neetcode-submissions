import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #sorting is trivial
        #as we iterate, keep a heap of size k (do a minheap even tho it says largest?) then just pop from it and return
        minh=[]

        for num in nums:
            heapq.heappush(minh, num)
            if len(minh) > k:
                heapq.heappop(minh)
        return heapq.heappop(minh)