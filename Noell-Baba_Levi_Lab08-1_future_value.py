#!/usr/bin/env python3
#Levi Noell-Baba, June 23, 2023, CPT-168-W17, Lab 8-1        
def get_number(prompt, low, high):
    while True:
        try: #a try statement that allows one to code any statement that might throw an exception
            number = float(input(prompt)) 
        except ValueError: # except clause used to catch exceptions that occur after the users input to prevent the program from crashing.
            print("you entered an invalid number") #informing the user that an invalid entry has been input using a print statement.
            continue #continue statement that continues execution of the while loop
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")
            
def get_integer(prompt, low, high):
    while True:
        try: #a try statement that allows one to code any statement that might throw an exception
            number = int(input(prompt)) 
        except ValueError: #except clause used to catch exceptions that occur after the users input to prevent the program from crashing
            print("you entered an invalid integer.") #message informing the user that an invalid input has been entered using a print statement.
            continue #continue statement used to keep the while loop going to ask for another input from the user.
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print(f"Entry must be greater than {low} " 
                  f"and less than or equal to {high}.")


def calculate_future_value(monthly_investment, yearly_interest, years):
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(months):
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest

    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_number("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_number("Enter yearly interest rate:\t", 0, 15)
        years = get_integer("Enter number of years:\t\t", 0, 50)

        # get and display future value
        future_value = calculate_future_value(
            monthly_investment, yearly_interest_rate, years)
        
        print()
        print(f"Future value:\t\t\t{round(future_value, 2)}")
        print()

        # see if the user wants to continue
        choice = input("Continue? (y/n): ")
        print()

    print("Bye!")
    
if __name__ == "__main__":
    main()
