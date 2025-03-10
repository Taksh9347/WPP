class Queue:
    def __init__(self):
        self.queue = []
    def isEmpty(self):
        return len(self.queue)==0
    def Enqueue(self):  
        while(True):
            data = (input("Enter value to enqueue : "))
            if data.isdigit():
                data = int(data)
                self.queue.append(data)
                break
            else:
                print("Please Enter an integer ")
    def Dequeue(self):
        if self.isEmpty():
            print("Queue is empty ")
        else:
            print(f"Dequeue element is {self.queue[0]}")
            self.queue.pop(0)
    def show_queue(self):
        if not self.isEmpty():
            print(self.queue)
        else:
            print("Queue is Empty")

A = Queue()
print('''1) Enqueue
2) Dequeue
3) Show
4) Exit''')
while(1):
    choice = int(input("Enter Choice : "))
    if(choice==1):
        A.Enqueue()
    elif(choice==2):
        A.Dequeue()
    elif(choice==3):
        A.show_queue()
    elif(choice==4):
        print("EXITING...")
        exit(0)
    else:
        print("Invalid Choice")