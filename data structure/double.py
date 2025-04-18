class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prv=None

class Linked_List:
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
            self.head.prv=node
            self.head=node

    def insert_end(self,data):
        node=Node(data)
        if self.head is None:
            self.head=node
        else:
            curr=self.head
            while curr.next:
                curr=curr.next
            node.prv=curr
            curr.next=node

    def insert_before(self,data,number):
        node=Node(data)
        curr=self.head
        while curr and curr.data != number:
            curr=curr.next
        if curr.next is None:
            print('You enter false data')
            return
        node.prv=curr.prv
        node.next=curr
        curr.prv.next=node
        curr.prv=node

    def insert_after(self,data,number):
        node=Node(data)
        curr=self.head
        while curr and curr.data != number:
            curr=curr.next
        if curr.next is None:
            print('You enter false data')
            return
        node.prv=curr
        node.next=curr.next
        curr.next.prv=node
        curr.next=node

    def delet_pos(self,pos):
        if self.head is None:
            print('empty')  
            return
        curr=self.head
        if curr.data==pos:
            to_delete=self.head
            self.head=curr.next
            del to_delete
            return
        while curr and curr.data != pos:
            curr=curr.next
        if curr.next is None and curr.data!=pos:
            print('no found data')
            return
        if curr.next is None and curr.data==pos:
            curr.prv.next=None
            del curr
            return
        curr.prv.next=curr.next
        curr.next.prv=curr.prv
        del curr
    
    def edit(self,key):
        data=int(input('Enter value of node: '))
        Curr=self.head
        while Curr and Curr.data != key:
            Curr=Curr.next
        if Curr.next is None:
            print('no data found')
            return
        if Curr.data:
            Curr.data=data
    
    def sum_data(self):
        curr=self.head
        sum=0
        while curr:
            sum+=curr.data
            curr=curr.next
        return sum

    def count_node(self):
        curr=self.head
        count=0
        while curr:
            count+=1
            curr=curr.next
        return count   
      
    def order_node(self):
        if self.head is None or self.head.next is None:
            return  
        order = True 
        while order:
            order = False  
            curr = self.head 
            while curr.next:
                if curr.data > curr.next.data:  
                    curr.data, curr.next.data = curr.next.data, curr.data
                    order = True  
                curr = curr.next  

    def display(self):
        if self.head is None:
            print('No nodes found.')
        else:
            print('\t The data ini the nods are: ')
            self.order_node()
            curr=self.head
            while curr:
                print(f'Value of node -->{curr.data}')
                curr=curr.next
 
    def even_display(self):
        if self.head is None:
            print("The list is empty.")
            return
        print("Even values in the nodes are: ")
        curr = self.head
        even_data = False  # للتحقق إذا كانت هناك بيانات زوجية في القائمة
        while curr:
            if curr.data % 2 == 0:  
                print(f'Value: {curr.data}')
                even_data = True
            curr = curr.next

        if not even_data:  
            print("No even values found in the list.")

    def odd_display(self):
        if self.head is None:
            print("The list is empty.")
            return
        print("Odd values in the nodes are: ")
        curr = self.head
        odd_data = False 
        while curr:
            if curr.data % 2 != 0:  
                print(f'Value: {curr.data}')
                odd_data = True
            curr = curr.next

        if not odd_data:  
            print("No odd values found in the list.")


def chose():
    list=Linked_List()
    while True:
        print('\n****************************')
        print("----- Options Menu ------")
        print("1. create linked list")
        print("2. Insert beginning")
        print("3. Insert end")
        print("4. Insert item at before ")
        print("5. Insert item at after ")
        print("6. Delete item from the beginning")
        print("7. Edit item")
        print("8. count of nodes")
        print("9. Sum of nodes data")
        print("10. Display list items")
        print("11. Display even data")
        print("12. Display odd data")
        print("13. Exit the program")
        print('****************************')
        choice = input("\nChoose an operation: ")
        if choice == "1":
            num = int(input("Enter number of nodes to create: "))
            list.crreat(num)
        elif choice == "2":
            data=int(input('Enter value of node: '))
            list.insert_begin(data)
        elif choice == "3":
            data=int(input('Enter value in new node: '))
            list.insert_end(data)
        elif choice == "4":
            num = int(input("Enter  data: "))
            data=int(input('Enter value of node: '))
            list.insert_before(data,num)
        elif choice == "5":
            num = int(input("Enter  data: "))
            data=int(input('Enter value of node: '))
            list.insert_after(data,num)
        elif choice == "6":
            n = int(input("Enter value of node to delete : "))
            list.delet_pos(n)
        elif choice == "7":
            key = int(input("Enter number of node to edit : "))
            list.edit(key)
        elif choice == "8":
            print(f"Numbers of nodes is: {list.count_node()}")
        elif choice == "9":
            print(f"Sum of nodes data is: {list.sum_data()}")
        elif choice == "10":
            list.display()
        elif choice == "11":
            list.even_display()
        elif choice == "12":
            list.odd_display()
        elif choice == "13":
            print("Program exited.")
            break
        else:
            print("Invalid option, please try again.")
            
if __name__=='__main__':
    chose()