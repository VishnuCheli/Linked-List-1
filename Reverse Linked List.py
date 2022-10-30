#Time Complexity:: O(n)-all nodes are visited in one pass
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        prev=None #the head has to point to null
        curr=head 
        
        while curr!=None: #till the curr hits the last node
            temp=curr.next #temp keeps track of the next node in the original linked list
            curr.next = prev #reverse the curr.next pointer to backward dir
            prev = curr  #no the previous node becomes the current node
            curr = temp #the current node becomes the temp node which is the next node to reverse pointer
            
        return prev #when the last null node pointer is reversed the prev node becomes current and that is the new head