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
delimiters = ['(',')', "input=",'=', '-' ,' ', '[',']','{', '}', '!', '.', ',', ';', '!', '#', '$', '?', '/', '<', '>', "digitsPerNode", "txt"]
arg = sys.argv
equation_list = [] #Original Equation
numbers = [] #Arrary of Equation Numbers and Operators
simple_list = [] #Final Contents



# Definitions
def remove_delimiters_string(delimiters, s):
    new_s = s
    for i in delimiters:
        new_s = new_s.replace(i, ' ')
    return ' '.join(new_s.split())

def convert_string_to_list(s):
    l = list(s.split(" "))
    return l

def print_list(list):
    for x in list:
        print(str(x))

def store_file_data(input_file):
    try:
        f = open(input_file, "r")
        line = f.readline()
        while line:
            #line = line.replace(" ", "")
            equation_list.append(line.rstrip())
            new_line = remove_delimiters_string(delimiters, line)
            numbers.append(new_line.split())
            line = f.readline()
            
    except IOError:
        sys.exit()

def do_math(val1, val2, op):
    if(op == "multiply"):
        val3 = int(val1) * int(val2)
    elif(op == "add"):
        val3 = int(val1) + int(val2)
    return val3

def compute(e, n, s):
    stackA = []
    stackB = []
    iterator = 0
    #print(len(e))
    ans = ""
    for x in n:
        if(len(x) <= 2):
            tempC = "invalid expression"
        else:
            for y in x:
                stackA.append(y)
            while(len(stackA) > 0):
                temp = str(stackA[-1])
                if(temp.isdigit()):
                    stackB.append(temp)
                    stackA.pop()
                else:
                    if(len(stackB) > 2):
                        tempA = stackB.pop()
                        tempB = stackB.pop()
                        tempC = do_math(tempA, tempB, temp)
                        stackB.append(int(tempC))                   
                    elif(len(stackB) < 2):
                        tempC = "invalid expression"
                        break
                    stackA.pop()
        s.append(e[iterator] + "=" + str(tempC))
        iterator = iterator + 1
            
        

# Main Code 
input_file = "mytc.txt"
args_list = convert_string_to_list(input_file)
store_file_data(input_file)
#print_list(numbers)
compute(equation_list, numbers, simple_list)
print_list(simple_list)







##
##def store_file_data(input_file):
##    try:
##        with open(input_file) as f:
##            lines = [line.rstrip() for line in f]
##        return lines
##    except IOError:
##        sys.exit()










