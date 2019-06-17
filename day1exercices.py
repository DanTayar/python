# #exercice1
# name = input("what is your name?")
# age = input ("what is your age ?")
# shoe_size = input("what is your shoes size ?")
# print ("wow!" ,name, "you are" , age , "and",shoe_size,"is your shoe size" )
# info = ("Hello , my name is {}.I am {} and i have big foot: my shoe size is {}" .format(name, age, shoe_size))
# print (info)


########



# #exercice2
# name1 = input("what is your name?")
# name2 = input("what is the name of the waiter?")
# name3 = input ("{what do you order?")
# price = input("what is the price of the item?")
# number = input("How many item do you order ?")
# answer = int(price) * int(number)
# print ("*" , answer, "*")
# discount = input("Do you have any discount ?")
# print ("**" ,discount, "%  discount **") 
# discount_price = int(answer) * int(discount) /100
# total = int(answer) - int(discount_price)
# print ("***" ,total , "without VAT ***")
# VAT = int(total) * 17 /100
# total_VAT = int(total) + int(VAT)
# print ("****" ,total_VAT , "with VAT *****")

# print ("Hello {}.My name is {}, i was your waiter today.So,you order,{} {}.You got a discount of {}% .That mean you have to pay{} TTC".format(name1,name2, number, name3,discount, total_VAT,))




#exercice3
sentence = input("tape 10 characters : ")
print (len(sentence))

if len(sentence) !=10:
	print ("you have to tape 10 characters")
else: 
	print (sentence)
	list = list(sentence)
	print (list)



