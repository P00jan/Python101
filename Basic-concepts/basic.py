"""Let's learn the basics of Python"""
"""
What is Print and why is it used?
Print is used to show the output to the screen. Anything to display on the screen will be done by Print Funtion
"""
print("Hello, Pythooooon!!!!")

print("02101010")  # numbers or letters must be in " " format in order to be printed

print("This is how you print in \n different lines")

print()  # use this to print an empty line

print("My \n" "Name \n" "is Pythooooon")

"""Variables"""
"""What are Variables? Variable are used to define something. For example A = "Python"
Here we define a variable 'A' and assign it a value Python, variables make things easy when you are doing coding."""

a = ("Hello")
b = ("Python")
print(a + " " + b)

"""Here we define a variable 'a' & 'b' with values then we print those 2 variables with '+' sign in between which 
is nothing but the concatenation of two strings"""

"""Operators and Data Types"""
"""Data Types is nothing but collection of certain groups. For example Alphabets or words are called Strings"""

a = "Hello, Python"  # String
b = 12  # integer
c = 2.5  # Float (Any number with decimal point is called Float)
d = True  # Boolean
e = False  # Boolean

"""Python has 4 types of collection data types"""

f = {"name": "Python",
     "age": 1991,
     "Useful": True}
"""This is called dictionary data type, where you have key:value format. In this case we have name,age and useful as keys
   and respective values to them. Dictionary is a collection which is ordered and changeable. No duplicate members
   Example use cases: representing a mapping of user IDs to usernames, storing configuration settings,
   caching data with keys for quick retrieval."""


g = ["python", "Java", 1921, 1990, True]
"""This is called List data type, which typically works as an array in Python. 
   List is a collection which is ordered and changeable. Allows duplicate members.
   Example use cases: storing a list of tasks, maintaining a history of actions, managing a sequence of elements."""

h = ("Python", "Java", 1990, 1992, False)
"""This is Tuple. Tuple is a collection which is ordered and unchangeable. Allows duplicate members. 
   Example use cases: returning multiple values from a function, representing fixed collections like RGB colors, 
   representing coordinates in a grid."""

i = {"Python", "Java", 1990, 1992, False}
"""This is set data type. Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Example use cases: removing duplicates from a list, checking membership efficiently, 
    performing set operations like intersection or difference."""

""" Use lists when you need an ordered collection that may change.
    Use tuples when you need an ordered collection that should not change.
    Use dictionaries when you need to associate unique keys with values.
    Use sets when you need an unordered collection of unique items or need to perform set operations."""

print(a, "\n",
      b, "\n",
      c, "\n",
      d, "\n",
      e, "\n",
      f, "\n",
      g, "\n",
      h, "\n",
      i)
# This way you would be able to print the variables we used above to assign different data types.

"""OPERATORS
Operators are mathematical signs which can be used for different usecases. 
   1. + : This sign is used to add or concate 2 values.
   2. - : This sign is used to subtract 2 values.
   3. * : This sign is used to multiply 2 values.
   4. ** : This sign is used to do Power of a value.
   5. / : This sign is used to perform division.(Would have the decimal value)
   6. // : This sign is used to perform floor division (Won't leave any decimal value).
   7. % : This sign is used to perform Percentage or get Remainder."""
