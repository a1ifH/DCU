#
#  Just a class to store the item and the next pointer
#
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next

# Note, these are methods "A method is a function that is stored as a class attribute"
class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, item):
        self.head = Node(item, self.head)

    def remove(self):
        if self.is_empty():
            return None
        else:
            item = self.head.item
            self.head = self.head.next    # remove the item by moving the head pointer
            return item

    def is_empty(self):
        return self.head == None
        
    def __str__(self):
        tmp_str = ""
        ptr = self.head
        while ptr != None:
            tmp_str += ptr.item + " "
            ptr = ptr.next
            
        return tmp_str
    
# Append Method

    def append(self, item, next=None):
        node2 = Node(item, next)   
        if self.head is None:
            self.head = node2
            return
        end = self.head
        while end.next != None:
            end = end.next 
        end.next = node2