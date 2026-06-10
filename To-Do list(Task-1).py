tasks=[]
while True:
    print("\n 1.Add 2.View 3.Exit")
    choice=input("Enter choice:")
    if choice=="1":
        task=input("enter task:")
        tasks.append(task)
        print("task Added!")
    elif choice=="2":
        print("\nTo-Do List:")
        for i, task in enumerate(tasks,
1):
            print(i,".",task)
    elif choice=="3":
        print("Exiting...")
        break
    else:
        print("Invalid Choice")        
                                
                                    