# this is my grocery list
linein = input("what is the number of items in your list?")
bad_list = ['meat', 'chicken', 'beef', 'duck', 'turkey', 'bison']
new_item_list = [] 
try:
	number = int(linein)
	counter = 0
	while  counter < number:
		message = "what is the"+str(counter)+" item in the list?"
		new_item = input(message)
		if new_item.lower() in bad_list:
			print('you are vegetarian!!')
		else:
			new_item_list.append(new_item)
			counter = counter + 1
except:
	print("you didnt enter in any valid number!!!")
print(new_item_list)