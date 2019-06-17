#EXERCICE 1 !!!


# first_list = []
# for x in range(0,10):
# 	first_list.append(x)
# print(first_list)
# second_list = []
# for x in range(1,11):
# 	second_list.append(x)
# print(second_list)
# third_list = []
# for x in range(-9,5):
# 	third_list.append(x)
# print(third_list)
# forth_list = []
# for x in range(10,4,-1):
# 	forth_list.append(x)
# print(forth_list)
# fifth_list = []
# for x in range(1,14,+2):
# 	fifth_list.append(x)
# print(fifth_list)
# sixth_list = []
# for x in range(2,8):
# 	sixth_list.append(2**x)
# print(sixth_list)
# main_list = first_list + second_list + third_list +forth_list + fifth_list + sixth_list
# print(main_list)


# message = ("keep calm and carry on")
# number = input("choose your number")
# for x in range(int(number)):
# 	print(str(x+1) + ":" + message)



#EXERCICE 2 !!

# first_list = []
# x = 1.5
# while x<5.5:
# 	first_list.append(x)
# 	x +=0.5
# print (first_list)



#EXERCICE 3 !!!

# list1 = [3, 47, 99, -80, 22, 97, 54, -23, 5, 7]
# list2 = [44, 91, 8, 24, -6, 0, 56, 8, 100, 2]
# list3 = [3, 21, 76, 53, 9, -82, -3, 49, 1, 76]
# list4 = [18, 19, 2, 56, 33, 17, 41, -63, -82, 1]
# final_list = list1 + list2 + list3 + list4
# print(sorted(final_list))
# final_list = sorted(final_list)
# # 3

# sum = 0
# for num in final_list:
# 	sum = sum +num
# print("the sum of the final_list is :" ,sum)

# #4

# litle_list = [final_list[0], final_list[-1]]
# print('the first and the last numbers of this list are :' ,litle_list)

#5

# greater_list = []
# k = 50
# for x in final_list:
# 	if x > k:
# 		greater_list.append(x)

# print("the numbers greater than 50 are : " ,greater_list)

# #6

# smaller_list = []
# i = 10
# for x in final_list:
# 	if x < i :
# 		smaller_list.append(x)

# print("the numbers smaller than 10 are :" ,smaller_list)

# #7

# squared_list = []
# for x in final_list:
# 	squared_list.append(x**2)
# print("this is the squared list",squared_list)

# #8
# final_list = list(dict.fromkeys(final_list))
# print("this is a list without duplicate numbers" ,final_list)


# #9
# print(len(final_list))
# average = sum / len(final_list)
# print("this is the average for the number in the list :", average)

# #10 
# largest_number = final_list[-1]
# print("the largest number of the list is : " ,largest_number)

# #11
# smallest_number = final_list[0]
# print("the smallest number of the list is : " ,smallest_number)



 #EXERCICE 3 !!!
# def triangle(n): 

#     # number of spaces 
#     k = 2n - 2

#     # outer loop to handle number of rows 
#     for i in range(0, n): 

#         # inner loop to handle number spaces 
#         # values changing acc. to requirement 
#         for j in range(0, k): 
#             print(end=" ") 

#         # decrementing k after each loop 
#         k = k - 1

#         # inner loop to handle number of columns 
#         # values changing acc. to outer loop 
#         for j in range(0, i+1): 

#             # printing stars 
#             print(" ", end="") 

#         # ending line after each row 
#         print("\r") 

# # Driver Code 
# n = 5
# triangle(n)
 

#EXERCICES 4 !!!
#1

import random

# secret_number = random.randint(1, 100)
# guess_number = int(input("pick a number between 1 and 100: "))
# if guess_number != secret_number:
# 	print("You didn't enter the proper number !!! The good number is : " ,int(secret_number))
# else: 
# 	print("you choose the good number ! CONGRATULATIONS !")

#2

secret_number = random.randint(1,100)
number_try = 10
# guess_number = int(input("pick a number between 1 and 100 :"))
for number in range(0,number_try):
	guess_number = int(input("pick a number between 1 and 100 :"))
	if guess_number > secret_number:
		print("you didnt ener the good number ! the number is LOWER ")
		number_try = number_try - 1
		print("less" , number_try , "left")
	elif guess_number < secret_number :
		print("you didnt ener the good number ! the number is HIGHER ")
		number_try = number_try - 1
		print("less" , number_try , "left")
	else:
		print("you finally got the good answer ! CONGRATULATIONS")













