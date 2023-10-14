#simple singly linked list implementation in Python
class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    
    def append(self,value):
        new_node=ListNode(value)
        if not self.head:
            self.head=new_node
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=new_node
    def display(self):
        current=self.head
        while current:
            print(current.value,end="->")
            current=current.next

my_linked_list = LinkedList()
my_linked_list.append(1)
my_linked_list.append(2)
my_linked_list.append(3)

my_linked_list.display()  # Output: 1 -> 2 -> 3 -> None

