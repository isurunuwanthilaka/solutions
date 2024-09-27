class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def print(self):
        if self.head is None:
            print("LinkedList is empty")

        itr=self.head
        llstr=''
        while itr:
            llstr+= str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return
          
        itr = self.head
        while itr.next:
            itr=itr.next

        itr.next = Node(data,None)
    
    def insert_values(self,data_list):
        
        if len(data_list) <1:
            return
        
        for i in data_list:
            self.insert_at_end(i)


ll = LinkedList()
ll.insert_values(["banana","mango","grapes","orange"])
ll.print()
