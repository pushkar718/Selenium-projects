import os
import time

# if os.name == "posix":
#     os.system("clear")
# elif os.name == "nt":
#     os.system("cls")
choice=0
while (choice!=1) or (choice!=2) or (choice!=3) or (choice!=4):
    print("-"*10,"PhoneBook","-"*10)
    print("1. Your contacts ")
    print("2. Add contact ")
    print("3. Delete a Contact")
    print("4. Exit")
    choice=int(input(">> "))
    if choice==1:
        print("Currently you don't have any contacts.")
        time.sleep(5)
        if os.name=="posix":
            os.system("clear")
        elif os.name=="nt":
            os.system("cls")
    elif choice==2:
        number=str(input("Enter the number> "))
        if (len(number)>10) or (len(number)<10):
            print("The format of the number you entered is invalid. ")
        else:
            name=str(input("Enter name> "))
            time.sleep(2)
            print("Contact saved successfully")