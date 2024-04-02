class Node:

    def __init__(self,value):
        self.value=value
        self.next=None



class LinkedList:

    def __init__(self,value):
        new_node=Node(value)
        self.head=new_node
        self.tail=new_node
        self.length=1
        
        
    def print_list(self):
        temp=self.head
        while temp is not None:
            print(temp.value)
            temp=temp.next

    def append(self,value):
        new_node=Node(value)
        if self.length==0:
            self.head=new_node
            self.tail=new_node
        else:
            self.tail.next=new_node
            self.tail=new_node
        self.length+=1
        return True
    
    def pop(self):
        if self.length==0:
            return None
        elif self.length==1:
            tempNode=self.head
            self.head=None
            self.tail=None
            self.length-=1
            return tempNode
        else:
            currNode=self.head
            while currNode.next is not None:
                nextNode=currNode.next
                if nextNode.next is None:
                    currNode.next=None
                    self.tail=currNode
                    self.length-=1
                    break
                currNode=currNode.next
                
    def prepend(self,value):
        newNode=Node(value)
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=self.head
            self.head=newNode
        self.length+=1
        return True
    
    def pop_first(self):
        if self.length==0:
            return None
        temp=self.head
        self.head=self.head.next
        temp.next=None
        if self.length==0:
            self.tail=None
        return temp
    
    def get(self,index):
        if (index<0 or index >=self.length):
            return None
        temp=self.head
        for _ in range(index):
            temp=temp.next
        return temp
    
    def set(self,index,value):
        temp=self.get(index)
        if temp is not None:
            temp.value=value
            return True
        return False

    def insert(self,index,value):
        if (index<0 or index >self.length):
            return None
        if index==0:
            return self.prepend(value)
        if index==self.length:
            return self.append(value)
        else:
            preNode=self.get(index-1)
            newNode=Node(value)
            changedNode=preNode.next
            preNode.next=newNode
            newNode.next=changedNode
            self.length+=1    
            return True

    def remove(self,index):
        if (index<0 or index>=self.length):
            return None
        if index==0:
            return self.pop_first()
        if index==self.length-1:
            return self.pop()
        else:
            prevNode=self.get(index-1)
            temp=prevNode.next
            prevNode.next=temp.next
            temp.next=None
            self.length-=1
            return temp
    def reverse(self):
        temp=self.head
        self.head=self.tail
        self.tail=temp
        after=temp.next
        before=None
        for _ in  range(self.length):
            if temp is None:
                break
            after = temp.next  
            temp.next = before
            before = temp
            temp = after             
        
        



my_linkedlist=LinkedList(4)
print("using append():")
my_linkedlist.append(2)
my_linkedlist.append(6)
my_linkedlist.append(8)
my_linkedlist.append(9)
my_linkedlist.print_list()
print("using pop():")
my_linkedlist.pop()
my_linkedlist.pop()
my_linkedlist.print_list()
print("using prepend():")
my_linkedlist.prepend(10)
my_linkedlist.prepend(15)
my_linkedlist.prepend(112)
my_linkedlist.print_list()
print("using pop_first():")
my_linkedlist.pop_first()
my_linkedlist.pop_first()
my_linkedlist.print_list()
print("using get():")
print(f"using indexing getting value: {my_linkedlist.get(0)}")
print(f"using indexing getting value: {my_linkedlist.get(3)}")
print("using set():")
print(f"Setting new value:{my_linkedlist.set(1,121)}")
print(f"Setting new value:{my_linkedlist.set(3,114)}")
my_linkedlist.print_list()
print("using insert():")
print(f"inserting new node  in the middle of linked list:{my_linkedlist.insert(1,144)}")
print(f"inserting new node  in the Ist position of linked list:{my_linkedlist.insert(0,14)}")
print(f"inserting new node  in the last position of linked list:{my_linkedlist.insert(8,23)}")
print(f"inserting new node  in the middle of linked list:{my_linkedlist.insert(5,111)}")
print(f"inserting new node  in the middle of linked list:{my_linkedlist.insert(3,44)}")
print(f"inserting new node  in the middle of linked list:{my_linkedlist.insert(8,34)}")
my_linkedlist.print_list()
print("Using remove():")
print(f"removing a node in the middle of the linked list:{my_linkedlist.remove(3)}")
print(f"removing a node from 1st positiom of the linked list:{my_linkedlist.remove(0)}")
print(f"removing a node from last postion of the linked list:{my_linkedlist.remove(7)}")
print(f"removing a node in the middle of the linked list:{my_linkedlist.remove(2)}")
print(f"removing a node in the middle of the linked list:{my_linkedlist.remove(1)}")
print(f"removing a node in the middle of the linked list:{my_linkedlist.remove(-1)}")
print(f"removing a node in the middle of the linked list:{my_linkedlist.remove(4)}")
my_linkedlist.print_list()
print("using reverse ():")
my_linkedlist.reverse()
my_linkedlist.print_list()
print(f"linked list head :{my_linkedlist.head.value}")        
print(f"linked list tail :{my_linkedlist.tail.value}")       
