# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        fast = slow = dummy
        for _ in range(n):
            fast = fast.next
        while fast.next:
            fast = fast.next
            slow = slow.next
        slow.next = slow.next.next
        return dummy.next
        """
        #reverse first?? like while i go along to the end
        curr = end =self.helpReverse(head)
        #then remove
        prev, after = None, curr.next
        counter=1
        while curr and counter<n:
            #walk
            prev=curr
            curr=after
            after=after.next
            counter +=1
        #delete
        prev.next=after
        #then reverse again!
        return self.helpReverse(end)


    def helpReverse(self, head: Optional[ListNode]) -> Optional [ListNode]: # returns the end of the reversed list so I can use it
        prev, curr = None, head
        while curr:
            after=curr.next
            curr.next=prev
            prev=curr
            curr=after
        return prev
        """