class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #easiest way is sorting but that's O(nlogn)
        #num is start of a sewuency if num-1 isn't in the set
        numset=set(nums)
        longest=0 #in case empty
        for num in numset:
            if (num-1) not in numset: #it's the start of a new subseq
                length=1
                while (num+length) in numset:
                    length +=1
                longest=max(length,longest)
        return longest
        