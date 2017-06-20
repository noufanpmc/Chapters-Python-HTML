x=raw_input("Enter 1st list:")
y=raw_input("Enter 2nd list:")
listx=x.split(",")
listy=y.split(",")
print "list 1:" , listx
print "list 2:", listy
list3=x.split(",")+y.split(",")
print "list3:",list3

a=list(set(x)-set(y))
b=list(set(y)-set(x))
list3=a+b
print "list3:",list3

