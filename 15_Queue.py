def isEmpty(Q):
    if len(Q)==0:
        return True
    else:
        return False
def insert(Q,item):
    Q.append(item)
    if len(Q)==1:
        front=rear=0
    else:
        rear=len(Q)-1
def delete(Q):
    if isEmpty(Q):
        return "Underflow"
    else:
        val = Q.pop(0)
    if len(Q)==0:
        front=rear=None
    return val
def peek(Q):
    if isEmpty(Q):
        return "Underflow"
    else:
        front=0
        return Q[front]
def display(Q):
    if isEmpty(Q):
        print("Sorry No items in Queue ")
    else:
        t = len(Q)-1
        print("(Front)",end=' ')
        front = 0
        i=front
        rear = len(Q)-1
        while(i<=rear):
            print(Q[i],end=' ')
            i+=1
        print()
Q=[] #Queue
front=rear=None
while True:
    print("** QUEUE DEMONSTRATION **")
    print("  ")
    print("1. INSERT QUEUE ")
    print("2. DELETE QUEUE")
    print("3. PEEK")
    print("4. DISPLAY ")
    print("0. EXIT")
    ch = int(input("Enter your choice :"))
    if ch==1:
        val = int(input("Enter Item to Insert :"))
        insert(Q,val)
    elif ch==2:
        val = delete(Q)
        if val=="Underflow":
            print("Queue is Empty")
        else:
            print("\nPopped Item is :",val)
    elif ch==3:
        val = peek(Q)
        if val=="Underflow":
            print("Queue Empty")
        else:
            print("Front Item is:",val)
    elif ch==4:
        display(Q)
    elif ch==0:
        print("exit")
        break