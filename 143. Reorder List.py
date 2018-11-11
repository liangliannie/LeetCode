# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        
        
        def BreakTwoList(head):
            pre = head
            slow = head
            fast = head
            while fast and fast.next:
                pre = slow
                slow = slow.next
                fast = fast.next.next
            pre.next = None
            return head, slow
        
        def ReverseList(head):
            if not head or not head.next:
                return head
            pre = None
            first = head
            second = head.next
            while first and first.next:
                first.next = pre
                pre = first
                first = second
                second = second.next
            first.next = pre 
            return first
        
        def merge(l1, l2):
            dummy = ListNode(0)
            h = dummy
            Flag = True
            while l1 and l2:
                if Flag:
                    h.next = l1
                    l1 = l1.next
                    Flag = False
                else:
                    h.next = l2
                    l2 = l2.next
                    Flag = True
                h = h.next
            if l1:
                h.next = l1
            if l2:
                h.next = l2
            return dummy.next
        
        if not head or not head.next:
            return head
        l1,l2 = BreakTwoList(head)
        d = merge(l1, ReverseList(l2))
        return d

Node1 = ListNode(1)
Node2 = ListNode(2)
Node3 = ListNode(3)
Node4 = ListNode(4)
Node1.next= Node2
Node2.next = Node3
Node3.next = Node4
f=Solution()
n=(f.reorderList(Node1))
while n:
    print(n.val)
    n=n.next
            