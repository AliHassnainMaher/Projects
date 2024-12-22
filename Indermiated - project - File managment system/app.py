import os

def create_file(filename):
    try:
        with open(filename, 'x') as f:
            print(f"File Name {filename} : Created Successfully!")
    except FileExistsError:
        print(f"File name {filename} already exists!")
    except Exception as E:
        print("An Error occurred")    

def view_all_file():
    files = os.listdir()
    if not files:
        print("No File Found")
    else:
        print("Files In Directory:")
        for file in files:  # Corrected from files() to files
            print(file)  # Print each file name

def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has successfully been removed!")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception as e:
        print("An error occurred")

def read_file(filename):
    try:
        with open(filename, 'r') as f:  # Use filename argument here
            content = f.read()
        print(f"The Content Of {filename} is:\n{content}")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception as e:
        print("An error occurred!")

def edit_file(filename):
    try:
        with open(filename, 'a') as f:  # Use filename argument here
            content = input(f"Enter Data To Write In {filename}: ")
            f.write(content + "\n")  # Fixed write syntax
            print(f"Content added to {filename} successfully!")
    except FileNotFoundError:
        print(f"{filename} not found!")
    except Exception as e:
        print("An error occurred")


def main():
    while True:
        print("1. To Create A New File")
        print("2. To View All The Files In The Current Directory")
        print("3. To Delete A File")
        print("4. To Read A File")
        print("5. To Edit A File")
        print("6. Exit")
    
        choice = input("Enter Your Choice From (1-6): ") 

        if choice == '1':
            filename = input("Enter The Name Of The File To Create In Your Current Directory: ")  
            create_file(filename)
        elif choice == '2':
            view_all_file()
        elif choice == '3':
            filename = input("Enter File Name To Delete: ") 
            delete_file(filename)
        elif choice == '4':
            filename = input("Enter File Name to Read From Your Current Directory: ")  
            read_file(filename)
        elif choice == '5':
            filename = input("Enter File Name From Your Current Directory To Edit: ")  
            edit_file(filename)
        elif choice == '6':  
            print("Exiting The App..")
            break  
        else:
            print("Invalid Choice")  

if __name__ == "__main__":
    main()
