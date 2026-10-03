import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #go back and implement this with bucketsort later
        maxh=[-x for x in stones] #negating values so we can use builtin heapq
        heapq.heapify(maxh)
        while maxh:
            x=-heapq.heappop(maxh) #negate it since we're using minheap
            if maxh:
                y=-heapq.heappop(maxh)#negate it since we're using minheap
            else:
                return x #last one standing
            if (x != y): heapq.heappush(maxh, -(abs(y-x)))

        return 0



"""
         old: misread the problem lowkey
        maxh=[-x for x in stones] #negating values so we can use builtin heapq
        heapq.heapify(maxh)
        while maxh:
            x=-heapq.heappop(maxh) #negate it since we're using minheap
            if maxh:
                y=-heapq.heappop(maxh)#negate it since we're using minheap
            else:
                return x #last one standing
            if x<y: heapq.heappush(maxh, -(y-x))

        return 0
            
        """