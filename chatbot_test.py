def read_json_script(name_of_json_file):
	# this function takes a file (like text file) and converts the string to a dictionary
	# this is the way python accepts json.  json is just a dictionary format in a text file. 
	import json
	file = open(name_of_json_file, "r")
	#2. Check the file is available
	if file.mode == 'r':
		#3. Read
		lines = file.read()
		# this takes the text and converts to json format (which is really a python dictionary)
		my_dict = json.loads(lines)
	else:
		lines = ''
		my_dict = {}

	file.close()
	return my_dict

def get_language():
	ask_user_language = input("what is your language you speak :? ")
	if ask_user_language in my_dict:
		language = ask_user_language
	else:
		print("You didn't enter in a proper language !!! I am going to assume english")
		language = 'en'

		return language 





	# try:
	# 	user_language = input("what is your language :? ")
	# except ValueError:
	# 	print("You didn't enter in a proper language !!! I am going to assume english ")
	# 	user_language = english
		





















#MAINLINE !!
name_of_json_file = 'languages.json'
languages = read_json_script(name_of_json_file)
print(languages)
print(language)
