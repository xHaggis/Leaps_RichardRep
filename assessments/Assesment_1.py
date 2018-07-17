#WHEN FINISHED EMAIL THIS TO: tfk2@hw.ac.uk

# # Question A
# Variables and conditions
#
# write a function that checks if a number is a multiple of:
# - 3 and outputs "fizz" if this is true.
# - 5 and outputs "buzz" if this is true.
# - 10 and outputs "banana" if this is true.
# - otherwise return the square of the number
#
# Tips:
# - First try to solve this using maths then write it in code.
# - Look at the asserts they describe what I am expecting as output.
# - What happens when the number is 30 or 21



def fizz_buzz_banana(n):
    output = ""
    return output


# check if your function works
print(fizz_buzz_banana(3))

assert fizz_buzz_banana(1) == 1
assert fizz_buzz_banana(2) == 4
assert fizz_buzz_banana(3) == "fizz "
assert fizz_buzz_banana(5) == "buzz "
assert fizz_buzz_banana(10) == "buzz banana"
assert fizz_buzz_banana(30) == "fizz buzz banana"


# # Question B (2 points)
# Loops and list
#
# Write a function that checks wether there are immediate adjecent pairs of numbers in a list.
# If there is a immediate adjecent pair then add this number (not the sum of these numbers!) to the sum of the list.
#
# For example:
# - `[1,1,2,2]` returns 3
# - `[1,1,1,1]` returns 3
# - `[1,2,3,4]` returns 0
# - `[1,2,1,2]` returns 0
# - `[1,2,3,1]` returns 0
# - `[9,1,2,3,4,5,6,7,8,9]` returns 0
#
# Tips:
# - one loop should be enough or not?


def sum_doubles(numbers):






print(sum_doubles([1,1,2,2]))


assert sum_doubles([1,2]) == 0
assert sum_doubles([1,1,2,2]) == 3
assert sum_doubles([9,1,2,3,4,5,6,7,8,9]) == 0
assert sum_doubles([9,10,20,30,40,50,60,70,80,9,
                    109,11,22,33,44,55,66,77,88,99,
                    119,21,32,43,54,65,76,87,98,19,
                    129,31,42,53,64,75,86,97,18,29,
                    139,41,52,63,74,85,96,17,28,39,
                    149,51,62,73,85,95,16,27,38,49,
                    159,61,72,83,94,15,26,37,48,59,
                    169,71,82,93,14,25,36,47,58,69,
                    179,81,92,13,24,35,46,57,68,79,
                    189,91,12,23,34,45,56,67,78,89]) == 0


###########################################################################################

'''
Multiple choice question:
PLEASE PUT YOUR ANSWER BELOW EACH QUESTION

Q1. What is special about the variables in Python:
A) Variables are not declared with a type and can switch type easily
B) Variables are declared with a type and cannot switch type easily

Q2. What is the difference between class and instance variables:
A) Class variables are declared in a class and work for all
   instances of the class. When class variables are changed they change for
   all instances. Instance variables are declared outside of the class,
   when changed only change for the instances.
B) Class and instance variables are declared inside the class and when changed,
   change for both class and instance.
C) Class and instance variables are declared inside the class. When class
   variables are changed they change for all instances. When instance variables
   are changed only change for the instances.


Q3. What is the difference between a for loop, a while loop and a do while loop:
A) There is no difference between a for loop and a while. However, a do-while
   loop executes the code inside the loop at least once
B) For loops are declared with a range, while and do while only have a condition
   that should be met. While loops execute the code inside the loop at least
   once.
C) For loops are declared with a range, while and do while only have a condition
   that should be met. Do-while loop executes the code inside the loop at least
   once.

WHEN FINISHED EMAIL THIS TO: tfk2@hw.ac.uk
'''
