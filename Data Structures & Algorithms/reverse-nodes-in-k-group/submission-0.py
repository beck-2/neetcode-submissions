# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        allPrev=dummy

        while True:
            kth=self.findk(allPrev, k)
            if not kth:
                break
            allNext=kth.next

            prev,curr = kth.next, allPrev.next
            while curr !=allNext:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            temp=allPrev.next
            allPrev.next=kth
            allPrev=temp

        
        return dummy.next
    def findk(self, curr, k):
        while curr and k>0:
            curr = curr.next
            k-=1
        return curr



        