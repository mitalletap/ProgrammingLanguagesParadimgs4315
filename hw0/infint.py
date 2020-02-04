import collections
import fileinput
import sys


# Resources:
# Stack Overflow: How to Remove Delimiters from a String
# https://stackoverflow.com/questions/35221535/python-removing-delimiters-from-strings
# Utilized resources from GeeksForGeeks, Python.org, previous projects
# Iterative Approach


# Functionality
# Add's numbers of a max of 40 digits (if over, print's error)
# Recognizes invalid number (if not a number, print's error)
# Identifies if input file has been selected or not. (If not, asks you to add the input file as an argument CORRECTLY)
# If input file does not exits, it will ask you the file is incorrect.


# Steps
# Reads input file if valid
# Read each line, removes all delimiters, and stores numbers in a list array (if they are numbers)
# From list array, it takes the key-value and stores in a dictionary
# New dictionary is added to another list
# Prints the output

# Variables
delimiters = ['(',')', "input=",'=', '-' ,' ', '[',']','{', '}', '!', '.', ',', '!', '#', '$', '?', '/', '<', '>', "add", "txt"]
arg = sys.argv
equation_list = []
simple_list = []



# Definitions
def remove_delimiters_string(delimiters, s):
    new_s = s
    for i in delimiters:
        new_s = new_s.replace(i, ' ')
    return ' '.join(new_s.split())


   
def functionA(inut_file, equation_list, simple_list):
    try:
        f = open(input_file + ".txt", "r")
    except IOError:
        print("Error: Input File Incorrect")
        sys.exit()

    line = f.readline()
    while line:
        line = line.replace(" ", "")
        equation_list.append(line.rstrip())
        new_line = remove_delimiters_string(delimiters, line)
        numbers = new_line.split()

        try:
            (int(numbers[0]) and int(numbers[1]))
            if((len(str(numbers[0])) <= 40 or len(str(numbers[1])) <= 40)):
                sum = int(numbers[0]) + int(numbers[1])
            else:
                sum = "error"
        except ValueError:
            sum = "error"
        
        dictionary = {line.rstrip() : ("=" + str(sum))}
        simple_list.append(dictionary)
        line = f.readline()
    f.close()


index = 0
try:
    input_file = remove_delimiters_string(delimiters, arg[1])
except IndexError:
    print("Input was not specified")
    sys.exit()


# Main Code
functionA(input_file, equation_list, simple_list)
for x in equation_list:
    print(equation_list[index] + simple_list[index][equation_list[index]])
    index = index + 1

    













