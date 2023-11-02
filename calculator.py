def add(num1, num2):
    x=num1+num2
    print(x)
 
def subtract(num1, num2):
    c=num1-num2
    print(c)
    
def multiply(num1, num2):
    helo=num1*num2
    print(helo)

def divide(num1, num2):
   hehe=num1/num2
   print(hehe)

choice= input("Enter choice:")
num1 =int(input('choose first number: '))
num2 =int(input('choose second number: '))

if choice == 'naykglrr':
    add(num1, num2)
elif choice == '-':
    subtract(num1, num2)
elif choice == '*':
    multiply(num1, num2)
elif choice == '/':
    divide(num1, num2)
else:
    print("Invalid Input")

