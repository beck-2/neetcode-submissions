import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #minheapify based on distance?
        def distance(x, y):
            ## x ** 2 is the same as x^2
            #we don't even need to use the true distance formula because our point is the origin
            return math.sqrt((x ** 2) + (y ** 2))
        h=[(distance(x,y),x,y) for x,y in points] #reorder by distance
        heapq.heapify(h) 
        res=[]
        while h and k>0:
            res.append(list(heapq.heappop(h)[1:]))
            k-=1
        return res

