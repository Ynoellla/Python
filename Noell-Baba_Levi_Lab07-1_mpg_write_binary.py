#!/usr/bin/env python3
#Levi Noell-Baba, June 22, 2023, CPT-168-W17, Lab 7-1
import csv #Importing the csv module to use the functions and objects available
FILENAME = "trips.csv" # assigning the name of the CSV file using a global constant

headerList = ['Distance', 'Gallons', 'MPG'] #List containing the headers of the CSV file in order
def write_trips(trips): #function that stores the data in the list "trips" to the file trips.csv
    with open("trips.csv", "w", newline="", ) as file: #use of a with statement to open and close the file. it is automatically opened in write mode.
        writer = csv.writer(file) #writer() function used to return a csv writer object for the file and converts the data into comma-separated values
        dw = csv.DictWriter(file, delimiter=',', #use of the DictWriter() function to apply headers to the created CSV file
                            fieldnames=headerList)
        dw.writeheader()
        writer.writerows(trips)

def get_miles_driven(): #definition of the miled driven function that allows for input of values for the miles driven.
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used(): #definition of the gallons used function that allows for input of values for the gallons used.
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used
        
def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = [] #creation of an empty list that will contain the data of inputs of each trip.

    more = "y"
    while more.lower() == "y":
        miles_driven = get_miles_driven()
        gallons_used = get_gallons_used()
                                 
        mpg = round((miles_driven / gallons_used), 2)
        print(f"Miles Per Gallon:\t{mpg}")
        print()

        trip = [] #Creation of an empty list for each trip that adds a trip to the trips list.
        trip.append(miles_driven) #adding number of miles driven for each trip.
        trip.append(gallons_used) #adding number of gallons of gas used for each trip.
        trip.append(mpg) #adding the calculated MPG value for each trip.
        trips.append(trip) #adding each trip list to the trips list.
        
        more = input("More entries? (y or n): ")

    write_trips(trips) #function that executes and stores the data from the list "trips" to the file created.
    
    print("Bye!")

if __name__ == "__main__":
    main()

