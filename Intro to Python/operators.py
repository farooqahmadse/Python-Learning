# Operator
# An operator is a symbol that performs a certain operation between operands.


# Arithmatic Operator: {+(sum), -(subtract), *(multiply), /(divide), %(reminder), **(power)}


# examples

a = 10
b = 3

sum = a+b
print("The sum of a and b is: ", sum)


subtraction = a-b
print("The sum of a and b is: ", subtraction)

division = a/b
print("The division of a and b is: ", division)

product = a*b
print("The product of a and b is: ", product)

modulas = a % b
print("The modulas of a and b is: ", modulas)

power = a**b
print("The power of a and b is: ", power)

# RELATIONAL OPERATOR/ COMPARISON OPERATORS: {==,!=, >, <, >=, <=}

# examples
a = 20
b = 44
# 1.
equal = a == b
# if  a and b is equal then it will print out True if not it will print false
print(equal)

# 2.
notequal = a != b
print(notequal)

# 3.
greaterthan = a > b
print(greaterthan)

# 4.
lessthan = a < b
print(lessthan)

# 5.
lessthanorequal = a >= b
print(lessthanorequal)

# 6.
greaterorequal = a <= b
print(greaterorequal)


# Assignment Opertors : {=, +=,-=, *=, /=,%=, **=}
# 1.
a = 5

# 2.
a += 10
print('add 10 to varibale a: ', a)

# 3.
a -= 3
print('subtract 3 from variable a:', a)

# 4.
a *= 4
print('multiply 4 with variable a:', a)

# 5.

a /= 4
print('divied 4 with variable a:', a)

# 6.
a %= 4
print('mod 4 with variable a:', a)

# 7.
a **= 4
print('power 4 with variable a:', a)


# Logical Operators: (not, and, or)


# 1.
# NOT OPERATPT WILL RETURN OPPSITE , it works on one operator
bool1 = True
bool2 = True
print("the no operator is:", not bool1)  # Outputs: False because bool1 is True


# 2.
# AND operator, IT WORKS ON TWO OPERTORS
val1 = 10
val2 = 20
print('the answer of AND operator is: ', val1 and val2)


# 3.
# OR, IT WORK ON TWO OPERATORS

print('OR OPERATOR:', (val1 == val2) or (val2 > val1))


# type function in python

school = "Sir Syed Public School"
teachers = 30
admissionfee = 3.9


print('the type of school is:', type(school))
print('the type of teachers is:', type(teachers))
print('the type of admissionfee is:', type(admissionfee))
