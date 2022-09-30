#create node
#create link list
#add node to the linklist
#print link list


class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linklist:
    def __init__(self):
        self.head=None

    def insert(self,newNode):
        #head->john->None
        if self.head is None:
            self.head=newNode
        else:
            #head->john->-> shakti-> None || john->-> singh
            #self.head.next=newNode
            #traveee from the starting
            lastNode=self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode=lastNode.next
            lastNode.next=newNode

    def printList(self):
        currentNode=self.head 
        while True:
            if currentNode is None:
                break
                print(currentNode.data)
                currentNode=currentNode.next 
            

fistnode=node("priya")
sin_linklist=Linklist()
sin_linklist.insert(fistnode)
secondNode=node("shakti")
sin_linklist.insert(secondNode)
thirdNode=node("singh")
sin_linklist.insert(thirdNode)
sin_linklist.printList()
