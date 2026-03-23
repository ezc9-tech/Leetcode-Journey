# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #We need two pointers one for the current and one for the prev nodes
        curr = head
        prev = None

        #While not at the end of the list
        while curr:
            #We will go ahead and look ahead of our first pointer
            temp = curr.next
            #Then we will say our first pointer's next is equal to the pointer behind it
            curr.next = prev
            #Then move the pointer behind it to where the curr pointer is
            prev = curr
            #Lastly move the curr pointer up
            curr = temp
        #After this loop has repeated for all nodes return the prev pointer
        #which is the reverse linked list
        return prev