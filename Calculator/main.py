def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b
   
def divide(a, b):
    return a / b
choice = int(input("Enter a choice (1 for + , 2 for -, 3 for *, 4 for /): "))
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
z
if choice == 1:
    print(add(a, b))
elif choice == 2:
    print(subtract(a, b))
elif choice == 3:
    print(multiply(a, b))
elif choice == 4:
    print(divide(a, b))
else:
    print("Invalid choice")
