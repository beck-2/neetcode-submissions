class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #oopsies it's not sorted but we can sort it!!
        if not position:
            return 0
        num_fleets=0
        curr_arrival_time=0
        for p, s in sorted(zip(position, speed), reverse=True): #we iterate through both simultaneously
            arrival_time=(target-p)/s
            if curr_arrival_time < arrival_time:
            #start a new fleet
                num_fleets +=1
                curr_arrival_time=arrival_time
        return num_fleets
