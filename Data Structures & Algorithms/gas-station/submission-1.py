class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total=0
        res=0
        for i in range(len(gas)):
            total += (gas[i]-cost[i])
            if total <0:
                total=0
                res=i+1 #move start
        return res

        """
        possible = 0
        maxind=0
        maxval=gas[0]-cost[0]
        for i in range(len(cost)):
            cost[i]=gas[i]-cost[i]
            if cost[i]>maxval:
                maxval=cost[i]
                maxind=i
            possible += cost[i]
        if possible <0:
            return -1
        return maxind



        #naively, try to complete circuit from every index, otherwise return -1
        #but that's O(n^2)... let's try O(n) time O(1) space
        #we should always stop at every gas station
        #lowkenuinely just start from the max, then see if it's possible... does that work... idk if that's optimal tho
        #could also treat this as a weighted graph problem
        #accumulate fuel first!!
        #can we use the gas and cost arrays to store useful info?
        """

        