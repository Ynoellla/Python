#!/usr/bin/env python3
#Levi Noell-Baba, June 17, 2023, CPT-168-W17, Lab 5-3     
def get_float(prompt, low, high):
    while True:
        number = float(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")
            
def get_integer(prompt, low, high):
    while True:
        number = int(input(prompt))
        if number > low and number <= high:
            is_valid = True
            return number
        else:
            print("Entry must be greater than", low,
                  "and less than or equal to", high,
                  "Please try again.")
            
def calculate_future_value(monthly_investment, yearly_interest, years):
    #print("Entering calculate_future_value()")
    # convert yearly values to monthly values
    monthly_interest_rate = yearly_interest / 12 / 100 #Logic Error - An additional division by 100 needed to be added here
    months = years * 12

    # calculate future value
    future_value = 0.0
    for i in range(1, months +1): #Logic Error - Python starts at 1 and stopped at months + 1. now, instead of stopping at "months" which the argument states, it now includes the additional month with the help of the +1 calling argument.
        future_value += monthly_investment
        monthly_interest = future_value * monthly_interest_rate
        future_value += monthly_interest
        #print("i =", i, "future value =", future_value)
    return future_value

def main():
    choice = "y"
    while choice.lower() == "y":
        # get input from the user
        monthly_investment = get_float("Enter monthly investment:\t", 0, 1000)
        yearly_interest_rate = get_float("Enter yearly interest rate:\t", 0, 15)
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
