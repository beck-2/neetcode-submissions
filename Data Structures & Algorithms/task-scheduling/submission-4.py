import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #i dont actually need a heap
        freq = [0] * 26
        for ch in tasks:
            freq[ord(ch) - ord("A")] += 1

        mx = max(freq)
        count_max = freq.count(mx)
        return max(len(tasks), (n + 1) * (mx - 1) + count_max)

        """
        #we should always start with the most freqent character
        #frequency map ->heapify (maxheap?)
        if not tasks:
            return 0
        frequency= [0] * 26 #make an empty 26 element array
        #we could also use a dict but since we know the size, array is better
        for char in tasks:
            frequency[ord(char)-ord("A")] -=1 #negative vals to use minheap
        
        heapq.heapify(frequency)
        maxfreq=heapq.heappop(frequency)
        best=((n+1)*(-maxfreq))-n
        while frequency and heapq.heappop(frequency)==maxfreq:
            best +=1
        return max(len(tasks),best)
        """

        