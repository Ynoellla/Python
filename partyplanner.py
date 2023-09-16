#Levi Noell-Baba, July 21, 2023, CPT-168-W17, Final Project
import csv# Import of the CSV module
import sys #Import of the sys module

FILENAME = "partyplanner.csv" #FileName of the csv file to be created and called.

def display_start(): #display_start function that shows the user the list of commands that are available
    print("Command list choices: ")
    print("List - List attendees")
    print("Add - Add an attendee")
    print("Del - Remove an attendee")
    print("Search - Search the attendees for an individual")
    print("Edit - Edit the information of an attendee")
    print("Report - Summary of all information")
    print("Exit - Exit the program")

def display_menu(): #display_menu function that displays the menu choices for the user and their corresponding number
    print("Menu Choices:")
    print("1. Chicken entree")
    print("2. Beef entree")
    print("3. Vegetarian entree")
    print("4. Stew entree")
    print("5. Hibachi entree")
    print("6. Salad entree")
    print("7. Sushi entree")

def exit_program(): #exit program function that gets called if the user enters "exit" 
    print("Terminating program.")
    sys.exit()

def write_attendees(attendees): #def of the write_attendees function that writes the data to the csv file. 
    try:
        with open(FILENAME, "w", newline="") as file: #open the file with the desgnation to write to a newline
            writer = csv.writer(file) #use of writer fuction of the csv module to write to the file.
            writer.writerow(["Name", "Membership Status", "Menu Choice", "Amount Paid"]) #designation of headers and input types
            for attendee in attendees: #for statement that writes each attendee in the list of attendees
                writer.writerow(attendee) #write to the row of the csv file
    except OSError as e: #except function that catches an OSError
        print(type(e), e)
        exit_program()
    except Exception as e: #except function that catches any exceptions
        print(type(e), e)
        exit_program()

def list_attendees(attendees): #list_attendees function that lists all attendees and their information
    print("Attendees:") # print function that displays "Attendees:"
    print("No. Name             Membership Status       Menu Choice        Amount Paid") #print function that displays the header for the list function
    for i, attendee in enumerate(attendees, start=1): #for statment that enumerates the attendees starting at one so they all have a numeric value
        name = attendee[0] #name variable is designated to the first data type in the attendee list
        membership_status = attendee[1] #membership_status variable is designated to the second data type in the attendee list
        menu_choice = attendee[2] #menu_choice variable is designated to the third data type in the attendee list
        amount_paid = attendee[3] #amount_paid variable is designated to the fourth data type in the attendee list
        print(f"{i}. {name.ljust(20)} {membership_status.ljust(20)} {menu_choice.ljust(20)} {amount_paid}") #print statement that prints out the attendee information
    print()

def add_attendee(attendees): # add_attendee function that allows the user to add an attendee to the attendees list
    name = input("Name: ") # input that gets assigned to the variable "name" to be added
    while True: #while true loop used to get information of the attendee and loop through if incorrect information is given
        Membership_status = input("Is this addition a Guest, Member, VIP, Dependent, Child, or Staff?: ") #membership_status is assigned to the user input
        if Membership_status.upper() not in ['MEMBER', 'GUEST', 'VIP', 'DEPENDENT', 'CHILD', 'STAFF']: #if statement that uses the .upper() function to change the user input to uppercase to search from the list provided.
            print("Invalid input. Please input a valid Membership Status")#print function that is displayed if the input is not in the given list
            continue #continue statment to get a new input from the user
        display_menu()
        Menu_order = input("What will this addition be having from the menu? Please enter the number associated with the item.: ") #menu_order is assigned to the numeric value the user inputs otherwise the else statment executes
        if Menu_order == '1': #if statement that checks if the entry is "1"
            order = "Chicken entree" #assigning the order to "chicken entree" if the input is 1
        elif Menu_order == '2': #elif statements that checks if the numbers equal their specified number. if so, the order is assigned the specified menu option
            order = "Beef entree"
        elif Menu_order == '3':
            order = "Vegetarian entree"
        elif Menu_order == '4':
            order = "Stew entree"
        elif Menu_order == '5':
            order = "Hibachi entree"
        elif Menu_order == '6':
            order = "Salad entree"
        elif Menu_order == '7':
            order = "Sushi entree"
        else: #else statment that prints if the order entry is not valid
            print("Invalid input. Please enter a valid value. ")
            continue
        Amount_paid = int(input("Please enter amount paid: ")) #amount_paid is assigned to the user input and converted to an integer.
        if Amount_paid < 22: #if statement that checks if the amount_paid is less than 22 and prints a statment letting the user know theres an outstanding balance
            print("Please see a staff member to pay your outstanding balance before being added.")
        elif Amount_paid >= 22:
            print("Thank you for your contribution!")
            break
        else: #else statement that catches any invalid inputs
            print("Please enter a valid input")
            continue
    attendee = [name, Membership_status, order, Amount_paid] #designation of the attendee list
    attendees.append(attendee) #attendee is appended onto the end of the attendees list
    write_attendees(attendees) #write_attendees updates the csv file to include the new attendee
    print(f"Attendee has been added.") #print function that lets the user know the attendee has been added
    return attendees #return statement that returns the new attendees list

def delete_attendee(attendees): #delete_attendee function that allows the user to delete an attendee
    while True: #while true loop that is used to get the information about the attendee that is being deleted
        try: #try statment used to code for exceptions
            number = int(input("Attendee Number: ")) #number variable used to get the number associated with the attendee as an integer
        except ValueError:#except statement that codes for a valueError if the inputted number is not a number.
            print("Invalid integer. Please try again.")
            continue 
        if number < 1 or number > len(attendees):#if statment that checks if the number is within the range of len(attendees) otherwise it prints that there is no attendee
            print("There is no attendee with that number. Please try again.")
        else:
            break
    attendee = attendees.pop(number - 1) #attendee removed from the list using pop
    write_attendees(attendees) #new list is written to the file
    print(f"{attendee[0]} was deleted.\n") #letting the user know the attendee was deleted

def search_attendees(attendees): #search_attendees function that searches the list for an attendee by name
    search_name = input("Enter the attendee you would like to search for: ") #assigning the search name variable to the inputted user input
    found_attendees = [attendee for attendee in attendees if search_name.lower() in attendee[0].lower()] #lists the attendees found with that name and assigns to the found_attendees variable.
    if found_attendees: #if statment that operates of an attendee is found
        print("Matching Attendees:")
        print("No. Name             Membership Status       Menu Choice        Amount Paid")
        for i, attendee in enumerate(found_attendees, start=1): #lists the attendees in a new list that begins at number 1
            name = attendee[0]
            membership_status = attendee[1]
            menu_choice = attendee[2]
            amount_paid = attendee[3]
            print(f"{i}. {name.ljust(20)} {membership_status.ljust(20)} {menu_choice.ljust(20)} {amount_paid}")
    else: #else statement that lets the user know an attendee was not found
        print("Attendee not found")
        

def read_attendees(): #read_attendees function that opens and reads the csv file.
    try: #try clause used to code for exceptions
        attendees = [] #defining the attendees list
        with open(FILENAME, newline="") as file: #opens the file
            reader = csv.reader(file) #reader assigned to the open file
            next(reader)
            for row in reader: #for statement that checks each row and and appends the row onto the list
                attendees.append(row)
        return attendees #return statement that returns the list
    except FileNotFoundError: #exception coded for a filenotfounderror if the file could not be found
        return []
    except Exception as e: #exception coded if the program needs to exit
        print(type(e), e)
        exit_program()

def edit_attendee(attendees): #edit attendee function that allows the user to edit an attendee's information
    name = input("Attendee Name: ").lower() #name is assigned to the inputted name that is converted to lowercase
    for attendee in attendees: #for statement that searches all attendee in attendees
        if attendee[0].lower() == name: #if statment that searches the first datavalue in the attendee
            attendee_found = True #assigning a true value to the attendee found to continue into the while loop
            print("Editing attendee:", attendee[0]) #display that allows the user to see their options
            print("Current Information:")
            print("1. Name:", attendee[0])
            print("2. Membership Status:", attendee[1])
            print("3. Menu Choice:", attendee[2])
            print("4. Amount Paid:", attendee[3])

            while True: #while true loop that is used to go through each function to change the attendee information.
                try: #try statement that codes for exceptions
                    choice = int(input("Enter the number corresponding to the attendee information you would like to edit (1-4)")) #choice variable is assigned to the integer that the user inputs
                    if choice not in range(1, 5): #checks if the inputted integer is within a certain range
                        print("Invalid choice. Please enter a valid input value.")
                    else:
                        break
                except ValueError: #exception that prints if an invalid input is detected
                    print("Invalid input. Please enter a valid input.")

            if choice == 1: #if statment that checks if the input is equal to 1
                name_change = input("Enter the name of the guest: ") #name_change is assigned to the name of the guest
                attendee[0] = name_change #first data value in the attendee list is changed to name_change
                print("Attendee name has been changed.") #letting the user know the name has been changed
                break
            elif choice == 2: #elif statement that checks if the value is equal to 2
                while True: #while true loop
                    new_membership_status = input("Enter the new membership status: ")#new_membership_status assigned to the new inputted membership status
                    if new_membership_status.upper() not in ['MEMBER', 'GUEST', 'VIP', 'DEPENDENT', 'CHILD', 'STAFF']: #converts the input into uppercase and checks if it is equal to a value in the list
                        print("Invalid membership status. Please try again.")
                    else: #else statement that updates the membership status
                        attendee[1] = new_membership_status.upper() #changes the value in the second data spot of attendee with the new membership status
                        print("Attendee membership status has been updated")
                        break
            elif choice == 3: #elif statement that checks if the input is equal to 3
                display_menu() #display menu function
                while True: #while true loop used to code for exceptions
                    try:
                        new_choice = int(input("Enter the new menu choice (1-7): ")) #new_choice assigned to the integer the user inputs
                        if new_choice not in range(1, 8): #if statement that checks if the input is not in a certain range
                            print("Invalid menu choice. Please enter a valid menu choice.")
                        else: #else statment that is used to break out of the while loop if the value is valid
                            break
                    except ValueError: #exception coded incase of a ValueError
                        print("Invalid input. Please enter a valid input")
                menu_options = ["Chicken entree", "Beef entree", "Vegetarian entree", "Stew entree", "Hibachi entree", "Salad entree", "Sushi entree"]#menu_options is assigned to the list provided
                new_menu_choice = menu_options[new_choice - 1] #new_menu_choice is assigned to the choice chosen by the user input
                attendee[2] = new_menu_choice #updates the third data value in the attendee list with the new_menu_choice
                print("Menu order information has been updated.")
            elif choice == 4:#elif statement that checks if the choice is equal to 4
                while True: #while true loop that is used to code for an exception
                    try:
                        amount_change = int(input("Enter the new amount paid: ")) #amount_change assigned to an integer input value
                        if amount_change < 22: #if statment that checks if the inputted amount is greater than 22
                            print("Amount paid must be greater than $22.00")
                        else: #else statement that updates the attendee amount paid
                            attendee[3] = amount_change #the fourth value of the attendee list is updated with amount_change
                            print("Attendee amount paid has been updated")
                            break
                    except ValueError: #valueerror exception coded for to make sure valid input is inputted
                        print("Invalid input. Input must be a valid number.")
            else: #else statement that lets the user know an invalid input was inputted
                print("Invalid choice number. Please enter a valid input.")

            print("Attendee information has been successfully updated.") #tells the user the list was successfully updated
            break
    if not attendee_found: #if statment that prints if an attendee was not found
        print("Attendee not found")

def report_summary(attendees): #report_summary function that reports a summary of the information
    total_members = 0 #assigning and creating variables used
    total_guests = 0
    total_VIPs = 0
    total_dependents = 0
    total_children = 0
    total_staff = 0
    total_entrees = {'Chicken entree': 0, 'Beef entree': 0, 'Vegetarian entree': 0, 'Stew entree': 0, 'Hibachi entree': 0, 'Salad entree':0, 'Sushi entree': 0} #creation of a dictionary for the total_entrees variable
    total_amount_raised = 0

    for attendee in attendees: #for statment that goes through each attendee in the attendees list
        membership_status = attendee[1].upper() #makes sure the membership status is valid and changes it to uppercase
        if membership_status == 'MEMBER': #if and elif statments used to update the variables assigned above and add 1
            total_members += 1
        elif membership_status == 'GUEST':
            total_guests += 1
        elif membership_status == 'VIP':
            total_VIPs += 1
        elif membership_status == 'DEPENDENT':
            total_dependents += 1
        elif membership_status == 'CHILD':
            total_children += 1
        elif membership_status == 'STAFF':
            total_staff += 1

        menu_choice = attendee[2] #assigning menu_choice to the third value in the attendee list
        if menu_choice in total_entrees: #if statement that checks if the menu_choice is in total_entrees
            total_entrees[menu_choice] += 1 #adds one to the menu choice assigned to the attendee

        total_amount_raised += int(attendee[3]) #calculation that calculates total of amount raised in the fourth attendee data value

    print("Summary:") #print summary with the updated report from the variable created above
    print(f"Total Members: {total_members}")
    print(f"Total Guests: {total_guests}")
    print(f"Total VIPs: {total_VIPs}")
    print(f"Total Dependents: {total_dependents}")
    print(f"Total Children: {total_children}")
    print(f"Total Staff: {total_staff}")
    print("Total Entrees:")
    for entree, count in total_entrees.items(): #creation of dictionaries to display the total entrees ordered
        print(f"{entree}: {count}")
    print(f"Total Amount Raised: ${total_amount_raised:.2f}")





def main(): #main function that is called to run the program
    display_start() #displays the start of the program
    attendees = read_attendees() #attendees list is pulled from the csv file
    while True: #while true statement that allows the user to input the commands
        command = input("Command: ") #command is assigned to the input
        if command.lower() == "list": #command inputs are converted into lowercase to check if they're equal to the commands. if they are, the specific function is called
            list_attendees(attendees)
        elif command.lower() == "add":
            attendees = add_attendee(attendees)
        elif command.lower() == "del":
            delete_attendee(attendees)
        elif command.lower() == "search":
            search_attendees(attendees)
        elif command.lower() == "edit":
            edit_attendee(attendees)
        elif command.lower() == "report":
            report_summary(attendees)
        elif command.lower() == "exit":
            write_attendees(attendees)
            break
        else:
            print("please enter a valid command")
            continue


main()

