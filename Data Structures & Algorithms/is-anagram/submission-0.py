class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        #count the frequencies of letters in s, then subtract for t
        from collections import Counter
        return Counter(s) == Counter(t)

        
        