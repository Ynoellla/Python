#!/usr/bin/env python3
#Levi Noell-Baba, June 22, 2023, CPT-168-W17, Lab 7-3
import pickle #importing the pickle module to use the functions and objects available

FILENAME = "trips.bin" #assigning the name of the bin file using a global constant

def write_trips(trips): #function that stores the data in the list "trips" to the file trips.bin
    with open(FILENAME, "wb") as file: # use of a with statement to open and close the file.
        pickle.dump(trips, file) #dump(bfile)method used to write the list to the binary file.

def read_trips(): #function that reads the data from the "trips.bin"file and returns the data
    trips = [] #creation of an empty "trips" list
    with open(FILENAME, "rb") as file: #use of a with statement and the open() function to open the binary file
        trips = pickle.load(file) #statement that calls the "load() method of the pickle module to get an object for the binary file
    return trips #return statement that returns the trips list back to the function

def get_miles_driven():  #definition of the miles driven function that allows for input of values for the miles driven
    while (miles_driven := float(input("Enter miles driven:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")       
    return miles_driven
          
def get_gallons_used(): #definition of the gallons used function that allows for input of values for the gallons used.
    while (gallons_used := float(input("Enter gallons of gas:\t"))) <= 0:                    
        print("Entry must be greater than zero. Please try again.\n")
    return gallons_used

def list_trips(trips):# definition of the list_trips function that displays the data in the trips list
    print("distance\tGallons\tMPG") #print function that displays each trip data that provides the distance of miles driven, gallons, and mpg
    for i in range(len(trips)): #a for loop that displays the numbered list of trips
        trip = trips[i] #"trip"(row) variable assigned to the value "i"
        print(str(trip[0]) + "\t\t" + str(trip[1]) + "\t\t" + str(trip[2])) # print function that displays the number of miles driven, gallons used, and mpg from each columns indexes
    print()

def main():
    # display a welcome message
    print("The Miles Per Gallon program")
    print()

    trips = read_trips() #main() function gets the data from the csv file.
    list_trips(trips) # main() function lists the data it gets from the csv file.

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
        write_trips(trips) #use of the write_trips() function to write data from teh trips list as an argument.

        list_trips(trips) #display of the data from the updated "trips" list

        
        more = input("More entries? (y or n): ")
    
    print("Bye!")

if __name__ == "__main__":
    main()

