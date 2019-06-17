


# def book_seat():
# 	pass






# def pay_for_tickets():
# 	pass





# def show_bus_info():
# 	pass			






# def show_menu():
# 	for x in range(1,100):
# 		print("(a)-Book a seat")
# 		print("(b)-Pay for a ticket")
# 		print("(c)-View information about the bus")	
# 		print("(d)-Exit")
# 		ask_the_user = input("Select an option please :(a , b , c or d) ").lower()
	
# 		if ask_the_user == 'a':
# 			book_seat()
# 		elif ask_the_user == 'b':
# 			pay_for_tickets()
# 		elif ask_the_user == 'c':
# 			show_bus_info()
# 		elif ask_the_user == 'd':
# 			print("GOODBYE")
# 			exit()
# 		else:
# 			print("error message ! Please enter a, b, c or d")







# def main():
# 	welcome_message = "Hello , Welcome !!"
# 	print(welcome_message)
# 	show_menu()
# 	parting_message = " GOODBYE ! "
# 	print(parting_message)




# main()



#6

# def book_seat(filename):
# 	file = open(filename, "a")
# 	if file.mode == "a":
# 		line = file.write()
# 	else:
# 		line = ''

# 		seat_list = line.split()
# 		print(seat_list)
# 	if number_of_seat < 10: 
# 		confirmation = print("Please confirm that you want to book a seat ? y to confirm or n to cancel : ")
# 		if confirmation == 'y':
# 			seat_list.append("x")
# 		else:
# 			print("you did not book your seat")
# 	else:
# 		print("there is no seat avaiable")
# 	file.close()
# 	return seat_list

import random


def book_seat():
	seat_list = ['x','','','x','','x','x','','','x']
	counter = 0
	for x in seat_list:
		if x == '':
			print("there are seats avaiable")
			confirmation = input("please confirm you want to book a seat on the bus . Tape y to confirm or n to cancel : ")
			if confirmation == 'y':
				print(seat_list)
				seat_list[counter] = 'x'
				counter = counter + 1
			else:
				exit()
		pay_for_tickets()	




def pay_for_tickets():
	pass





def show_bus_info():
	print("make: Mercedes, model:d200, year:2006 ")	
	print("the bus has 10 seats")		






def show_menu():
	for x in range(1,100):
		print("(a)-Book a seat")
		print("(b)-Pay for a ticket")
		print("(c)-View information about the bus")	
		print("(d)-Exit")
		ask_the_user = input("Select an option please :(a , b , c or d) ").lower()
	
		if ask_the_user == 'a':
			book_seat()
		elif ask_the_user == 'b':
			pay_for_tickets()
		elif ask_the_user == 'c':
			show_bus_info()
		elif ask_the_user == 'd':
			print("GOODBYE")
			exit()
		else:
			print("error message ! Please enter a, b, c or d")







def main():
	welcome_message = "Hello , Welcome !!"
	print(welcome_message)
	show_menu()
	parting_message = " GOODBYE ! "
	print(parting_message)



# filename = 'seat_list.txt'
main()




























