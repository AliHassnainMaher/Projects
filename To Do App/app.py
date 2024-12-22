def tasks():
    headding = "--Welcome To Task Managment App--"
    print(headding.center(80))
    #ask user how many tasks
    total_tasks = int(input("Enter How Much Tasks You Want To Add : "))
    for i in range(1,total_tasks+1):
        task_name = input(f"Enter Task {i} : ")
    MainTasks = [task_name]
    while True:
        print("1 for .To Add Another Task")
        print("2 for .To View Your Tasks")
        print("3 for .To Edit A Task")
        print("4 for .To Delete A Task")
        print("5 for .To Clear Full List")
        print("6 for .To Exit")
        choice = int(input("Enter Your Choce : "))

        
        if(choice==1):
            add = input("Enter What Want To Add : ")
            MainTasks.append(add)
            with open("tasks.txt" ,"w") as f:
                f.write(tasks())
        if(choice==2):
            print(MainTasks)
        if choice == 3:
            try:
                # Display the list with proper numbering (starting from 1)
                print("Current Tasks:")
                for i, task in enumerate(MainTasks, start=1):
                    print(f"{i}. {task}")

                # Ask user for the task number they want to edit
                edit1 = int(input("Enter the Task Number You Want to Edit: "))

                # Adjust user input to 0-based index
                task_index = edit1 - 1

                # Validate index range
                if 0 <= task_index < len(MainTasks):
                # Ask for the new task
                    edit2 = input("Enter the New Task: ")

                # Replace the task at the specific index
                MainTasks[task_index] = edit2
                print("Task updated successfully!")
            except ValueError:
                print("Error: Please enter a valid number.")



        if(choice==4):
            delete = input("Enter What Task You Want To Delete : ")
            MainTasks.remove(delete)
            if(choice==5):
                MainTasks.clear()
            if(choice==6):
                break
with open("tasks.txt" ,"w") as f:
    f.write(tasks())
     
tasks()
                