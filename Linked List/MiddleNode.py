# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        
        currentnode = head
        nodelist = []
        while currentnode:
            nodelist.append(currentnode)
            currentnode = currentnode.next
        
        n = len(nodelist)
        return nodelist[int(n/2)]
