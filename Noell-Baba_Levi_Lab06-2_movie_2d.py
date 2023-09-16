#!/usr/bin/env python3
#Levi Noell-Baba, June 18, 2023, CPT-168-W17, Lab 6-2
def display_menu(): # Definition of the "display_menu() function" that displays the name of the "Movie List 2D program" as well as the "Command Menu" with its coresonding commands below for the user to select from. 
    print("The Movie List 2D program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("find - Find movies by year")
    print("exit - Exit program")
    print()    

def list(movie_list): #definition of the list function that has a list called movie_list passed to it in its call statement
    if len(movie_list) == 0: # us of an if statement to check if the argument is equal to 0
        print("There are no movies in the list.\n")
        return # return function to return the result of the calculation
    else:
        i = 0 #an integer variable assigned a value of 0.
        for movie in movie_list: #use of a for loop that goes through the larger movie_list list and searches for movies.
            row = movie #assignment of the list "movie" as the value to the "row" variable.
            print(str(i+1) + ". " + row[0] 
                  + " (" + str(row[1]) + ")"
                  + " @ " + str(row[2])) #execution of the print function that displays the list of movies 
            i += 1 #1 added to the integer variable "i"
        print()

def add(movie_list): #definition of the "add() function that adds a new movie to the end of the list movie_list.
    name = input("Name: ") #the input() function is used to get an input of the movie name from the user
    year = input("Year: ")# the input() function is used to get an input from the user for the year of the movie
    price = input("Price: ") # the input() function is used to get an input from the user for the price of the movie
    movie = [] #creation of an empty list named "movie"
    movie.append(name) # use of the append function to add the name of the movie to the movie list
    movie.append(year) # use of the append function to add the year of the movie to the movie list
    movie.append(price) # use of the append function to add the price of the movie to the movie list
    movie_list.append(movie) # use of the append function to add the movie generated from user input back into the "movie_list" list
    print(movie[0] + " was added.\n") # print function used to notify the user that the movie was added to the movie_list list

def delete(movie_list): #definition of the delete function for the user input
    number = int(input("Number: ")) #defining the variable number that uses the input of the user as an argument.
    if number < 1 or number > len(movie_list): #if statement that uses the or logical operator to determine if the input satisfies either condition. 
        print("Invalid movie number.\n") #print statement that displays if an invalid input is detected.
    else:
        movie = movie_list.pop(number-1) #variable assigned to removing the item in a list
        print(movie[0] + " was deleted.\n") # print function that notifies the user that the intended movie was removed

def find_by_year(movie_list): #definition of the find_by_year function that finds a certain movie according to year it was released.
    year = int(input("Year: ")) #defining the variable "year" by equating it to the input of the user after calling the find_by_year function
    for movie in movie_list: #a for loop used to specify that the function searches the movie_list
        if movie[1] == year: #if statement that finds the movie with the corresponding release year to the input
            print(movie[0] + " was released in " + str(year)) #print function that prints the final statement plus the year converted into a string
    print()

def main(): #definition of the main() function that calls the display_menu function using the movie_list list
    movie_list = [["Monty Python and the Holy Grail", 1975, 9.95],
                  ["On the Waterfront", 1954, 5.59],
                  ["Cat on a Hot Tin Roof", 1958, 7.95]]
    display_menu() #display_menu() function is called to execute a while loop
    while True: #while statements that evaluates the expression to true and continues the while loop
        command = input("Command: ") # command variable assigned to the value of the "input() function"
        if command == "list": #if statement that determines if the input is calling the list function
            list(movie_list) #list function called to display the movies_list
        elif command == "add": #elif statement that determines if the input is calling the "add" function.
            add(movie_list) #add function called to add to the movies_list.
        elif command == "del": #elif statement that determines if user input calls the "del" function to remove a movie.
            delete(movie_list) # "del" function called to remove a movie from the movies_list 
        elif command == "find": # elif statement used to determine if the user called the "find" function
            find_by_year(movie_list) # find_by_year function called to diplay the desired movie from the movie_list list.
        elif command == "exit": #elif command used to determine if the user enters "exit" to break out of the while loop.
            break
        else:
            print("Not a valid command. Please try again. \n") #else statement used to indicate an invalid input was given by the user.
    print("Bye!")

if __name__ == "__main__":
    main()
            
    
