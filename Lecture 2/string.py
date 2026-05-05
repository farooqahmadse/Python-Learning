# # string can be in many wasy

# # 1.

# name = 'python'
# name2 = "python"
# name3 = '''python'''


# # all are same but there is some thing that need to be understand why we are using it

# name4 = "FAROOQ'S CAR"  # We cannot use this like in single quotation marks 'Farooq's'


# name5 = '''Hi i am software engineer and i am learning python after working in many other language

# so it easy and fun
# '''


# # String concatenation
# # we can add two string in python and it called string conatenation
# firstname = 'farooq'
# lastname = 'ahmad'
# print(firstname+lastname)


# # length of string


# country = 'Pakistan'

# print(len(country))


name = input('Enter your name: ') 
print('Hello',name)
# it will remove the extra space from the start and end of the string

name =name.strip() 
print('Hello',name)

name=name.capitalize() # it will capitalize the first letter of the string
print('Hello',name)
name=name.title() # it will capitalize the first letter of each word in the string
print('Hello',name)

print(f"Hello, {name}") 