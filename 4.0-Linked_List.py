 
# * Simple Linked List Implementation 


# * Access an element O(n)
# * Add/remove at an iterator position O(1)
# * Add/remove at an first element O(1)
# * Add last element O(1)
# * Remove last element O(n)
# TODO Removing element for double linked list it is O(1)

"""
• Array                                                                       
• Fixed number
• Size need to be specific during decleration
• Static:It's location is allocated during compile time
• Stored consecutively
• Direct or random access method
• Specify the array index or subscript
• Binary search and linear search 

• Linked List
• Grow and contract since of insertions and deletions
• Maximum size depends on heap
• Dynamic:It's node is located during run time
• Stored randomly
• Sequential access method
• Traverse starting from the first node in the list by pointer
• Linear search.


"""
__author__ = "Metehan Özcan"



class node: #* Node constructor
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linkedlist: 
    def __init__(self):
        self.head = None
        self.size = 0

    def getlength(self):
        return self.size

    def prepend(self, data):
        n = node(data, self.head)
        self.head = n
        self.size += 1  # !

    def append(self, data):
        if self.head == None:
            self.prepend(data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data, None)
        self.size += 1  # !

    def insert(self, index:int,data=None ):  # ?
        """
        Prints value of index.
        Parameters
        ----------
        data : Any
            Given data by user.
        index : Int
            The number of index that u want to insert.       
            
        """
        if type(index) is not int:
            print("Try again insert index")
            return -1
        if index == 0 or None:
            return self.prepend(data)

        if self.size < index:
            print("Data inserted at the end, however the index you gave was not valid.")
            return self.append(data)

        curr = self.head
        count = 0
        while count != index-1:
            curr = curr.next
            count += 1

        #temp = curr.next
        #* Logic Here, We have created a Node for the next index, that pointed by the Current Pointer.
        #* temp = curr.next was the previous next element of the current node. Simply, we merge it.
        curr.next = node(data, curr.next)
        self.size += 1
        return

    def removebeginning(self):
        if self.head == None:
            return "LL is already empty."
        self.head = self.head.next
        self.size -= 1  # !

    def pop(self, index=None):
        """
        Deletes value of index.
            Parameters
            ----------        
            index : Int
                The number of index that u want to delete.       
        """
        # print(index, type(index))
        if self.head == None:
            return "LL is already empty."

        if not isinstance(index, int):
            print("The index you've given was not valid. However last node was deleted.")
            curr = self.head
            while curr.next.next:
                curr = curr.next
            curr.next = None
            self.size -= 1  # !
            return

        if index == 0:
            return self.removebeginning()

        if self.size > index:
            
            curr = self.head
            count = 0
            while count != index-1:
                curr = curr.next
                count += 1
            curr.next = curr.next.next
            self.size -= 1
            return

    def basicSort(self): 
        #* this method is not effective, it is GARBAGE. 
        #* for linked lists use MERGE SORT instead.
        
        curr = self.head
        temp = curr.next
        
        while curr.next: #* While curr.next is not none 
            
            if temp.next == None:                
                if curr.data > temp.data:
                    temp.data, curr.data = curr.data, temp.data #*swap datas
                curr = curr.next #* For iterating loop
                temp = curr      #* For iterating temp.
                
            if curr.data > temp.data:                
                temp.data, curr.data = curr.data, temp.data
                
                if curr.data > temp.next.data:                    
                    temp.next.data, curr.data = curr.data , temp.next.data 
            
                      
            temp=temp.next
            
    
    

    def print(self):

        curr = self.head
        s = ''
        while curr:
            s += str(curr.data)+'--->'
            curr = curr.next
        s += 'None'
        print(s)
    def get(self,index) -> int:
        if index <0 or index>=self.size:
            return -1
        curr = self.head
        for _ in range(0,index):
            #print(_)
            curr=curr.next
        return curr.data
        


ll = linkedlist()


ll.prepend(1)
ll.append(3)
ll.insert(1,2)
ll.insert(2,2)
ll.insert(3,2)
ll.insert(5,2)
ll.print()
ll.pop(1)
print(ll.get(1))
ll.prepend(1)
ll.prepend(2)
ll.prepend(3)
ll.prepend(4)
ll.prepend(5)
ll.prepend(6)
ll.prepend(6)
ll.append(20)
ll.append(76)
ll.append(-2)
ll.append(212)
ll.prepend(50)
ll.prepend(34)
ll.prepend(34)
ll.prepend(1500)
ll.prepend(1021251)



ll.print()
print(ll.get(6))
ll.basicSort()
ll.print()

