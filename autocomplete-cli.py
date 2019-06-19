import sqlite3
# from month2week3day3_exercices import 

def open_database_connection():
	conn = sqlite3.connect('word-games.db')
	return conn

def close_database_connection(c):
	c.close()



class autocomplete():

	def get_autocomplete_list(self,text):
		conn = open_database_connection()
		c = conn.cursor()
		text1 = "{}%".format(text)
		query = ''' SELECT word from word_list where word_list.word like ? limit 10'''
		show = c.execute(query, (text1,))
		show1 = show.fetchall()
		if len(show1)==0:
			print('YOU DIDNT ENTER A WHOLE WORD IN THE LIST')
		else:
			print(show1)
		close_database_connection(c)
		

text = input("entrer un mot ")
autocomplete().get_autocomplete_list(text)