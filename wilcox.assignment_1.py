"""
Assignment #1 (Module 3): Built-in types and functions

Begin by executing this script from the command line or visual stodio code by typing
    `$ python assignment_1.py` or assignment_1.py

This script will print out all the questions . This
script must execute without error.

Some questions have variables in them, and will need manipulation. In that
case, perform whatever transformations to the variable, and make sure that
it prints the output.


"""

print("Question_1():")
print("Print a tuple containing a single item.\n")

x = (1,)    # is a tuple
print(x, '\n')    # print the tuple


print("Question_2():")
print("Print a list of strings.('one', 'two', 'three')\n")

countQ2 = ['one','two','three']   # create the string list
print(countQ2, '\n')  # print the list


print("Question_3():")
print("Print list of floats.(1.0, 2.0, 3.0)\n")

countQ3 = [1.0, 2.0, 3.0]   # create the float list
print(countQ3, '\n')    # print the list


print("Question_4():")
print("Print the following list in reverse order, using the sort built-in function.")
print("10, 20, 30, 40, 100\n") #1 mark deduction if you didn't use the sort() function

countQ4 = [10, 20, 30, 40, 100]     # create the int list
countQ4.sort(reverse=True)   # sort list in reverse order
print(countQ4, '\n')    # print list


print("Question_5():")
print("Using the append built-in function, add the number 200 to the following list, and print.")
print("197, 198, 199\n")

countQ5 = [197, 198, 199]   # create int list
countQ5.append(200)     # append 200 to the end of list
print(countQ5, '\n')    # print new int list

print("Question_6():")
print("Using a built-in function, insert the value `banana` after `orange`")
fruits = ['orange', 'tomato\n']

fruits.insert(1, 'banana')  # insert banana after orange in string list
print(fruits, '\n') # print list


print("Question_7()")
print("Using a built-in function, remove the value 2 from the following list and print\n")
numbers = [1, 2, 3, 4, 5]

numbers.pop(1)  # To remove second list item
print(numbers, '\n')    # print list

print("Question_8()")
print("Using the slice function, print the last element from the following list.\n")
words = ['fizz', 'buzz', 'foo', 'bar']

print(words[3:], '\n')  # print last element of list using slice function

print("Question_9():")
print("Using the slice function, print the value 'c' from the following list\n")
letters = ['a', 'b', 'c', 'd', 'e'] #no marks if slice function not used

print(letters[2:3], '\n')   # print the value 'c' using slice


print("Question_10()")
print("Using the slice function, return the first two element in the list.\n")
letters = ['a', 'b', 'c', 'd', 'e']

print(letters[:2], '\n')    # print the first two elements in the list using slice

print("Question_11():")
print("print the sum of 2 and 3 (use addition).\n")

print(2 + 3, '\n')    # print the sum of 2 plus 3

print("Question_12():")
print("Print the difference of 100 and 1 (use subtraction).\n")

print(100 - 1, '\n')    # print the difference of 100 - 1

print("Question_13():")
print("Print the product of 7 and 5 (use multiplication).\n")

print(7 * 5, '\n')  # print the product of 7 x 5

print("Question_14():")
print("Print the quotient of 10 and 3 (use division).\n")

print(10 / 3, '\n')    # print the quotient of 10 and 3


print("Question_15():")
print("What is the data type of the value returned by: 4 / 2?\n")
#type. Example if your answer is "string" or "list", then return the data
#type like this: `return str` or `return list`.
#return float #OR return type(4/2) also acceptable. 1 mark deduction if you returned a string of
#the type and not the type itself. return "float" is different than return float

print(type(4/2), '\n')   # return the data type of 4/2

print("Question_16():")
print("What is the data type of number 9?\n")

print(type(9), '\n')    # return data type 9

print("Question_17():")
print("What is the data type of the number 3.0?\n")

print(type(3.0), '\n')    # return data type 3.0

print("Question_18():")
print("What is 4 to the power of 3?\n")

print(4**3, '\n')   # print 4 to the power of 3

print("Question_19():")
print("Print the variable `value` as an integer.\n")
value = 1 / 3

print(int(value), '\n') # print 1/3 as an int


print("Question_20():")
print("Print the variable `value` as a float.\n")
value = 2

print(float(value), '\n') # print 2 as a float

print("Question_21():")
print("Print a string containing single quotes.\n")

print('He\'s the man!\n')   # string made using single quotes and contains single quote

print("Question_22():")
print("Print a string containing double quotes.\n")

print("\"He\'s the man!\"\n")   # string made using double quotes and contains double quote

print("Question_23():")
print("Print a string that spans multiple lines.\n")

print(' 1\n 2\n 3\n')    # Printed string that spans multiple lines

print("Question_24():")
print("Using a built-in function, return the following textas all uppercase.\n")
text = 'The quick brown fox jumps over the lazy dog'

text = text.upper()   # return the text in upper with built-in function when text variable is called
print(text, '\n')     # print text as all upper

print("Question_25():")
print("Using a built-in function, print the following text as title case (i.e. every word starts with a capital letter).\n")
text = 'The quick brown fox jumps over the lazy dog'

text = text.title()   # return the text in title[ form with built-in function when text variable is called
print(text, '\n')     # print text in title form

print("Question_26():")
print("Print a string containing the backslash character.\n")

print("This text contains a '\\' character\n")  # Printed text containing a backslash character


print("Question_27():")
print("Print a string containing both single and double quotes.")

print("""This string contains both ' & " characters\n""")   # printed string containing both single and double quotes
print("This string contains both ' & \" characters\n")      # Variation of the same


print("Question_28():")
print("Print a dictionary containing the three most populour Canadian provinces.\n")
print('Use their code as the key, and the full name as the value. Example "AB" - "Alberta"')

prov_dict = {'ON': 'Ontario', 'QC': 'Quebec', 'BC': 'British Columbia'}     # created dictionary of 3 provinces
print(prov_dict, '\n')  # print dictionary

print("Question_29():")
print('Print the value of the key "c" from the dictionary by using the key as the index.\n')
my_dict = {'a': 3, 'b': 2, 'c': 7}

print(my_dict['c'], '\n')   # Print the dict value of c which is 7

print("Question_30():")
print("Extend and print the following dictionary by adding the following key/value pair: b, 10.\n")

my_dict = {'a': 1}
my_dict['b'] = 10

print(my_dict, '\n')  # print the extended dictionary (it was already extended above)

print("Question_31():")
print("Print the unique values from the following list.\n")
my_list = [1, 2, 2, 1, 3, 3, 2]


print(set(my_list), '\n')  # print the set of my_list list



