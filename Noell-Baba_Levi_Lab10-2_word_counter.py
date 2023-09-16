#!/usr/bin/env python3
#Levi Noell-Baba, July 16, 2023, CPT-168-W17, Lab 10-2
import re #importing the "re" module or "regular expression. the functions in this module let you check if a particular string matches a given regular expression.
def get_sentences(filename): #definition of get_sentences function to get the number of sentences in a file.
    with open(filename) as file: #statement that reads the content of a file and stores it in the variable text
        text = file.read()
    sentences = re.split(r'[.!?]', text) #splitting the text into sentences using periods, exclamation points, and question marks as separators between sentences
    sentences = [sentence.strip() for sentence in sentences if sentence.strip()] #use of the strip() function to remove any leading or tailing spaces.
    return sentences

def get_words_from_file(filename): #function that gets text from specified file.
    with open(filename) as file:
        text = file.read()    # read str from file

    # print(text)
    text = text.replace("\n", "")
    text = text.replace(",", "")
    text = text.replace(".", "")
    text = text.lower()
    
    words = text.split(" ")   # convert str to list
    words.sort()
    # print(words)
    return words

def get_unique_words(words): #function that gets each word used in the file
    unique_words = []
    unique_words.append(words[0])
    
    for i in range(1, len(words)):
        if words[i] == words[i - 1]:
            continue
        else:
            unique_words.append(words[i])            
    return unique_words

def main():
    filename = "gettysburg_address.txt"
    print("The Word Counter program\n")

    #get sentences
    sentences = get_sentences(filename) #assigning the result of the get_sentence function to the variable "sentences"

    # get words and unique words
    words = get_words_from_file(filename) # get list of words
    unique_words = get_unique_words(words)

    # display number of words and unique words
    print(f"Number of sentences = {len(sentences)}")
    print(f"Number of words = {len(words)}")
    print(f"Number of unique words = {len(unique_words)}")

    # display unique words and their word counts
    print("Unique word occurrences:")
    for word in unique_words:
        print(f"    {word} = {words.count(word)}")
 
if __name__ == "__main__":
    main()
