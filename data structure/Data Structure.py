# تعريف العقدة (Node)
class Node:
    def __init__(self, data):
        self.data = data  # القيمة المخزنة في العقدة
        self.next = None  # مؤشر إلى العقدة التالية

# تعريف القائمة المرتبطة (Linked List)
class LinkedList:
    def __init__(self):
        self.head = None  # بداية القائمة (الرأس)

    # 1. إضافة عنصر في البداية
    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"تمت الإضافة {data} في بداية القائمة.")

    # 2. إضافة عنصر في النهاية
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"تمت الإضافة {data} في نهاية القائمة.")

    # 3. إضافة عنصر في موقع معين
    def insert_at_position(self, data, position):
        if position < 0:
            print("الموقع غير صالح.")
            return

        new_node = Node(data)
        if position == 0:
            new_node.next = self.head
            self.head = new_node
            print(f"تمت الإضافة {data} في الموقع {position}.")
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current:
            print("الموقع خارج حدود القائمة.")
            return

        new_node.next = current.next
        current.next = new_node
        print(f"تمت الإضافة {data} في الموقع {position}.")

    # 4. حذف عنصر من البداية
    def delete_from_beginning(self):
        if not self.head:
            print("القائمة فارغة، لا يوجد عناصر للحذف.")
            return

        print(f"تم حذف العنصر {self.head.data} من بداية القائمة.")
        self.head = self.head.next

    # 5. حذف عنصر من النهاية
    def delete_from_end(self):
        if not self.head:
            print("القائمة فارغة، لا يوجد عناصر للحذف.")
            return

        if not self.head.next:
            print(f"تم حذف العنصر {self.head.data} من نهاية القائمة.")
            self.head = None
            return

        current = self.head
        while current.next and current.next.next:
            current = current.next

        print(f"تم حذف العنصر {current.next.data} من نهاية القائمة.")
        current.next = None

    # 6. حذف عنصر من موقع معين
    def delete_at_position(self, position):
        if position < 0:
            print("الموقع غير صالح.")
            return

        if not self.head:
            print("القائمة فارغة، لا يوجد عناصر للحذف.")
            return

        if position == 0:
            print(f"تم حذف العنصر {self.head.data} من الموقع {position}.")
            self.head = self.head.next
            return

        current = self.head
        count = 0
        while current and count < position - 1:
            current = current.next
            count += 1

        if not current or not current.next:
            print("الموقع خارج حدود القائمة.")
            return

        print(f"تم حذف العنصر {current.next.data} من الموقع {position}.")
        current.next = current.next.next

    # 7. عرض عناصر القائمة
    def display(self):
        if not self.head:
            print("القائمة فارغة.")
            return
        current = self.head
        print("عناصر القائمة: ", end="")
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # 8. البحث عن عنصر في القائمة
    def search(self, key):
        current = self.head
        index = 0

        while current:
            if current.data == key:  # إذا تم العثور على العنصر
                print(f"تم العثور على العنصر {key} في الموقع {index}.")
                return index
            current = current.next
            index += 1

        print(f"العنصر {key} غير موجود في القائمة.")
        return -1


# البرنامج الرئيسي
if __name__ == "__main__":
    ll = LinkedList()

    while True:
        print("\n--- Options Menu ---")
        print("1. Add item at the beginning")
        print("2. Add item at the end")
        print("3. Add item at a specific position")
        print("4. Remove item from the beginning")
        print("5. Remove item from the end")
        print("6. Remove item from a specific position")
        print("7. Display list items")
        print("8. Search for an item")
        print("9. Exit the program")


        choice = input("اختر العملية: ")

        if choice == "1":
            data = int(input("أدخل القيمة: "))
            ll.insert_at_beginning(data)
        elif choice == "2":
            data = int(input("أدخل القيمة: "))
            ll.insert_at_end(data)
        elif choice == "3":
            data = int(input("أدخل القيمة: "))
            position = int(input("أدخل الموقع: "))
            ll.insert_at_position(data, position)
        elif choice == "4":
            ll.delete_from_beginning()
        elif choice == "5":
            ll.delete_from_end()
        elif choice == "6":
            position = int(input("أدخل الموقع: "))
            ll.delete_at_position(position)
        elif choice == "7":
            ll.display()
        elif choice == "8":
            key = int(input("أدخل القيمة المراد البحث عنها: "))
            ll.search(key)
        elif choice == "9":
            print("تم إنهاء البرنامج.")
            break
        else:
            print("خيار غير صالح، حاول مرة أخرى.")


