class Solution:

    def encode(self, strs: List[str]) -> str:
        #basically let's join it with a certain character using "".join(strs) ... but what can we join with? ORR just have the split indices at the back of the new string!! lets start with the indices with x in between all of them, and the first y is where the actual string starts
        #so genuinely just append the length of each to the start of it
        #have a pointer at the end working backwards? like maybe? 
        #join these hoes with a y
        num_strs = len(strs)
        for i in range(num_strs -1, -1, -1): #count down instead! for easier decoding, so the number on the end is the len of the first str
            strs.append("y"+str(len(strs[i])))
        print(("".join(strs)))
        return ("".join(strs))

    def decode(self, s: str) -> List[str]:
        output=[]
        #iterate from the back and front til the pointers meet
        beginning=0
        end=len(s)-1
        while beginning < end:
            len_str=0
            while s[end] != "y":
                end -=1
                len_str+=1
            begin_slice=int(s[(end+1) : (end+1+len_str)])
            output.append(str(s[beginning:(beginning+begin_slice)]))
            beginning += begin_slice
            end -=1
        return output
