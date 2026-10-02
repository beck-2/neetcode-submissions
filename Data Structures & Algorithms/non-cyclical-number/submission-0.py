class Solution:
    def isHappy(self, n: int) -> bool:
        #stop if a number has already been seen, because it's cyclical
        #we can build a set of the answers
        import string
        seen={n}
        while n !=1 :
            digits=str(n)
            sum_digits=0
            for digit in digits:
                sum_digits+= int(digit) * int(digit)
            n=sum_digits
            if n in seen:
                return False
            seen.add(n)
        return True
