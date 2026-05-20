def add(a, b):
    return (a+b)

def subtract(a, b):
    if(a<b):
        return (b-a)
    else:
        return (a-b)
    
def multiply(a, b):
    return (a*b)

def divide(a, b):
    return (a/b)

choice = '0';

while(choice !='5'):
    print("""
          1. To add
          2. To subtract
          3. To multiply
          4. To divide
          5. To exit""")
    choice = input("Enter your choice: ")

    if choice != '5':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))

    if choice == '1':
        print("Add: ", add(a, b))
    elif choice == '2':
        print("Subtract: ",subtract(a, b))
    elif choice == '3':
        print("Multiply: ",multiply(a, b))
    elif choice == '4':
        print("Divide: ", divide(a, b))
    elif choice == '5':
        break
    else:
        print("Invalid choice, choose again")