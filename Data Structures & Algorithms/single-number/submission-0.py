class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        #the O(1) extra space is hard because this would be very easy to do with a set... I would sort it but that's O(nlogn) time... what if I keep a fixed size array? or manipulate the original list or numbers!!
        #take the xor of the whole array
        result=0
        for num in nums:
            result = num ^ result
        return result


        