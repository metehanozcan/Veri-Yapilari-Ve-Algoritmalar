"""_summary_
Circular Linked List Implementation.



"""

__author__='Metehan Özcan'

class Node:
     
    #* Constructor to create  a new node
    def __init__(self, data,next=None):
        self.data = data
        self.next = next
 
class CircularLinkedList:
     
    #* Constructor to create a empty circular linked list
    def __init__(self):
        self.head = None
        self.size =0
 
    
    def prepend(self,data): #* Add new node at beginning
        newNode=Node(data,self.head)
        curr=self.head        
        
        if not self.head: #* If List is empty.
            newNode.next=newNode
        else:
            while curr.next!=self.head:
                curr=curr.next
            curr.next=newNode
        self.head=newNode
        self.size+=1
        return
   
    
        
    def append(self,data): #* Add new node to the end
        if self.size ==0:
            self.prepend(data)
        newNode=Node(data)        
        curr=self.head
        while curr.next!=self.head:
            curr=curr.next
        curr.next=newNode
        newNode.next=self.head
        self.size+=1
        return
    
    def delete(self): #* Deletes Head
        curr=self.head
        while curr.next !=self.head:
            curr=curr.next
        curr.next=self.head.next
        self.head=self.head.next
        self.size-=1
        return
        
        
    def pop(self): #* Deletes Last Node
        curr=self.head        
        while curr.next.next != self.head:
            curr=curr.next
        curr.next=self.head
        self.size-=1
        return        
        
        
 
 
    #* Function to print nodes in a given circular linked list
    def printList(self):
        curr = self.head
        last=self.head
        s=''
        if self.head is not None:
            while(True):
                s+=str(curr.data)+'--->'
                curr = curr.next
                if (curr == self.head):
                    break
        s+='To The Head Again->'+str(last.data)
        print(s)
        return
 
#*Created Linked List
cll = CircularLinkedList()
 
#* Created linked list will be 2--->1--->4--->5--->To The Head Again->2
cll.prepend(1)
cll.prepend(2)
cll.prepend(3)
cll.append(4)
cll.append(5)
cll.append(6)
cll.delete()
cll.pop()
print ("Circular Linked List;")
cll.printList()
           
