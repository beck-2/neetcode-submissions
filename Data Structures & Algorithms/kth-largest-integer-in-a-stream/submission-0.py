import heapq
class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        #make minheap of size k
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) #only store k elements in minheap

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        return self.minHeap[0] #the top of the minheap is the minimum of the k maximum numbers




        
        #3:16
        #insert a val into the heap (literally just at the end) and then return the kth largest (just heap[k])
        #if a maxheapify function exists in python lets use that otherwise gota implement



        
