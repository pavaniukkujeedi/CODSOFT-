contacts = {}

while True:
    print("\n 1.Add Contact")
    print("2.View Contact")
    print("3.Search Contact")
    print("4.Exit")
    choice = input("enter your choice:")
    if choice == "1":
        name = input("Enter Name:")
        phone=input("enter phone number:")
        contacts[name]=phone
        print("contact added!")
    elif choice =="2":
        print("\n contacts:")
        for name,phone in contacts.items():
            print(name, "-",phone)
    elif choice =="3":
        name = input("enter name to search:")
        if name in contacts:
            print("phone number:",contacts[name])
        else:
            print("contact not found!")
    elif choice == "4":
        print("exiting contact book...")
        break
    else:
        print("invalid choice!")                        