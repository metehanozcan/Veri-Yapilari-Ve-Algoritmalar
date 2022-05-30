
"""
    _summary_
    Hash Table implementation with python, 
    but you can simply use Dictionary data types 
    that represent the implementation of hash tables. 
    
"""

__author__ = 'Metehan Özcan'

#*Here is a simple Hash Table Not Usefull



class HashTable:
    def __init__(self):
        self.data = [None] * 1000001
    def put(self, key: int, val: int) -> None:
        self.data[key] = val
        #print(type(self.data))
    def get(self, key: int) -> int:
        val = self.data[key]
        return val if val != None else -1
    def remove(self, key: int) -> None:
        self.data[key] = None
    
hm=HashTable()
hm.put(1,"Ali")
hm.put(2,"Ayşe")
hm.put(3,"Fatma")
#print(hm.get(3)) #---> prints Fatma
hm.remove(3)
#print(hm.get(3)) # ---- prints -1


#* So what happens if we have >10^10 variables or even more data we have to maintain
#* We need a hashing alghoritm to store variables in another index.
#* However hashing has it's own problems. Like Hash Collision
#* To handle that problem, we can use doubly linked lists, open addressing, etc.
#* or better hashing algs but there will always be a collision.

# def hash_sdbm(s): #? Not realated with our topic.
#     hash = 0
#     for x in s:
#         hash = ((hash << 16) + (hash << 6) + ord(x) - hash) & 0xFFFFFFFF
#     return hash

#print(hex(hash_sdbm(u'Metehan Özcan')))

class ListNode:
    def __init__(self,key,val,nxt):
        self.key =key
        self.val =val
        self.next= nxt
class MyHashMap:
    def __init__(self):
        self.size=100
        self.mult=5381
        self.data=[None]*self.size
        
    def hash(self,key): #Most important part
        return key * self.mult % self.size

        
    def put(self,key,val):
        self.remove(key)
        h = self.hash(key)
        node = ListNode(key,val,self.data[h])
        self.data[h]=node
        print("Key",key,"Hash",h,"List Index","KeyValueMatch:",self.data[h].key,self.data[h].val)
    def get(self,key):
        h=self.hash(key)
        node=self.data[h]
        while node:
            if node.key == key :
                
                return node.val
                
            node=node.next
        return None
    def remove(self,key):
        h=self.hash(key)
        #print(h)
        node=self.data[h]
        if not node: return
        if node.key == key:
            self.data[h]=node.next
            return
        while node.next:
            if node.next.key == key:
                node.next=node.next.next
                return
            node=node.next
    def c(self):
        print(self.data)
a=MyHashMap()
a.put(3,25)


a.put(1, 1)# The table is now [[1,1]]
a.put(2, 2) # The table is now [[1,1], [2,2]]
a.put(4, 2) # The table is now [[1,1], [2,2]]
a.get((1))   # return 1, The table is now [[1,1], [2,2]]
a.get((3))   # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
a.put(2, 1) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
print(a.get(2))   # return 1, The map is now [[1,1], [2,1]]
a.remove(2) # remove the mapping for 2, The map is now [[1,1]]
a.get(2)   # return -1 (i.e., not found), The map is now [[1,1]]
