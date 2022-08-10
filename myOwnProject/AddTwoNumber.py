class Solution():
    ListNode=[]
    #def addTwoNumbers(self, l1:ListNode, l2:ListNode)->ListNode:
    try:
        l1 = [2,4,3] 
        l2 = [5,6,4]        
        num1=0 
        num2=0
    except Exception as df:
        []
    
    while l1:
        num1 = num1 * 10 + l1.val
        l1 = l1.next
    
    while l2:
        num2 = num2 * 10 + l2.val
        l2 = l2.next
        
        sum_ = num1 + num2
        curr = head = ListNode(0)
        if sum_ == 0:
    return head
        
    while sum_ > 0:
        head.next = ListNode(sum_ % 10)
        head = head.next
        sum_ //= 10
    
    prev = None
    head = curr.next
    while head:
         nxt = head.next
         head.next = prev
         prev = head
         head = nxt
    return prev