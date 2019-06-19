import sqlite3

def open_database_connection():
    conn = sqlite3.connect('word-games.db')
    return conn

def close_database_connection(c):
    c.close()


def open_file(filename):
    file = open(filename,'r')
    if file.mode == 'r':
        lines = file.read().split()
    file.close()
    return lines


def save_to_db():
    conn = open_database_connection()
    c = conn.cursor()
    word_list = open_file('sowpods.txt')
    query = '''INSERT INTO word_list (word) VALUES (?)'''
    for item in word_list:

        c.execute(query ,(item,))
    conn.commit()
    close_database_connection(c)



# filename = "sowpods.txt"
# print(open_file(filename))
# def main():
save_to_db()
