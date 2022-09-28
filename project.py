contact = {}
  

  
  
def delete():
    global contact
    print("Enter the contact"\
        " name to be deleted")
  
    name = input().strip()
  
    if name in contact:
        del(contact[name])
        print("Contact Deleted !\n")
    else:
        print("Contact not found !\n")
  
    print("Do you want to perform more"\
        " operations? (y / n)")
  
    choice = input().strip()
    if choice == "y":
        main()
  
def update():
    global contact
    print("Enter the contact name"\
        " to be updated - ")
  
    name = input().strip()
  
    if name in contact:
        print("Enter the new"\
            " contact number - ")
        phone = int(input())
  
        contact[name] = phone
  
        print("Contact updated\n")
    else:
        print("Contact not found !\n")
  
    print("Do you want to perform "\
        "more operations? (y / n)")
  
    choice = input().strip()
    if choice == "y":
        main()
  

def search():
    while True:


        global contact
        print("Enter the name to be searched - ")
  
        name = input().strip()
  
        if name in contact:
            print("Contact Found !")
            print(name, contact[name])
        else:
            print("Contact not found !\n")
  
  
        print("Do you want to perform more"\
         " operations? (y / n)")
  
        choice = input().strip()
        if choice == "y":
            main()
  
def store():
    while True:

        print("\n\nEnter the name"\
        " and phone number"+\
        " separated by space - ")
  
        name, phone = map(str, \
                    input().strip()\
                            .split(" "))
  
        global contact
        if name in contact:
            print("Contact Already exists !\n")
        else:
            contact[name] = phone
            print("Contact Stored !")
  
        print("Do you want to perform more"\
        " operations? (y / n)")
  
        choice = input().strip()
        if choice == "y":
            main()
        elif choice=="n":
            break    
def email():
    while True:

        global contact
        print("Enter the name to  sent mail - ")
  
        name = input().strip()
  
        if name in contact:
            print("Contact Found !")
            print(name, contact[name])
            filename = "phonebook1.txt"  
            myfile = open(filename, "a+")  
           
              
            
            myfile.write(contact[name])  
            print( "The following Contact Details:\n " + contact[name]+ "\nhas been stored successfully!")  
            myfile.close 
        else:
            print("Contact not found !\n")

        
  
      
              
  
        print("Do you want to perform more"\
        " operations? (y / n)")
  
        choice = input().strip()
        if choice == "y":
            main()
        elif choice=="n":
            break  
# Main Function for Menu-Driven
def main():
    while True:

  
        print("Store Contact number (1)")
        print("Search Contact number (2)")
        print("Update Contact number (3)")
        print("Delete Contact number (4)")
        print("send email(5)")
        print("exit (6)")

  
        choice = input("enter your choice:")
        if choice=="1":
            store()
        elif choice == "2":  
            search()  
        
        elif choice == "3":  
            update()  
        elif choice == "4":  
            delete() 
        elif choice == "5":  
            email()
        elif choice == "6":  
            break 
        else: 
            print( "Please provide a valid input!\n")  
            enter = input( "Press Enter to continue ...")  
            main()  
  
  
if __name__ == "__main__":
    print("----------------------"+\
        "Menu-driven program"+\
        "----------------------")
  
main()
