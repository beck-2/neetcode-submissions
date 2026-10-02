# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #find the middle
        mid, end = head, head.next
        while end and end.next:
            mid = mid.next
            end = end.next.next
        #reverse
        second=mid.next
        prev=mid.next=None
        while second:
            temp=second.next
            second.next=prev
            prev=second
            second=temp
        #swap merge
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next=second
            second.next=temp1
            first, second = temp1, temp2



        """
        #lowkenuinely start by marching a pointer to the end
        #reverse it halfway through??? nah we can't tell halfway UNLESS slow fast ptr
        end, beginning, mid = head, head, head
        #slow fast ptr to find mid
        while end.next is not None and end.next.next is not None:
            mid=mid.next
            end=end.next.next
        prev=mid
        if end.next is not None:
            end=end.next
            mid=mid.next
        #reverse from mid to end
        while mid:
            temp=mid.next
            mid.next=prev
            prev=mid
            mid=temp
        while end !=beginning:
            temp_beg=beginning.next
            beginning.next=end
            beginning=temp_beg
            temp_end=end.next
            end.next=beginning
            end=temp_end
        """
        
        """
        end, beginning = head, head
        while end.next is not None:
            end=end.next
        #end is now at the end of the linked list
        while end != beginning:
            temp=beginning.next
            beginning.next=end
            beginning=temp

        """