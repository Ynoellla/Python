#!/usr/bin/env python3
#Levi Noell-Baba, June 4, 2023, CPT-168-W17, Lab 3-1
# display a welcome message
print("Welcome to the program!")
print("The Miles Per Gallon program")
print()
#Setting value of repeat input variable
another_trip = "y"
#setting to loop while true
while another_trip =="y":

    # get input from the user
    miles_driven = float(input("Enter miles driven:         "))
    gallons_used = float(input("Enter gallons of gas used:  "))
    Cost_of_a_gallon = float(input("Enter the cost of a gallon:  "))
#Control statements to keep input numbers in guidelines
    if miles_driven <= 0:
        print("Miles driven must be greater than zero. Please try again.")
    elif gallons_used <= 0:
        print("Gallons used must be greater than zero. Please try again.")
    elif Cost_of_a_gallon <= 0:
        print("Cost must be greater than zero. Please try again.")
    else:
        # calculate and display miles per gallon
        mpg = round(miles_driven / gallons_used, 2)
        total_gas_cost = round(gallons_used * Cost_of_a_gallon, 1)
        cost_per_mile = round(total_gas_cost / miles_driven, 1)
        print()
        print("Miles Per Gallon:          ", mpg)
        print("Total Gas Cost:            ", total_gas_cost)
        print("Cost Per Mile:             ", cost_per_mile)

    another_trip = input("Get entries for another trip (y/n)?")
    print()
print("Bye!")



