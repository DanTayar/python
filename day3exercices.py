# #EXERCICE 0

# fav_fruits = input("what is your favorite fruits? : ")
# fruits_list = fav_fruits.split()
# print(fruits_list)
# random_fruit = input("tape the name of a random fruit : ")

# # x = len(fav_fruits)
# # if x > 1:
# # 	final_fruits_list = fruits_list + pop(x) + append("and") + appe

# if random_fruit in fruits_list:
# 	print("you chose one of your favourites fruits ! enjoy 1 !")
# # else:
# 	print("you chose a new fruit. I hope you enjoy it too")


#EXERCICE 1 !!

# def get_age(year , month ):
# 	current_year = 2019
# 	current_month = 5
# 	age = current_year - your_birth_year
# 	if your_month < current_month:
# 		age = age
# 	else:
# 		age = age - 1
# 	return age

# your_birth_year = int(input("what is your your birth year (example:1980) :"))
# your_month = int(input("what is the number of yout birthmonth ?:"))
# print("your age : " , get_age(your_birth_year , your_month))

# def can_retire(sex , date_of_birth):
# 	age = get_age(your_birth_year , your_month)
# 	if age >= 67 and your_sex == "m" :
# 		can_retire = str(" it is "),True ,str("you can retire !! ")
# 	elif age >= 62 and your_sex == "f":
# 		can_retire = str(" it is "),True ,str("you can retire !! ")
# 	else:
# 		can_retire = str(" it is "),False ,str("you can't retire yet !! ")
# 	return can_retire



# your_sex = input("what is yout sex  ? (m or f) :")
# your_date_of_birth = int(input("What is your date of birth ? :"))
# print(can_retire(your_sex , your_date_of_birth))
	

#EXERCICE 2 !!!

# sentense = ("Ne jamais remettre a demain ce qu on peut peta tout de suite. Ne jamais reflechire trop longtemps. Je vais me remettre en question. Je .")
# re_sentense = sentense.split()
# print(re_sentense)

# nbr_char = len(sentense)
# print("there is " , nbr_char , "{characters in this sentensepythoi")


# phrase = sentense.count(".")
# print ("il y a " + str(phrase) + " phrase dans cette phrase.")


# print (len(re_sentense))


# unique_words = []
# for i in re_sentense:
# 	if not i in unique_words:
# 		unique_words.append(i)
# print("there is " , len(unique_words) , "unique words")

# # space = re_sentense.count(" ")
# # print(space) 


# non_unique_words = len(re_sentense) - len(unique_words)
# print("there is" , non_unique_words , " non unique words in this paragraph")

# split_by_dot = sentense.split(".")
# print(split_bydot)


# for i in re_sentense
# 	if i!=:
# 		pass


#EXERCICE 4 !!!

def get_car_manufacturers(manufacturers_list):
	file = open(manufacturers_list, "r")
	if file.mode == "r":
			line = file.read()
	else:
			line = ''

	manufacturers = line.split()
	number_of_manufacturers = len(manufacturers)
	print ("il y a " + str(number_of_manufacturers) + " marque")

		#5 !!

	sorted_manufacturers = (sorted(manufacturers,reverse = True))
	print(sorted_manufacturers)



		#6 

	list_O=[]
	for i in manufacturers:
		if "o" in i:
			list_O.append(i)

	list_i = []
	for i in manufacturers:
		if not "i" in i:
			list_i.append(i)


	print("these are the manufacturers name with an O : ", list_O)
	print(len(list_O))
	print("these are the manufacturers name without an i :" , list_i)
	print(len(list_i))

	#7
	manufacturers = list(dict.fromkeys(manufacturers))
	# print("list without duplicates :" , manufacturers)

	

	file.close()
	return manufacturers



#mainLine
my_manufactures_list = "car_manufacturers.txt"
print(get_car_manufacturers(my_manufactures_list))
# print("list without duplicates :" , manufacturers)




























