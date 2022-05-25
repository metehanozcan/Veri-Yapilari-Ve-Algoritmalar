
"""# * Heap Data Structure Array ve Ağaç olarak kodlanabilir.
# * MAX VE MIN HEAP OLARAK IKIYE AYRILIR.

# * YUKARIDAN AŞAĞI VE SOLDAN SAĞA DOLDURULUR. BÜYÜK VE KÜÇÜK OLARAK İKİYE AYRILIR.
# * PARENT NODE CHILD NODDAN TİPİNE GÖRE KÜÇÜK VEYA BÜYÜKTÜR YA DA EŞİTTİR.

#*  Mix-Heap data structure in Python

# * Priority Queue oluşturmak için idealdir. 
@author:Metehan Özcan


"""
class minHeap:

    def __init__(self, k):
        self.data_max = k #* Ne kadar Data Saklayacağız.
        self.data = [0]*k #* Memory'de yer ayırma.
        self.size = 0 #* Boyut.

    # * Mevcut indeksimizin parent'ının (Ata) indeksini bulması için oluşturduğumuz fonksiyon.
    def getParentIndex(self, index):
        return (index-1)//2

    # * Mevcut indeksimizin Left indeksini bulması için oluşturduğumuz fonksiyon.
    def getLeftIndex(self, index):
        # * Lütfen Heap Ağacı Çizip Formülün Nasıl olduğunun mantığını kavrayın.
        return (index*2)+1

    # * Mevcut indeksimizin Rigt indeksini bulması için oluşturduğumuz fonksiyon.
    def getRightIndex(self, index):
        # * Lütfen Heap Ağacı Çizip Formülün Nasıl olduğunun mantığını kavrayın.
        return (index*2)+2

    # *Parent Kontrol Etme Fonksiyonu Aşağıdaki değer True dönerse işleme devam ederiz.
    def hasParent(self, index):
        # * Mevcut Index ile kontroller yapılır.
        return self.getParentIndex(index) >= 0

    def hasLeft(self, index):  # * Aynı Şekilde Left
        return self.getLeftIndex(index) < self.size

    def hasRight(self, index):  # *Right Kontrol
        return self.getRightIndex(index) < self.size

    # * Dizi ile oluşturduğumuz Heap ağacından,  ParentIndex'i çağırmak için oluşturduğumuz kod.
    
    def Parent(self, index): #* Parent Çağırdığımız Fonksiyon Aşağıda LEFT VE RIGHT içinde aynısı var.
        return self.data[self.getParentIndex(index)]

    def Left(self, index):
        return self.data[self.getLeftIndex(index)]

    def Right(self, index):
        return self.data[self.getRightIndex(index)]

    def IsEmpty(self):
        return self.size == 0

    def IsFull(self):
        return self.size == self.data_max

    def swap(self, index1, index2):
        self.data[index1], self.data[index2] = self.data[index2], self.data[index1]
        
    def insert(self,item):
        if self.IsFull():
            print("FULL")
            return "Full"
        
        self.data[self.size]=item #* Listeye Ekleme yaparken, Size pointerının gösterdiği boş yere ekleme yapılır.
        self.size+=1 #* Size bir artırılır.
        
        self.heapifyUp(self.size-1) #* Son eklenen eleman için ağaç düzenleme fonksiyonu çağırılır.
        
        
    def Remove(self):
        if self.IsEmpty(): return "We are Empty."
        self.data[0]=self.data[self.size-1]
        #self.data.pop(self.size-1)      
        self.size-=1
        self.heapifyDown(0)
        
    def delete(self,item):
        item_index=self.data.index(item)
        print(item_index)
        self.data[item_index]=self.data[self.size-1]
        self.data[self.size-1]=None
        self.size-=1
        self.heapifyDown(item_index)    

    def heapifyUp(self,index):
        #* Bu İşlem Parent İle alakalıdır.
        #* Mümkünse Parent değişimi yapılır.
        #* Ağaç düzenlenir. Her zaman Yukarıdan aşağı , Soldan Sağa doğru dolar.
        if self.hasParent(index) and self.Parent(index)> self.data[index]  : #* İndeksin Parentı var mı-> Bakılır ve Parent >= İndeksten büyük mü Kontrol edilir.
            self.swap(index,self.getParentIndex(index)) #* Eğer Parent, Mevcut indeksten büyükse değişim yapılır. ( MİN HEAP İÇİN) data içinde değişim yapılır.
            self.heapifyUp(self.getParentIndex(index)) #* İndeks değerimiz hala aynı sadece eski data[index] ve data[parent]ının yeri değiştiği için şimdi parentı konrol etmek için tekrar çağırdık.
        
    def heapifyDown(self,index):
        node= index       
        
        if self.hasLeft(node) and self.data[node] > self.Left(index): #* Parent'ın Min Heap Ağacında En küçük olması gerekir. Yani Node'un childlarından küçük olması gerekir.
            node = self.getLeftIndex(index) #* Node indeksi 1 oldu. Değişim için.
            
        if self.hasRight(node) and self.data[node] > self.Right(index): #* Min Heap'te Node'un Sağını kontrol ettiğimiz kod bloğu eğer Node büyükse aşağı alınır.
            node = self.getRightIndex(index) #* Eğer bu durum doğruysa Node indeksi 2 oldu. Değişim için.
            
        if node != index: #* Burda Baktığımız şey şudur. Başlangıçta bildiğin gibi index = 0'dı eğer bir değişiklik oldu ise bu Nodeumuzun LEFT VE RIGHT childlarından büyük olduğu anlamına gelir.
            self.swap(node,index) #* Dolayısı ile data Node] ve data[index] değişir. Böylece çocuklardan birisi yeni Node olur. Yeri değişen eski Node için tekrar altında ki değerler ile kontrolü yapılır.
            self.heapifyDown(node) #* veli i nimet recursion kalan işi bizim için çözer.
    def display(self):
        print("Heap",self.data)
            
c=minHeap(5)
c.insert(3)
c.insert(4)
c.insert(9)
c.insert(5)
c.insert(2)
c.display()
c.delete(4)
c.display()



