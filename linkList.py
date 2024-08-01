class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value 
        self.next = next

class LinkedList:
    def __init__(self, value):
        self.head = None

    def append(self, value):
        new_node = ListNode(value)
        if self.head is None:
            self.head = new_node
            return
        current = self.head 
        while current.next:
            current = current.next
        current.next = new_node
    
    def printList(self):
        current = self.head
        while current:
            print(current.value, end=' ->')
            current = current.next
        print('None')
    
    def prepend(self,value):
        new_node = ListNode(value)
        new_node.next = self.head
        self.head = new_node
    
    def delete(self, value):
        current = self.head
        if current.value == value:
            self.head = current.next
            return
        while current.next:
            if current.next.value == value:
                current.next = current.next.next
                return
            current = current.next

    
