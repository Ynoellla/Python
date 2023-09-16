#!/usr/bin/env python3
#Levi Noell-Baba, July 18, 2023, CPT-168-W17, Lab 11-1
from datetime import datetime, timedelta, date #importing the modules dateime, timedelta, and date

def get_invoice_date(): #defining the get invoice date function
    while True: #use of a while true statement to code for exceptions
        invoice_date_str = input("Enter the invoice date (MM/DD/YYYY): ") #input to ask the user for the date value
        try: #try statement to check if the value is valid. otherwise the code refers to the except clause to print the valueerror message.
            dt = datetime.strptime(invoice_date_str, "%m/%d/%Y") #parse the invoice date string into a datetime object with the format %m/%d/%Y 
        except ValueError: #value error exception that detects an incorrect input value
            print("Invalid date format! Try again.")
            continue
        invoice_date = date(dt.year, dt.month, dt.day) # creation of a date object from the datetime object to extract the date information
        if invoice_date > date.today(): #if statement that checks if the invoice date is greater than today's date
            print("Invoice date must be today or earlier. Try again.")
        else:
            return invoice_date
    
def main():
    print("The Invoice Due Date program")
    print()

    again = "y"
    while again.lower() == "y":
        invoice_date = get_invoice_date()
        print()

        # calculate due date and days overdue
        due_date = invoice_date + timedelta(days=30)
        current_date = date.today() #changed to .today to get the current days information
        days_overdue = (current_date - due_date).days

        # display results
        date_format = "%B %d, %Y"
        print(f"Invoice Date: {invoice_date:{date_format}}")
        print(f"Due Date:     {due_date:{date_format}}")
        print(f"Current Date: {current_date:{date_format}}")
        if days_overdue > 0:
            print(f"This invoice is {days_overdue} day(s) overdue.")
        else:
            days_due = days_overdue * -1
            print(f"This invoice is due in {days_due} day(s).")
        print()

        # ask if user wants to continue
        again = input("Continue? (y/n): ")
        print()
        
    print("Bye!")      

if __name__ == "__main__":
    main()
