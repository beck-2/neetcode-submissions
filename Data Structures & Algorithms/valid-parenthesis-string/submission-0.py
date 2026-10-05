class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []
        for i, c in enumerate(s):
            if c == "(":
                left.append(i)
            elif c == "*":
                star.append(i)
            else: #open paren
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while left and star:
            if left.pop() > star.pop(): # * is before (
                return False
        return not left

        """
        stack=[]
        extra=0
        for char in s:
            if char=="(":
                stack.append("(")
            if char=="*":
                extra +=1
            if char==")" and stack:
                if stack.pop() != "(":
                    if extra>0:
                        extra-=1
                    else:
                        return False
            else:
                if extra>0:
                    extra-=1
                else:
                    return False
        while extra>0:
            if not stack:
                return True
            stack.pop()
            extra-=1
        if not stack:
            return True
        return False
        """