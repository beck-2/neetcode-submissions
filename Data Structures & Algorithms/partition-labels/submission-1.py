from dataclasses import dataclass
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last={}
        for i, c in enumerate(s):
            last[c]=i
        res = []
        start = end = 0
        for i, c in enumerate(s):
            end = max(end, last[c])
            if i == end: #dont need to extend interval
                res.append(end - start + 1)
                start = i + 1
        return res
        """
        #find intervals, then iterate through to see whether we must extend
        @dataclass
        class Pair:
            first: int = 0
            last: int = 0
        seen=defaultdict(Pair)
        #build the intervals
        for i, char in enumerate(s):
            if char in seen:
                seen[char].last=i
            else:
                seen[char].first, seen[char].last =i, i
        #merge them
        res=[]
        for i, char in enumerate(s):
            l=seen[char].last
            f=seen[char].first
            while i <= l:
                if seen[char].last >l:
                    l=seen[char].last #grow/merge the intervals
                i+=1
            res.append((l-f)+1)
        return res



        
        #keep track of first and last time we see a letter, that's our interval. Then merge overlapping intervals. but how do we do that without sorting them?
        #just iterate through the original string again! 
        #coult we iteratively chop it and check whether a given char is in the rest of the string?
        #O(n) time and O(m) space where m is num unique chars -> I'm thinking hash table?
        @dataclass
        class Pair:
            a: int = 0
            b: int = 0
        seen=defaultdict(pair)

        """