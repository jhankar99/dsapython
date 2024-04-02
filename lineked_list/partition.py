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

    def partition_list(self,x):
        less_list=None
        greater_list=None
        if x       efewfjewfwefwefew 