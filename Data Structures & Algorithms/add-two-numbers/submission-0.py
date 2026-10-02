# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #reverse, then add while creating a new list and keeping track of carries
        #orr just parse what the lists say, then add those two integers and construct a new linked list to represent
        multiple=1
        sum=0
        while l2:
            sum += (l2.val * multiple)
            l2=l2.next
            multiple *=10
        multiple=1
        while l1:
            sum += (l1.val * multiple)
            l1=l1.next
            multiple *=10
        #sum is accurate. Now just separate out digits one by one and construct a linked list with them! buttt do i need a dummy node or construct from the other direction? or j keep a ptr from the last one
        prev=None
        first=True
        if sum==0:
            return ListNode(0)
        while sum !=0:
            digit=sum%10
            sum //= 10
            newNode=ListNode(digit) #next gets initialized to none
            if first:
                head=newNode
                first=False
            curr=newNode
            if prev:
                prev.next=curr
            prev=curr
        return head
