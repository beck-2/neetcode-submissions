class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = s[::-1]
        x, y = 0, 0
        while (x < len(s)) and (y < len(r)):
            while x < len(s) and not s[x].isalnum():
                x += 1
            while y < len(r) and not r[y].isalnum():
                y += 1
            if x < len(s) and y < len(r):
                if s[x].lower() == r[y].lower():
                    x += 1
                    y += 1
                else:
                    return False
        return True