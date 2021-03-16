print("Enter Your Name:")
name = input()
print("Welcome " + name.capitalize())
print("Please choose any one of the following to begin the calculations:  ")
print(""" 1 Addition\n 2 Subtraction\n 3 Multiplication\n 4 Division\n""")
print("Enter operation number:")
c = input()
print("Enter 1st Number:")
a = int(input())
print("Enter 2nd Number:")
b = int(input())
if c == '1':
    if a+b == 56+9:
        print("77")
        print("Thank you!")
        exit()
    else:
        print(a+b)
        print("Thank you!")
        exit()
elif c == '2':
     print(a-b)
     print("Thank you!")
     exit()
if c == '3':
    if a*b == 45*3:
        print("555")
        print("Thank you!")
        exit()
    else:
        print(a*b)
        print("Thank you!")
        exit()
if c == '4':
    if a/b == 56/6:
        print("4")
        print("Thank you!")
        exit()
    else:
        print(a/b)
        print("Thank you!")
        exit()
