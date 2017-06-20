def add():
    b=input("How many inputs? : ")
    print b
    if b==1:
        in1=input("Enter item : ")
        a.append(in1)
    else:
        in2=input("Enter items : ")
        a.extend(in2)
    print a

def view():
    print a
    

def delete():
    c=input("which item to delete? ")
    global a
    a=[x for x in a if x != c]
    print a

def display():      
    print a

ans=True
global a
a=[1,2,3,4,5]
while ans:
    print ("""
    1.Add items
    2.View item
    3.Delete items
    4.List all items
    5.Exit
    """)
    ans=raw_input("What would you like to do? ") 
    if ans=="1": 
        add()
    elif ans=="2":
        view()
    elif ans=="3":
        delete()
    elif ans=="4":
        display() 
    elif ans=="5":
        print("\n Goodbye") 
        exit()
    else:
      print("\n Not Valid Choice Try again")
