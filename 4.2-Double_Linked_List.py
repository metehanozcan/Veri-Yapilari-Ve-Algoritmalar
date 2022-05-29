




class node:
    def __init__(self, data=None,next=None,prev=None):
        self.data = data
        self.next = next
        self.prev = prev


class linkedlist:
    def __init__(self):
        self.head = None
        self.size = 0

    def prepend(self, data):
        n=node(data,self.head)
        
        if self.head is not None:
            self.head.prev =n
        self.head=n
        self.size+=1
            
    def append(self,data):
        curr = self.head
        
        while curr.next:
            curr=curr.next
        n=node(data)
        curr.next=n
        n.prev=curr
        self.size+=1
        
    
    def insert(self,item,index):
        curr =self.head
        if index == 0:
            self.prepend(item)
        if index > self.size:
            self.append(item)
        count=0
        while count < index-1:
            curr=curr.next
            count+=1
        n=node(item,curr.next,curr)
        curr.next=n
    
    def delete(self,index:int):
        curr =self.head
        if index == 0:
                       
            self.head=curr.next
            return
        if index > self.size:
            return "Error"
        
        count=0
        while count != index-1:
            curr=curr.next
            count+=1
            print(count)
        
        curr.next=curr.next.next
        
        
        
    
    def print(self):

        curr = self.head
        s = ''
        t=''
        while curr:
            s += str(curr.data)+'<==>'
            curr = curr.next
        t+='None<==>'+ str(s) +'None'
        print(t)
        
ll=linkedlist()
ll.prepend(2)
ll.prepend(3)
ll.prepend(4)
ll.append(5)
ll.append(6)
ll.print()
ll.insert(12,5)
ll.delete(15)
ll.print()
