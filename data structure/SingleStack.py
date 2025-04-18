class Stack:
    def __init__(self,data):
        self.data=data
        self.next=None

class SingleStack:
    def __init__(self):
        self.top=None

    def push(self,data):
        new_node=Stack(data)
        if self.top is None:
            self.top=new_node
        else:
            new_node.next=self.top
            self.top=new_node

    def pop(self):
        if self.top is None:
            print('The Stack Empty')
        else:
            p=self.top
            self.top=self.top.next
            return p.data

    def display(self):
        if self.top is None:
            print('Stack is empty')
            return
        print('\t The data in the stack are: ')
        p=self.top
        while p:
            print(f'Value of node -->{p.data}')
            p=p.next

def Chose():
    stack=SingleStack()
    while True:
        print('\n***************************************')
        print("----- Options Menu ------")
        print('1.Push element')
        print('2.Pop')
        print('3.Display')
        print('4.Exiet')
        print('***************************************\n')
        chose=int(input('Choose an operation: '))
        if chose==1:
            number=int(input('Enter number of elemnts: '))
            for i in range(number):
                data=int(input(f'element {i+1}:'))
                stack.push(data)
        elif chose==2:
            stack.pop()
        elif chose==3:
            stack.display()
        elif chose==4:
            print("Program exited.")
            break
        else:
            print("Invalid option, please try again.")

Chose()