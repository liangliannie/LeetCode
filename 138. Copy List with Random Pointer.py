# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution(object):
    def __init__(self):
        self.visited = {}
        
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head == None:
            return None
        
        if head in self.visited:
            return self.visited[head]
        
        node = RandomListNode(head.label)
        self.visited[head]= node
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)
        return node
    
    def copyRandomList1(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        if head is None:
            return head
        
        visiteddict = {}
        dummy = RandomListNode(0)
        newnode = dummy
        cur = head
        while head:
            newnode.next = RandomListNode(head.label)
            visiteddict[head] = newnode.next
            head = head.next
            newnode = newnode.next
            
        new = dummy    
        while cur:
            node=visiteddict[cur]
            if cur.random is not None:
                node.random = visiteddict[cur.random]
            cur = cur.next
            
        return dummy.next
    
