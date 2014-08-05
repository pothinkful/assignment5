################################################################################################################################################
# First print "Fizz buzz counting up to n", substituting in the number we'll be counting up to.
# Then the program should print out each number from 1 to some value n, replacing numbers divisible by both 3 and 5 with “fizz buzz”, 
# Those divisible by only 3 with “fizz”, and those divisible by only 5 with “buzz”. Each number goes on a new line.
# v1: Hard Coded Upper Limit
#  [X]   Hard code in 100 as value for upper limit to count up to when the program runs.
#  [X]   Verify your program works by running it from the command line with python my_script.py, substituting in your Python file name
# v2: User Supplied Inputs
#  [ ]   If user supplies value at command line when script runs, we'll use that value.
#  [ ]   Otherwise, we'll use the raw_input() dialogue to get an input from the user.
################################################################################################################################################

num = 0

while (num <= 100):
    if num % 3 == 0:
        print "fizz"
    elif num % 5 == 0:
        print "buzz"
    else:
        print num
    num += 1
