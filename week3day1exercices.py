#EXERCICE 1 

# import random
# def get_random_temp():
# 	random_temperature = random.randint(-10, 40)
# 	return random_temperature

# def main():
# 	grt = get_random_temp()
# 	print ("the tempperature right now is :", get_random_temp() ,  "degres celsus.")
# 	if grt < 0 :
# 		print("BRRRR that is freezing 1111")
# 	elif 0< grt <16:
# 		print("Quitte chilly! dont forget yout coat")
# 	elif 16 < grt < 23:
# 		print("it is quite HOT")
# 	elif 23<grt<32:
# 		print("it is HOT")
# 	elif 32<grt<40:
# 		print("TO HOOTTT")


# main() 




# #4
# import random
# def get_random_temp(season):
# 	if season == 'winter':
# 		random_temperature = random.randint(-10, 10)
# 	elif season == 'autumn':
# 		random_temperature = random.randint(11,16)
# 	elif season == 'spring':
# 		random_temparure = random.randint(17, 23)
# 	elif season == 'summer':
# 		random_temperature = random.randint(24,40)


# 	return random_temperature

# def main():
# 	season = input("What is the season ?(winter,spring,sumnmer or autumn) ")
# 	grt = get_random_temp(season)
# 	print ("the tempperature right now is :", get_random_temp(season) ,  "degres celsus.")
# 	if grt < 0 :
# 		print("BRRRR that is freezing 1111")
# 	elif grt >= 0 and grt <=16:
# 		print("Quitte chilly! dont forget yout coat")
# 	elif grt>=17 and grt <=23:
# 		print("it is quite HOT")
# 	elif grt>=24 and grt <=31:
# 		print("it is HOT")
# 	elif grt >=32 and grt <=40:
# 		print("TO HOOTTT")


# main() 


#6 
#4
# import random
# def get_random_temp(month):
# 	if month < 3:
# 		random_temperature = random.randint(-10, 10)
# 	elif month >= 3 and month<6:
# 		random_temperature = random.randint(11,16)
# 	elif month >=6 and month<9:
# 		random_temperature = random.randint(24, 40)
# 	elif month >=9 and month <12:
# 		random_temperature = random.randint(17,23)

# 	return random_temperature

# def main():
# 	month = int(input("What is the number of the current month ? (1 to 12 ) : "))
	
# 	grt = get_random_temp(month)
# 	print ("the tempperature right now is :", get_random_temp(month) ,  "degres celsus.")
# 	if grt < 5 :
# 		print("it is WINTER : BRRRR that is freezing 1111")
# 	elif grt >= 5 and grt <=16:
# 		print(" it is AUTUNM : Quitte chilly! dont forget yout coat")
# 	elif grt>=17 and grt <=23:
# 		print("It is SPRING : it is quite HOT")
# 	elif grt>=24 and grt <=40:
# 		print("It is SUMMER : it is HOT")



# main() 




#EXERCICE 2 !!!!!

# import random

# def throw_dice():
# 	random_number = random.randint(1, 6)
# 	return random_number

# def throw_until_doubles():
# 	counter = 0
# 	while True:
# 		counter = counter +1
# 		first_throw = throw_dice()
# 		second_throw = throw_dice()
# 		print(first_throw)
# 		print(second_throw)
	
# 		if first_throw == second_throw:
# 			print("vous avez reussit en " , counter, "essais")
# 			break
# 		else:
# 			continue
		

	

# throw_until_doubles()



#3

import random

def throw_dice():
	random_number = random.randint(1, 6)
	return random_number

def throw_until_doubles():
		counter = 1
		first_throw = throw_dice()
		second_throw = throw_dice()
		while first_throw != second_throw:
			counter += 1
			first_throw = throw_dice()
			second_throw = throw_dice()
		
		return counter , first_throw , second_throw

def throw_until_double2():  # to return only the counter parameter
    first_throw = throw_dice()
    second_throw = throw_dice()
    counter = 1
    while first_throw != second_throw:
        counter += 1
        first_throw = throw_dice()
        second_throw = throw_dice()

    print(f"Dices were thrown {counter} times and we got the double {first_throw,second_throw}")
    return counter

def main():
    results = []
    for _ in range(100):
        results.append(throw_until_double2())
    total = 0
    for i in results:
        total = total + results[i]
    print(f"\n-------------------------\n-------------------------\n\nDices were thrown {total} times to obtain 100 doubles")
    av = total/100
    print(f"We have to throw an average of {av} times to obtain a double\n-------------------------\n-------------------------\n")

main()
	
		
		

	















