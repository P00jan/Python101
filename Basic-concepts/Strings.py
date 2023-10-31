"""
In python you can use either double or single quotes to define string to the variable
String is the group of characters
"""
message = "Good Morning"
print(message)
# Output: Good Morning

# how to check length of the string?
print(len(message))
# Output: 12

# Some Strings methods
# Remember Strings location starts from 0

# You are printing the character which is located in 1st place
print(message[1])
# ouput : o

# You are printing the character starting from 0th location till 1st location but not including the 1st character
print(message[:1])
# output: G

# You are printing the character which is in last third place of whole string
print(message[-3])
# output: i

# From 0th location till last location but not including it.
print(message[:-1])
# output: Good Mornin

# from 0th location till 5th location and not including it.
print(message[0:5])
# output: Good

# For lower casing all the characters
print(message.lower())
# output: good morning

# For upper casing all the characters
print(message.upper())
# output: GOOD MORNING

# for replacing a word
new = (message.replace("Morning", "night"))
print(new)
# output: Good night

# For concatenating
greeting = "How are you?"
name = "Poojan"
print(greeting + " " + name)
# output: How are you? Poojan
# f strings
print(f"{greeting}" + " "+f"{name}")
# output: How are you? Poojan
