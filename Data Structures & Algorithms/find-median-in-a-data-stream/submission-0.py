import heapq
class MedianFinder:
    #if we were doing a mean we wouldn't need a data structure
    #store the median and the two - three entries closest to it??
    #cannn we do median without a data structure?
    #lowkey no. let's do a binary tree with the median at the middle??
    #make a maxheap and minheap
    def __init__(self):
        self.big, self.small= [], [] #small is a maxheap, big is a minheap

    def addNum(self, num: int) -> None:
        #O(logn) time
        if self.big and num>self.big[0]:
            heapq.heappush(self.big, num)
        else:
            heapq.heappush(self.small, -1 * num) #at first all nums will end up here
        if len(self.small) > len(self.big)+1:
            #balance by moving from small pile to large pile
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.big, val)
        if len(self.big) > len(self.small)+1:
            #vice versa
            val = -1 * heapq.heappop(self.big)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float: 
        #O(1) time O(n) space
        if len(self.small) > len(self.big):
            return -1 * self.small[0]
        elif len(self.big) > len(self.small):
            return self.big[0]
        return (-1 * self.small[0] + self.big[0]) / 2.0

        