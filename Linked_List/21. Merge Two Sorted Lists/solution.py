# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #We need to have a completely new list so we need a new list node
        #But we want to return the beginning of the list so technically we need two

        list3 = node = ListNode()

        #Now we need to go through each list to see which values are less than the other
        while list1 and list2:
            #If the list1 val is smaller than list2 val
            if list1.val < list2.val:
                #Then node's next val will be list1
                node.next = list1
                #Iterate list1
                list1 = list1.next
            #Else do the opposite
            else:
                node.next = list2
                list2 = list2.next
            #Afterwards make sure to iterate the node
            node = node.next
        #Lastly if we run out of list1 and list2 has remaining elements
        #Add them onto the end of the node
        node.next = list1 or list2

        #Return the new lists head
        return list3.next
                
