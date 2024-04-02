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

    def has_loop(self):
        slow=self.head
        fast=self.head
        while slow and fast and fast.next:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                return True
        return False    


linked=LinkedList(11)
linked.append(10)
linked.append(12)
linked.append(15)
print(f"{linked.has_loop()}")

my_linked_list_1 = LinkedList(1)
my_linked_list_1.append(2)
my_linked_list_1.append(3)
my_linked_list_1.append(4)
my_linked_list_1.tail.next = my_linked_list_1.head
print(my_linked_list_1.has_loop() )