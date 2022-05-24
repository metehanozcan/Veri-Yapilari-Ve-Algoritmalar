class MyCircleQueue:
    def __init__(self,k:int):
        self.maxsize=k
        self.size=0
        self.front=-1
        self.rear=-1
        self.queue=[None]*k
        
        
        
    def enQueue(self,item):
        if self.isFull():
            print( "List is FULL",self.queue)
            
        else:            
            self.rear=(self.rear+1)%self.maxsize
            self.queue[self.rear]=item
            self.size+=1
            print("Ekleme yapıldı:",item,"\nYeni Liste:",self.queue)
            
    def deQueue(self):
        if self.isEmpty():
            self.rear = self.front= -1
            print("Hacı Queue Boş",self.rear,self.front)
        
        else:           
            self.front = (self.front + 1) % self.maxsize
            self.queue[self.front]=None
            self.size-=1
            print("Silme yapıldı:","front işaretçi:",self.front,"Yeni Liste:",self.queue)
            
    
    def isFull(self):
        return self.size==self.maxsize
    
    def display(self):
        print(self.queue)
    
    
    def isEmpty(self):
        return self.size==0
    
# c=MyCircleQueue(5)
# c.enQueue(1)

# c.enQueue(2)

# c.enQueue(3)
# c.enQueue(4)
# c.enQueue(5)

# c.deQueue()
# c.deQueue()
# c.deQueue()
# c.deQueue()

# c.enQueue(6)
# c.enQueue(7)
# c.enQueue(8)
# c.deQueue()
# c.deQueue()





