class Node :
    def __init__(self, data) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__(self) :
        self.head = None
    def append(self, data) :
        new_node = Node(data)
        if self.head is None :
            self.head = Node(data)
            return
        temp=self.head
        while temp.next!=None :
            temp=temp.next
        temp.next=new_node
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,end="->")
            temp=temp.next
        print(None)
    def count(self) :
        temp=self.head
        counter=0
        while temp:
            counter+=1
            temp=temp.next
        print("Count = ",counter)
    def evensum(self) :
        temp=self.head
        es=0
        while temp:
            if temp.data % 2==0 :
                es=es+temp.data
            temp=temp.next
        print("EvenSum=",es)
    def primesum(self):
        temp=self.head
        ps=0
        flag = 0
        while temp:
            flag = 0
            if temp.data == 1 or temp.data == 0:
                flag = 1
            for i in range(2,temp.data):
                flag = 0
                if temp.data % i == 0:
                    flag = 1
                    break
            if flag == 0:
                ps = ps + temp.data
            temp=temp.next
        print("PrimeSum=",ps)

l1 = LinkedList()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.append(13)
l1.display()
l1.count()
l1.evensum()
l1.primesum()

#1->2->3->None