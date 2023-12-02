"""
What is Function?
A program which contains group of statements to be executed in the one block, mostly intended for doing specific tasks. Also known as resuable code as you can use it again and again.

Syntax: 
def functionname(parameter 1, parameter 2 , ..., parameter n):
    Function logic and statements to be executed here.
funtionname(arguments passed to function) # this is called calling the function
"""
def sum(a,b):
    c = a + b
    print (c)
sum(a = 1,b = 2)
sum(12,2)
sum(1.55,2.58)
#Output will be 3 , 14 and 4.13 
#Same goes with anything or any operations you write.
#we can use the sum to call funtion multiple times to establish that it is resuable.
"""
What is Return in Function?
Well, return is similar to print but we return the result to the body of the funtion. To understand this imagine you want to use the function and want to return in 2 different variables.
"""
def subtract(a,b):
    c = a - b
    return c
x = subtract(10 , 2) # calling the subtract function and storing it in a variable x 
print(f"The answer for x variable is: {x}" )
y = subtract(8 , 4) # calling the subtract function and storing it in a variable y
print(f"The answer for y variable is: {y}")
"""
Output will be: 
The answer for x variable is: 8
The answer for y variable is: 4
"""


"""
Write a code to test whether a number is odd or even.
"""
def check_number(a):
    if a % 2 == 0:
        print(f"The number {a} is even")
    else:
        print(f"The number {a} is odd")#printing the answer for the output for the user.
    return a 
number_1 = int(input("Enter a number to test: ")) # Take a user input 
number_1 = check_number(number_1) #call function
number_2 = int(input("Enter a number to test: "))
number_2 = check_number(number_2)

"""
Output:
Enter a number to test: 10
The number 10 is even
Enter a number to test: 9
The number 9 is odd
"""

"""
Let's make a program where we are using functions to ask user about their income and then calculate the tax amount on it.
We will by default use the NJ Tax criteria which is as follows also user will only provide the salary less than or equal to 10K$:
Federal	10.00%	1.91%	
FICA	7.65%	7.65%	
State	1.40%	1.31%
"""

salary_amount = int(input("Enter your salary amount: "))
Federal = 1.91%
def main():
    name = input("Enter your name: ")
    if salary_amount > 10000:
        print("Please enter a salary amount less than or equal to 10000:")
    else:
        return (salary_amount,name)
main()

def calculate():
    
    

