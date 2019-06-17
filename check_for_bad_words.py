def get_a_sentence():
	#dothis
	linein = input("what is your sentence to check?")
	return linein

def check_for_bad_words(sentence_to_check):
	#do this
	bad_words = ['hell' , 'damn', 'shit']
	words = sentence_to_check.split()
	dirty = False
	for each_word in words:
		if each_word in bad_words:
			dirty = True
	return dirty

#Main line
for counter in range(5):
	#get a sentence
	sentence = get_a_sentence()
	#check for bad works
	if check_for_bad_words(sentence):
		print("stop writing bad words !!")
	else:
		print("you typed a clean sentence")
	#do something