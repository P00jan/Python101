"""
Condition Statements are one of the basic use cases in the programming.
These helps us to develop a program which is more efficient and it can choose what output to give on the basis of conditions Developer has set.
In these we will learn about following topics:
    1. If statement
    2. If-Else statement
    3. Nested If-Else statements
    4. For loop statements
    5. While loop statements
"""
"""
In this we will learn about Condition statements and Control statements in Python
"""
# If - else statements
name_1 = "Poojan"
name_2 = "Raj"
L1 = ["Raj", "Amit", "Helly ", "Rishita"]
if name_1 == "Poojan" in L1:
    print(name_1)
else:
    print(f"{name_1} is not in the List")
if name_2 == "Raj" in L1:
    print(f"{name_2} is in the List ")
else:
    print(f"{name_2} is not in the List")

    """
    Output:
    Poojan is not in the List
    Raj is in the List 
    """
"""You can also use nested el-if statements"""

l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [1, 2, 3, 4]

if l1 == l2:
    print(True)
elif l1 == l3:
    print(True)
else:
    print(False)
"""
Output:
True
Reason is program will check one condition and then will go to next condition, el-if is simply nothing but asking code if not that then is this condition fulfilled?
"""

"""
Control statements includes of 2 loops: For and While statements
"""
l1 = [1, 2, 3, 4, 5, 6, 7, 8]
for i in l1:
    if 2 in l1:
        print(f"Number is found")
    elif 9 in l1:
        print("Number is not found")
