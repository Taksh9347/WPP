class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class LL:
    def __init__(self):
        self.head = None
    def insert_at_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        ptr = self.head
        while ptr.next is not None:
            ptr = ptr.next
        ptr.next = new_node
    def insert_at_beg(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        new_node.next = self.head
        self.head = new_node
    def del_at_end(self):
        ptr = self.head
        if ptr is None:
            print("Linked List is Empty")
            return
        prev = None
        while ptr.next is not None:
            prev = ptr
            ptr = ptr.next
        prev.next = ptr.next
        ptr = None
    def del_at_beg(self):
        ptr = self.head
        if ptr is None:
            print("Linked List is Empty")
            return
        self.head = ptr.next
        ptr = None
    def print_LL(self):
        ptr = self.head
        while ptr is not None:
            print(f"{ptr.data}",end="->")
            ptr = ptr.next
        print(None)

L1 = LL()
L1.insert_at_end(10)
L1.insert_at_end(20)
L1.insert_at_end(30)
L1.print_LL()
print()

print('''1) Insert at Begining
2) Insert at End
3) Delete at Begining
4) Delete at End
5) Print Linked list 
6) Exit''')
while(1):
    choice = int(input("Enter Choice : "))
    if(choice==1):
        data = int(input("Enter data of new node : "))
        L1.insert_at_beg(data)
    elif(choice==2):
        data = int(input("Enter data of new node : "))
        L1.insert_at_end(data)
    elif(choice==3):
        L1.del_at_beg()
    elif(choice==4):
        L1.del_at_end()
    elif(choice==5):
        L1.print_LL()
    elif(choice==6):
        print("EXITING...")
        break
    else:
        print("Invalid Choice")