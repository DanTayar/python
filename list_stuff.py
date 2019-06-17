first_list = [1,2,3,4,5]
second_list = ['a', 'b' ,3.14, 10, 'this is a test']
print("1: ", first_list)
print("2: ", second_list)
third_list = first_list+second_list
first_list.extend(third_list)
fourth_list = first_list
print("3: ", third_list)
print("4: ", fourth_list)

sentence = input('How are you feeling today?')
my_words = sentence.split()
if my_words[0] == 'I':
	print('you really think about yourself!')
else:
	print('have a good day')



sentence2 = input('tell me about yourself ?')
my_next_list = sentence2.split()
if 'shit' in my_next_list:
	print('STOP SWEARING !!!')
elif 'I' in my_next_list:
	print("It is good you're focused on yourself")
elif 'bad' in my_next_list:
	print('i hope your day gets better')



