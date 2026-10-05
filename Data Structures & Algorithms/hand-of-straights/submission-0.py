from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False
        freq = Counter(hand)
        for card in sorted(freq):
            cnt = freq[card]
            if cnt > 0:
                for k in range(groupSize):
                    if freq[card + k] < cnt:  
                        return False
                    freq[card + k] -= cnt
        return True


        """
        freq=[0] * 1000 #can also make this smaller
        for card in hand:
            freq[card] +=1
        #iterate through
        for i in range(1000):

            if freq[i] >0:
                if i+(groupSize) >len(hand):
                    return False
                for k in range(groupSize,-1):
                    freq[i+k] = freq[i+k]-freq[i]

            if freq[i] !=0:
                return False
        return True




        
        #it's only possible to do this if the length of the hand modulus groupsize is equal to 0
        #sort first?? then start from both ends? O(nlogn) so we have time to sort
        if (len(hand) % groupSize) != 0:
            return False #some cards will be left over
        if groupSize==1:
            return True

        hand.sort()
        l, r = 0, len(nums)-1

        """
        
