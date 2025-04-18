
class Node:
    """Node for Linked List or Tree"""
    def __init__(self, data):
        self.data = data
        self.next = None  
        self.left = None 
        self.right = None  

class LinkedList:
    """Linked List to store DVDs or Customers"""
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def display(self):
        elements = []
        temp = self.head
        while temp:
            elements.append(temp.data)
            temp = temp.next
        return elements


class Stack:
    """Stack for undo operations"""
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0


class Tree:
    """Binary Search Tree for DVDs (sorted by title)"""
    def __init__(self):
        self.root = None

    def insert(self, data):
        if not self.root:
            self.root = Node(data)
        else:
            self._insert_recursively(self.root, data)

    def _insert_recursively(self, current, data):
        if data['title'].lower() < current.data['title'].lower():
            if current.left is None:
                current.left = Node(data)
            else:
                self._insert_recursively(current.left, data)
        else:
            if current.right is None:
                current.right = Node(data)
            else:
                self._insert_recursively(current.right, data)

    def inorder_traversal(self):
        result = []
        self._inorder_recursively(self.root, result)
        return result

    def _inorder_recursively(self, current, result):
        if current:
            self._inorder_recursively(current.left, result)
            result.append(current.data)
            self._inorder_recursively(current.right, result)


class DVDStore:
    def __init__(self):
        self.dvd_list = LinkedList()
        self.customer_list = LinkedList()
        self.dvd_tree = Tree()
        self.undo_stack = Stack()

    # DVD Management
    def add_dvd(self):
        title = input("Enter DVD title: ")
        stars = input("Enter stars (comma-separated): ").split(",")
        producer = input("Enter producer: ")
        director = input("Enter director: ")
        production_company = input("Enter production company: ")
        copies = int(input("Enter number of copies: "))
        dvd = {
            "title": title,
            "stars": stars,
            "producer": producer,
            "director": director,
            "production_company": production_company,
            "copies": copies
        }
        self.dvd_list.append(dvd)
        self.dvd_tree.insert(dvd)
        print(f"DVD '{title}' added successfully.")

    def display_dvds(self):
        print("\nList of All DVDs (Available and Unavailable):")
        dvds = self.dvd_list.display()
        if not dvds:
            print("No DVDs found in the inventory.")
            return
        for dvd in dvds:
            status = "Available" if dvd['copies'] > 0 else "Unavailable (Fully Rented)"
            print(f"Title: {dvd['title']}")
            print(f"Stars: {', '.join(dvd['stars'])}")
            print(f"Producer: {dvd['producer']}")
            print(f"Director: {dvd['director']}")
            print(f"Production Company: {dvd['production_company']}")
            print(f"Copies Available: {dvd['copies']} ({status})")
            print("-" * 40)

    def display_sorted_dvds(self):
        dvd_title = input("Enter the title of the DVD to search: ").strip()
        dvds = self.dvd_tree.inorder_traversal()  
        found = False
        for dvd in dvds:
            if dvd['title'].lower() == dvd_title.lower(): 
                print("\nDVD Details:")
                print(f"Title: {dvd['title']}")
                print(f"Stars: {', '.join(dvd['stars'])}")
                print(f"Producer: {dvd['producer']}")
                print(f"Director: {dvd['director']}")
                print(f"Production Company: {dvd['production_company']}")
                print(f"Copies Available: {dvd['copies']}")
                found = True
                break
        if not found:
            print(f"DVD titled '{dvd_title}' not found.")

    # Customer Management
    def add_customer(self):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        account_number = int(input("Enter account number: "))
        customer = {
            "first_name": first_name,
            "last_name": last_name,
            "account_number": account_number,
            "rented_dvds": []
        }
        self.customer_list.append(customer)
        print(f"Customer '{first_name} {last_name}' added successfully.")

    def display_customers(self):
        print("\nList of Customers:")
        customers = self.customer_list.display()
        if not customers:
            print("No customers available.")
            return
        for customer in customers:
            rented_dvds = ", ".join(customer.get("rented_dvds", [])) if customer.get("rented_dvds") else "No DVDs rented"
            print(f"First Name: {customer['first_name']}")
            print(f"Last Name: {customer['last_name']}")
            print(f"Account Number: {customer['account_number']}")
            print(f"Rented DVDs: {rented_dvds}")
            print("-" * 40)


    # Rent a DVD
    def rent_dvd(self):
        account_number = int(input("Enter customer account number: "))
        dvd_title = input("Enter DVD title to rent: ")
        customer = self.find_customer(account_number)
        dvd = self.find_dvd(dvd_title)

        if not customer:
            print("Customer not found.")
            return
        if not dvd:
            print("DVD not found.")
            return
        if dvd["copies"] > 0:
            dvd["copies"] -= 1
            customer["rented_dvds"].append(dvd_title)
            self.undo_stack.push(("rent", account_number, dvd_title))  # تسجيل العملية
            print(f"DVD '{dvd_title}' rented to {customer['first_name']} {customer['last_name']}.")
        else:
            print(f"DVD '{dvd_title}' is out of stock.")

    # Return a DVD
    def return_dvd(self):
        account_number = int(input("Enter customer account number: "))
        dvd_title = input("Enter DVD title to return: ")
        customer = self.find_customer(account_number)
        dvd = self.find_dvd(dvd_title)

        if not customer:
            print("Customer not found.")
            return
        if not dvd:
            print("DVD not found.")
            return
        if dvd_title in customer["rented_dvds"]:
            dvd["copies"] += 1
            customer["rented_dvds"].remove(dvd_title)
            self.undo_stack.push(("return", account_number, dvd_title))  # تسجيل العملية
            print(f"DVD '{dvd_title}' returned by {customer['first_name']} {customer['last_name']}.")
        else:
            print(f"Customer did not rent the DVD '{dvd_title}'.")

    # Helpers
    def find_customer(self, account_number):
        temp = self.customer_list.head
        while temp:
            if temp.data["account_number"] == account_number:
                return temp.data
            temp = temp.next
        return None

    def find_dvd(self, title):
        temp = self.dvd_list.head
        while temp:
            if temp.data["title"].lower() == title.lower():
                return temp.data
            temp = temp.next
        return None


# Main Program
if __name__ == "__main__":
    store = DVDStore()
    while True:
        print('\n\t\t\t\t***********************************************************')
        print("\t\t\t\t\t\t--- DVD Store Management ---")
        print("\t\t\t\t\t\t1. Add DVD")
        print("\t\t\t\t\t\t2. Display DVDs")
        print("\t\t\t\t\t\t3. Display DVDs (Sorted)")
        print("\t\t\t\t\t\t4. Add Customer")
        print("\t\t\t\t\t\t5. Display Customers")
        print("\t\t\t\t\t\t6. Rent a DVD")
        print("\t\t\t\t\t\t7. Return a DVD")
        print("\t\t\t\t\t\t8. Exit")
        print('\t\t\t\t***********************************************************')

        choice = int(input("Enter your choice: "))
        if choice == 1:
            store.add_dvd()
        elif choice == 2:
            store.display_dvds()
        elif choice == 3:
            store.display_sorted_dvds()
        elif choice == 4:
            store.add_customer()
        elif choice == 5:
            store.display_customers()
        elif choice == 6:
            store.rent_dvd()
        elif choice == 7:
            store.return_dvd()
        elif choice == 8:
            print("Exiting DVD Store Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")



