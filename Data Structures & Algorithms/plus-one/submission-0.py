class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        #literally just start at the end
        rhs=len(digits)-1
        while digits[rhs] == 9:
            digits[rhs] = 0
            if rhs == 0:
                digits.insert(0,0)
            else:
                rhs -=1
        digits[rhs] +=1
        return digits