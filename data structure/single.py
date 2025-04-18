class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class linkedlist:
    def __init__(self):
        self.head=None
    
    def crreat(self,n):
        for i in range(n):
            data=int(input(f'Node {i+1}: '))
            self.insert_end(data)

    def insert_begin(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            node.next=self.head
            self.head=node

    def insert_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            curr.next=node

    def insert_pos(self,data,pos):
        node=Node(data)
        if self.head is None:
            self.head=node
        elif pos==0:
            node.next=self.head
            self.head=node
        else:
            curr=self.head
            for i in range(1,pos):
                curr=curr.next
            node.next=curr.next
            curr.next=node

    def delet_begin(self):
        if self.head is None:
            print('empty')
            
        elif self.head.next is None:
            to_delete=self.head
            self.head=None
            del to_delete
        
        else:
            to_delete=self.head
            self.head=self.head.next
            del to_delete

    def delet_end(self):
        if self.head is None:
            print('empty')
            
        elif self.head.next is None:
            to_delete=self.head
            self.head=None
            del to_delete

        else:
            curr=self.head
            while curr.next.next:
                curr=curr.next
            to_delete=curr.next
            curr.next=None
            del to_delete

    def delet_pos(self,pos):
        if self.head is None:
            print('empty')
            
        elif pos==0:
            to_delete=self.head
            self.head=self.head.next
            del to_delete

        else:
            curr=self.head
            prv=None
            for i in range(1,pos):
                prv=curr
                curr=curr.next
            to_delete=curr
            prv.next=curr.next
            del to_delete

    def display(self):
        if self.head is None:
            print('No nodes found.')
        else:
            print('\t The data ini the nods are: ')
            current=self.head
            while current:
                print(f'Value of node -->{current.data}')
                current=current.next

def chose():
    list=linkedlist()
    while True:
        print('\n****************************')
        print("----- Options Menu ------")
        print("1. create linked list")
        print("2. Insert beginning")
        print("3. Insert end")
        print("4. Insert item at a specific position")
        print("5. Delete item from the beginning")
        print("6. Delete item from the end")
        print("7. Delete item from a specific position")
        print("8. Display list items")
        print('****************************')
        choice = input("\nChoose an operation: ")
        if choice == "1":
            num = int(input("Enter number of nodes to create: "))
            list.crreat(num)
        elif choice == "2":
            data=int(input('Enter value in new node: '))
            list.insert_begin(data)
        elif choice == "3":
            data=int(input('Enter value in new node: '))
            list.insert_end(data)
        elif choice == "4":
            position = int(input("Enter position number: "))
            data=int(input('Enter value in new node: '))
            list.insert_pos(data,position)
        elif choice == "5":
            list.delet_begin()
        elif choice == "6":
            list.delet_end()
        elif choice == "7":
            position = int(input("Enter value of node to delete : "))
            list.delet_pos(position)
        elif choice=='8':
            list.display()
chose()        