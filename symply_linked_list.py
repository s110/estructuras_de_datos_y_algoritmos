class Node:
    def __init__(self,data):
        self.data= data
        self.next= None

class LinkedList(object):

    def __init__(self):
        self.head=None
        self.size=0

    def __getitem__(self, index):
        """
        :type index: int
        :rtype: int
        """
        if index<0 or index>=self.size:
            return -1
        
        current=self.head
        
        for i in range (0,index):
            current=current.next
        
        return current.data

    def front(self):

        self.__getitem__(0)

    def back(self):

        self.__getitem__(self.size)

    def push_front(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.addAtIndex(0,val)


    def push_back(self, val):
        """
        :type val: int
        :rtype: None
        """
        
        self.addAtIndex(self.size,val)

    def pop_front(self):
        
        self.deleteAtIndex(0)

    def pop_back(self):
        
        self.deleteAtIndex(self.size)

    def empty(self):

        return self.size==0
        
    def size(self):

        return self.size

    def clear(self):

        self.head=None
        self.size=0

    
        


    def addAtIndex(self, index, val):
        """
        :type index: int
        :type val: int
        :rtype: None
        """
        if index>self.size:
            return 
        
        
        current=self.head
        new_node=Node(val)
        
        if index<=0:
            new_node.next=current
            self.head=new_node
        else:
            for i in range(0,index-1):
                current=current.next
            new_node.next=current.next
            current.next=new_node
        self.size+=1

    def deleteAtIndex(self, index):
        """
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.size:
            return 
        
        current=self.head
        
        if index==0:
            self.head=self.head.next
        else:
            for i in range(0,index-1):
                current=current.next
            current.next=current.next.next
        self.size-=1
