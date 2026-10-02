class Solution:
    def isValid(self, s: str) -> bool:
        from collections import deque
        stack=deque()
        for char in s:
            if (char == "[" or char == "(" or char == "{"): #open
                stack.append(char)
            if not stack:
                return False
            if (char == "]" and stack.pop() != "["):
                return False
            if (char == ")" and stack.pop() != "("):
                return False
            if (char == "}" and stack.pop() != "{"):
                return False
        return not stack
