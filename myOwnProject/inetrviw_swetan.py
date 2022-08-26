
#I=1
#V=5
#X=10
#L=50
#C=100
#D=500
#M=1000

l1 = [2,4,3]
l2 = [5,6,4]
#Output= [7,0,8]
#Explanation: 342 + 465 = 807.
#example -2 
#Input: l1 = [0], l2 = [0]
#Output: [0]
#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]


class interviw:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        a = l1 
        b = l2 
        arr1 = []
        arr2 = []

        while a:
          arr1.append(a.val)
          a = a.next

        while b:
          arr2.append(b.val)
          b = b.next

        arr1.reverse()
        arr2.reverse()

        inta = int("".join(str(x) for x in arr1)) #converting list to strings
        intb = int("".join(str(x) for x in arr2))

        c = list(str(inta + intb)) #performing addition - the answer we wanted

        # assign last digit to new ListNode which represents the head of returned LL
        head = l3 = ListNode(c.pop())

        c.reverse()

        # traverse remaining digits, assigning each to new ListNode
        for i in c:
            l3.next = ListNode(i)
            l3 = l3.next

        return head 




