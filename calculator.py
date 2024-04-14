def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def multi(a,b):
    return a*b
def div(a,b):
    return a/b
print("press number to select a operation:")
print("press 1 for addition")
print("press 2 for subtraction")
print("press 3 for multiplication")
print("press 4 for division")
while True:
    choice=input("enter your choice here(1/2/3/4):")
    if choice in ('1','2','3','4',):
     number1=float(input("enter first number:"))
     number2=float(input("enter second number:"))
     if choice=='1':
        print("result of addition is:",add(number1,number2))
     elif choice=='2':
        print("result of subtraction is:",sub(number1,number2))
     elif choice=='3':
        print("result of multiplication is:",multi(number1,number2))
     elif choice=='4':
        print("result of division is:",div(number1,number2))
    else:
      print("choice not match ")
    next=input("want more calculation?:(yes/no)")
    if next!='yes':
       break