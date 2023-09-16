#!/usr/bin/env python3
#Levi Noell-Baba, July 16, 2023, CPT-168-W17, Lab 10-1  
def main():
    full_name = get_full_name() #Get the value from the get_full_name() function and assign it to full_name
    password = get_password() #Get the value from the get_password() function and assign it to password
    email_address = get_email_address() #Get the value from the get_email_address() function and assign it to email_address
    phone_number = get_phone_number()#Get the value from the get_phone_number() function and assign it to phone_number
    print()

    
    first_name = get_first_name(full_name)   
    print(f"Hi {first_name}, thanks for creating an account.")
    print(f"We'll text your confirmation code to this number: {phone_number}")
    
def get_full_name(): #function used to get the users full name
    while True:
        name = input("Enter full name:       ").strip() #user input of their full name with the strip function removing leading and trailing spaces.
        if " " in name: #an if statement that checks that there is a space in the name the user inputted for a first and last name 
            return name
        else:
            print("You must enter your full name.")
    
def get_first_name(full_name): #function that gets the first name from the get_full_name function
    index1 = full_name.find(" ") #finds the first space index in full_name
    first_name = full_name[:index1] #first name called from full_name
    return first_name
    
def get_password(): #function to get the inputted password from the user
    while True:
        digit = False #checks to make sure the password fits specifications
        cap_letter = False
        password = input("Enter password:        ").strip() #user inputted password stripped of spaces before and after
        for char in password:
            if char.isdigit(): #if statement making sure there's a number in the password
                digit = True
            elif char.isupper(): #elif statement making sure there's a capital letter in the password
                cap_letter = True
        if digit == False or cap_letter == False or len(password) < 8: #if statement making sure the password passes criteria and has at least 8 characters in length
            print(f"Password must be 8 characters or more \n"
                  f"with at least one digit and one uppercase letter.")
        else:
            return password

def get_email_address(): #function to get an inputted email address from the user
    while True:
        try:
            email=input("Enter email address: ").strip() #email address input that is stripped of spaces before and after input
            local_part, domain_part = email.split('@') #splitting the email into two parts at the "@" character 
            if '.' not in domain_part or domain_part.split('.')[-1].lower() not in {'com', 'org', 'net', 'edu'}: #if function that checks if there is a "." in the domain part and then checks if ending ends in "com, edu, org, or net"
                raise ValueError() #raises a value error if the domain is not valid
            return email
        except ValueError:
            print("Please enter a valid email address.") #printed if there is a value error.

def get_phone_number(): #function to get the inputted phone number from the user
    while True:
        phone_number = input("Enter phone number: ").strip() #inputted number with spaces stripped assigned to phone_number
        for char in " -().":
            phone_number = phone_number.replace(char, "") #removes non digit values
        if len(phone_number) != 10 or phone_number.isdigit() == False: #if statement that checks if the number is 10 digits in length or is not digits
                print("Please enter a 10 digit phone number.")
        else:
            phone_number = phone_number[0:3] + "." + phone_number[3:6] + "." + phone_number[6:] #formatting the number with periods
            return phone_number
        
if __name__ == "__main__":
    main()
