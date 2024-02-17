"""Conditional statements consists of the following:
1. If statement
2. If-else Nested statements
3. For Loop statements
4. Nested Loop statements
5. While Loop statements"""

"""If and Nested If else statements is used when You have to choose between 1 or multiple options. 
For and example someone say if you are above 15 yr old You get a fruit and if you are below 15 yr old you get a chocolate.
So that means you say what age you are and in that order you get either a fruit or a chocolate."""

import time
ask_user = int(input("What is your age?\n"))
if ask_user > 15:
    print("You get a fruit")
else:
    print("You get a chocolate")

""" Based on a numeric grade input (0-100),use If-Else to assign a letter grade 
according to the following ranges: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60)."""

grade_input = int(input("Enter your grade:\n"))
if 90 <= grade_input <= 100:
    print("You get an \"A\"")
elif 80 <= grade_input < 90:
    print("You get a \"B\"")
elif 70 <= grade_input < 80:
    print("You get a \"C\"")
elif 60 <= grade_input < 70:
    print("You get a \"D\"")
else:
    print("You get a \"F\"")

"""Write a program that calculates a discount based on the purchase amount: 10% off for $100 or more,
 5% off for $50-$99, and no discount for below $50. Output the discounted price."""

Item_price = int(input("Enter the amount:\n"))
if Item_price >= 100:
    discount_amount = 10
elif 50 <= Item_price < 90:
    discount_amount = 5
else:
    discount_amount = 0

discount_price = (Item_price - (Item_price * (discount_amount/100)))
print(f"Your final price is {discount_price}$")


"""For loops and nested For loops: For loops are nothing but looping or iterating over an item provided.
Basically you say loop through an item for 2 times and then exit the code and print loop ended is what for loop is"""

for i in range(2):
    print("Looped")
print("Loop ended")

"""Write a program to calculate the factorial of a given number using a for loop."""
number = int(input("Enter the number: "))
factorial = 1
for i in range(1, number + 1):
    factorial *= i
print(factorial)

"""Explanation: we set the factorial to 1 so that we can multiply the i and save it in factorial,
there is no logic here other than using 1 and number + 1 which is simply number starting from 1 and adding a limit to number+1 i.e 
till the number itself eg: for 5 we have starting point 1 and ending point 6 (5+1) but it will count till 5. """

"""Generate a multiplication table for a given number up to a certain range using nested for loops."""
