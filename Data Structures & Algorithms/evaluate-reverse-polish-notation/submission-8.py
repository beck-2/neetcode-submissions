class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        #basic rule: whenever we reach an operator, operate on the two digits directly under it
        from collections import deque
        stack=deque()
        for token in tokens:
            if token in {"+", "-", "/", "*"}:
                b=int(stack.pop())
                a=int(stack.pop())
                if token == "+":
                    stack.append(a+b)
                elif token == "-":
                    stack.append(a-b)
                elif token == "*":
                    stack.append(a*b)
                else:
                    stack.append(a/b)
            else:
                stack.append(token)  
        return int(stack.pop())


        