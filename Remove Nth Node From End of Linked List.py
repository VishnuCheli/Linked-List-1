#Time Complexity:: O(n)-all nodes are visited once
#Space Complexity:: O(1)-no extra space used as everything is inplace
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        count = 0 
        dummy = ListNode("dummy", head)#creating a node with random value pointing to head
        slow = dummy #dummy node is used to simplify index issue as you're traversing n nodes
        fast = dummy 
        
        while count<n: #removing nth node from end of list so
            fast = fast.next #seperate slow and fast by n nodes
            count += 1
            
        while fast.next!=None: #when fast.next is null, slow will be behind by n+1 nodes which allows to cut of the nth node
            slow = slow.next
            fast = fast.next
        
        slow.next = slow.next.next #nth node is cut of as n-1.next.next = n+1
        
        return dummy.next #return the original head without the dummy, this also stops edge case like just having 1 node