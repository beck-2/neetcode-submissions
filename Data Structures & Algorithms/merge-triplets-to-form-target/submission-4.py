class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        x,y,z=False,False,False
        for triplet in triplets:
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2]>target[2]:
                continue
            if triplet[0] == target[0]:
                x=True
            if triplet[1] == target[1]:
                y=True
            if triplet[2]==target[2]:
                z=True
        return x and y and z

        """
        #greedy stays ahead. for each x, y, z, we want THOSE values to be high and everything else to be low. For example, if we find a triplet that contains x, the second val must be less than or equal to y, and the third val less than or equal to z
        x, y, z, = False, False, False #will update as we find
        for triplet in triplets:
            if triplet[0] == target[0] and triplet[1] <=target[1] and triplet[2] <=target[2]:
                x=True
            if triplet[1] == target[1] and triplet[0] <=target[0] and triplet[2]<=target[2]:
                y=True
            if triplet[2] == target[2] and triplet[0] <=target[0] and triplet[1] <=target[1]:
                z=True
        return x and y and z
        """
