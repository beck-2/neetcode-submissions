class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if (len(s) != len(t)):
            return False
        #count the frequencies of letters in s, then subtract for t
        counts = [0] * 26 #one for each of the 26 lowercase letters
        for i in range(len(s)):
            counts[ord(s[i])-97] +=1
            counts[ord(t[i])-97] -=1
        return all(c == 0 for c in counts)

        
        