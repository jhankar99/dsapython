class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        self.prev=None


class DoublyLinkedlist:

    def __init__(self,value):
        newNode=Node(value)
        self.head=newNode
        self.tail=newNode
        self.length=1

    def print_list(self):
        temp=self.head
        ddlist=[]
        while temp:
            ddlist.append(str(temp.value))
            temp=temp.next
        print(("->").join(ddlist))
   
    def append(self,value):
        newNode=Node(value)
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            self.tail.next=newNode
            newNode.prev=self.tail
            self.tail=newNode
        self.length +=1
        return True
    
    # def testing(self):
        # temp=self.tail
        # print(temp.value)
        # c=temp.prev
        # print(c.value)
        # d=c.prev
        # print(d.value)
    
    def pop(self):
        if self.length==0:
         return None
        temp=self.tail
        if self.length==1:
            self.head=None
            self.tail=None
        else:
            self.tail=self.tail.prev
            self.tail.next=None
            temp.prev=None
        self.length-=1
        return temp        
    

    def  prepend(self,value):
        newNode=Node(value)
        temp=self.head
        if self.length==0:
            self.head=newNode
            self.tail=newNode
        else:
            newNode.next=temp
            temp.prev=newNode
            self.head=newNode
        self.length +=1
        return True
    
    def pop_first(self):
        temp=self.head
        if self.length==0:
            return None
        elif self.length==1:
            self.head=None
            self.tail=None
        else:
            currNode=temp.next
            currNode.prev=None
            temp=None
            self.head=currNode
        self.length -=1
        return temp    
              
     
        
        
        

    

 

dou=DoublyLinkedlist(2)
dou.print_list()
print("USING  append():")
dou.append(23)
dou.append(45)
dou.append(11)
dou.append(33)
dou.print_list()  
# dou.testing()     
print("Using pop():")
print(dou.pop().value)
dou.pop()
dou.pop()
dou.print_list()
print("Using prpend():")
dou.prepend(98)
dou.prepend(43)
dou.prepend(9)
dou.print_list()
print("using prepend():")
dou.pop_first()
dou.pop_first()
dou.print_list()



                 