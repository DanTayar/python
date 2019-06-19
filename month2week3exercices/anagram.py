import sqlite3

def open_database_connection():
    conn = sqlite3.connect('word-games.db')
    return conn

def close_database_connection(c):
    c.close()

def find_anagrams():
	conn = open_database_connection()
    c = conn.cursor()
    text1 = "%{}%".format(text)
    query = ''' SELECT word from word_list '''
	

s1=input("Enter first string:")
s2=input("Enter second string:")
if(sorted(s1)==sorted(s2)):
      print("The strings are anagrams.")
else:
      print("The strings aren't anagrams.")