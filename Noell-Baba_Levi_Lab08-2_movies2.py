#!/usr/bin/env python3
#Levi Noell-Baba, June 23, 2023, CPT-168-W17, Lab 8-2


import csv
import sys

FILENAME = "movies_test.csv" #changing the filename in the global constant to test the program.

def exit_program():
    print("Terminating program.")
    sys.exit()

def read_movies():
    try:
        movies = []
        with open(FILENAME, newline="") as file:
            reader = csv.reader(file)
            for row in reader:
                movies.append(row)
        return movies
    except FileNotFoundError as e:
        #print(f"Could not find {FILENAME} file.") #commenting out the print statement.
        #exit_program() #commenting out the exit_program function in the read_movies() function
        return movies #return statement that returns the empty lovies list from the try block statements
    except Exception as e:
        print(type(e), e)
        exit_program()

def write_movies(movies):
    try:
        with open(FILENAME, "w", newline="") as file:
            #raise BlockingIOError #using a raise statement to raise an exception to test teh exception handler.
            writer = csv.writer(file)
            writer.writerows(movies)
    except OSError as e: #except clause used to hand the child "OSError class" as exception object "e"
        print(type(e), e) #print statement used to display the class name and the error message
        exit_program()
    except Exception as e:
        print(type(e), e)
        exit_program()

def list_movies(movies):
    for i, movie in enumerate(movies, start=1):
        print(f"{i}. {movie[0]} ({movie[1]})")
    print()
    
def add_movie(movies):
    name = input("Name: ")
    while True: #use of an infinite while loop
        try: #useing a try statement to catch an exception
            year = int(input("year: ")) #int() function converting the string input to an integer value
        except ValueError: #except clause that handles valueerror exceptions
            print("Invalid integer. Please Try again.") #print statement that informs the user an invalid integer has been inputted
            continue #continue statement that continues the try statement in the while loop if the input is invalid
        if year <= 0: #an if statement that checks for data validation by checking the condition in this statement
            print("Year must be greater than zero. Please try again.") #
            continue #use of a continue statement that continues the try statement
        else: #use of an else clause to check if the input is greater than zero. if so, the else clause uses the break function.
            break
    movie = []
    movie.append(name)
    movie.append(year)
    movies.append(movie)
    write_movies(movies)
    print(name + " was added.\n")

def delete_movie(movies):
    while True:
        try:
            number = int(input("Number: "))
        except ValueError:
            print("Invalid integer. Please try again.")
            continue
        if number < 1 or number > len(movies):
            print("There is no movie with that number. Please try again.")
        else:
            break
    movie = movies.pop(number - 1)
    write_movies(movies)
    print(f"{movie[0]} was deleted.\n")

def display_menu():
    print("The Movie List program")
    print()
    print("COMMAND MENU")
    print("list - List all movies")
    print("add -  Add a movie")
    print("del -  Delete a movie")
    print("exit - Exit program")
    print()    

def main():
    display_menu()
    movies = read_movies()
    while True:        
        command = input("Command: ")
        if command.lower() == "list":
            list_movies(movies)
        elif command.lower() == "add":
            add_movie(movies)
        elif command.lower() == "del":
            delete_movie(movies)
        elif command.lower() == "exit":
            break
        else:
            print("Not a valid command. Please try again.\n")
    print("Bye!")

if __name__ == "__main__":
    main()
