# Write a function is_even that will return true if the passed-in number is even.

# YOUR CODE HERE

def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# Read a number from the keyboard
num = input("Enter a number: ")
num = int(num)

# Print out "Even!" if the number is even. Otherwise print "Odd"
# YOUR CODE HERE

def check_num(number):
    if is_even(number) == True:
        print("Even!")
    elif is_even(number) == False:
        print("Odd")

check_num(num)