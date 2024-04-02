class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class LinkedList:

    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode 

    def append(self,value):
        newNode=Node(value)
        if self.head is None:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            self.tail=newNode 

    def find_middle_node(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow

linked=LinkedList(4)
linked.append(5)
linked.append(9)
node=linked.find_middle_node()
print(node.value)
my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
# my_linked_list.append(5)

print( my_linked_list.find_middle_node().value )




        
