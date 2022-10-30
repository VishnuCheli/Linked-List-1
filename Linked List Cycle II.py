#Time Complexity:: O(n)-all nodes are visited and some are traversed multiple times
#Space Complexity:: O(1)-no extra space used
#Did this code successfully run on Leetcode : Yes
#Any problem you faced while coding this : No
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        
        if not head: #edge case
            return head
        
        slow = head
        fast = head
        cycle=False #creating a flag to check if there is cycle
        
        while fast!=None and fast.next!=None:
            slow = slow.next #slow node will eventually meet with fast
            fast = fast.next.next
            if slow==fast:
                cycle=True #trigger cycle flag
                break
                
        if not cycle: #if there is no cycle just return none
            return None
        
        slow=head #restart slow pointer
        while slow!=fast: #if if slow meets fast #2(c+a)=c+a +b+a -> c=b (1)-c->(2)-a->(3)-b->(2)
            slow=slow.next #slow moves one at a time and stops exactly on the cycle start
            fast=fast.next #fast pointer is stuck inside loop and will meet slow
            
            
        return slow #returning the node
        