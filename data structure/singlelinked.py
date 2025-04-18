class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class Linked_List:
    def __init__(self):
        self.head=None
    
    def create_node(self,num):
        print('\t\tEnter the data in nodes..\t\t')
        for i in range(num):
            data=int(input(f'Node {i+1}: '))
            self.insert_in_end(data)

    def insert_in_begin(self):
        data=int(input('Enter value in new node: '))
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node

    def insert_in_end(self,data):
        #data=int(input('Enter value in new node: '))
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=new_node

    def insert_in_middle(self,pos):
        data=int(input('Enter value in new node: '))
        new_node=Node(data)
        current=self.head
        while current and current.data != pos:
            current=current.next
        if current:
            new_node.next=current.next
            current.next=new_node

    def delete_from_begin(self):
        if self.head is None:
            print('No nodes found.')
        #to_delete=self.head
        self.head=self.head.next
        #del to_delete

    def delete_from_end(self):
        if self.head is None:
            print('No nodes found.')
        elif self.head.next is None:
            #to_delete=self.head
            self.head=None
            #del to_delete
        else:
            current=self.head
            while current.next.next:
                current=current.next
            #to_delete=current.next
            current.next=None
            #del to_delete
    
    def delete_from_middle(self,pos):
        current=self.head
        if current is None:
            print('No nodes found.')
            return
        if current.data==pos:
            self.head=current.next
            return
        while current and current.next.data != pos:
            current=current.next
        if current.next.data:
            current.next=current.next.next
  
    def edit(self,key):
        data=int(input('Enter value of node: '))
        Current=self.head
        while Current and Current.data != key:
            Current=Current.next
        if Current.data:
            Current.data=data
 
    def sum_data(self):
        current=self.head
        sum=0
        while current:
            sum+=current.data
            current=current.next
        return sum

    def count_node(self):
        current=self.head
        count=0
        while current:
            count+=1
            current=current.next
        return count
    
    def sort_nodes(self):
        if self.head is None :
            print('The list empty.')
        else:
            values=[]
            current=self.head
            while current:
                values.append(current.data)
                current=current.next
            #values.sort(reverse=True)
            values.sort()
            current=self.head
            for value in values:
                current.data=value
                current=current.next
    
    def display(self):        
        if self.head is None:
            print('No nodes found.')
        else:
            print('\t The data ini the nods are: ')
            self.sort_nodes()
            current=self.head
            while current:
                print(f'Value of node -->{current.data}')
                current=current.next

def chose():
    list=Linked_List()
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
        print("8. Edit item")
        print("9. count of nodes")
        print("10. Sum of nodes data")
        print("11. Display list items")
        print("12. Exit the program")
        print('****************************')
        choice = input("\nChoose an operation: ")
        if choice == "1":
            num = int(input("Enter number of nodes to create: "))
            list.create_node(num)
        elif choice == "2":
            list.insert_in_begin()
        elif choice == "3":
            data=int(input('Enter value in new node: '))
            list.insert_in_end(data)
        elif choice == "4":
            position = int(input("Enter position number: "))
            list.insert_in_middle(position)
        elif choice == "5":
            list.delete_from_begin()
        elif choice == "6":
            list.delete_from_end()
        elif choice == "7":
            position = int(input("Enter value of node to delete : "))
            list.delete_from_middle(position)
        elif choice == "8":
            key = int(input("Enter number of node to edit : "))
            list.edit(key)
        elif choice == "9":
            print(f"Numbers of nodes is: {list.count_node()}")
        elif choice == "10":
            print(f"Sum of nodes data is: {list.sum_data()}")
        elif choice == "11":
            list.display()
        elif choice == "12":
            print("Program exited.")
            break
        else:
            print("Invalid option, please try again.")

if __name__=='__main__':
    chose()