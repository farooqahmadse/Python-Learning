# # Print numbers from 1 to 5 using a loop.

# for i in range(1,6):
#     print(i)

# # Q2 — FOR LOOP (range)

# # Print numbers from 0 to 9.

# for z in range(10):
#     print(z)

# # 🔹 Q3 — Custom range

# # Print numbers from 5 to 15.
# for j in range(6,16):
#     print(f"the  number 5 to 15 : {j}")

# # 🔹 Q4 — EVEN NUMBERS

# for u in range(1,21):
#     if u%2==0:
#         print (f'th even number is : {u}')



# # 🔹 Q5 — SUM USING LOOP

# # Find sum of numbers from 1 to 10.
# toplam=0
# for k in range(1,11):
#     toplam=toplam+k    
#     print(toplam)

# # 🔹 Q6 — WHILE LOOP (basic)

# # Print numbers from 1 to 5 using while loop.
# i=1
# while i<=5:
#     print(i)
#     i+=1
    

# # 🔹 Q7 — WHILE LOOP (manual counter)

# # Print numbers from 10 to 1 (reverse order).

# i=10
# while i>=1:
#     print(i)
#     i-=1

# #------------- Q8 — MULTIPLICATION TABLE-----------------------------

# # Take a number from user and print its table (1 to 10).
 
# numberfromuser =int(input("write any number: "))

# for i in range(1,11):
#     print(numberfromuser,"x",i,'=', numberfromuser*i)




# #--------------------Q9 — COUNT DIGITS (loop concept)--------------------

# # Take a number and count how many digits it has.

# # Example:

# # Input: 12345
# # Output: 5
# userinpt=int(input('write a random number:'))
# print(len(userinpt))



# #------------------ Q10 — BREAK LOOP-------------------------

# # Print numbers 1 to 10 but stop when number is 6.



# # ------------------ Q11 — CONTINUE LOOP---------------------

# # Print numbers 1 to 10 but skip number 5.

# # Your Answer:

# # 🔹 Q12 — PATTERN (VERY IMPORTANT)

star=0
for i in range(5):
    star+=i
    print(star*"*")

# *
# **
# ***
# ****
# *****

# Your Answer:

# 🔹 Q13 — PATTERN REVERSE

# Print:

# *****
# ****
# ***
# **
# *

# Your Answer:

# 🔹 Q14 — LOOP + CONDITION

# Print numbers from 1 to 20 but only show numbers divisible by 3.

# Your Answer:

# 🔹 Q15 — MINI CHALLENGE

# Take a number n from user and print:

# all numbers from 1 to n
# their sum at the end       