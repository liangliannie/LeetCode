
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
        if not head:
            return head
        cur = head
        mem = []
        while cur:
            mem.append(cur)
            cur = cur.next
            
        l = len(mem)
        for i in range(l/2):
            mem[i].next = mem[l-i-1]
            mem[l-i-1].next = mem[i+1]
            
        mem[l/2].next = None
            
            
            

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution2(object):
#     def sortList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         def BreakTwoList(head):
#             pre = head
#             slow = head
#             fast = head
#             while fast and fast.next:
#                 pre = slow
#                 slow = slow.next
#                 fast = fast.next.next
#             pre.next = None # Break the two link!
#             return head, slow
# 
#             
#         def merge(list1,list2):
#             pre = ListNode(0)
#             head = pre
#             while list1 and list2:
#                 if list1.val<=list2.val:
#                     head.next = list1
#                     list1 = list1.next
#                 else:
#                     head.next = list2
#                     list2 = list2.next
#                 head = head.next
#             if list1:
#                 head.next = list1
#             if list2:
#                 head.next = list2        
#             return pre.next
#     
#         if not head or not head.next:
#             return head
#         
#         l1,l2 = BreakTwoList(head)
#         return merge(self.sortList(l1), self.sortList(l2))
    
Node1 = ListNode(4)
Node2 = ListNode(2)
Node3 = ListNode(1)
Node4 = ListNode(3)
Node1.next= Node2
Node2.next = Node3
Node3.next = Node4
f=Solution()
# n=(f.sortList(Node1))
# while n:
#     print(n.val)
#     n=n.next

