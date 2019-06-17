from model_example import Person
import view_example as view

def showAll():
   #gets list of all Person objects
   # people_in_db = Person.getAll()
   #people_in_db = Person.getallDB()
   people_in_db = Person.getAllFirestore()
   #calls view
   return view.showAllView(people_in_db)

def start():
   view.startView()
   answer = input()
   if answer == 'y':
      return showAll()
   if answer == 'a':
      first_name = input("what is your first name?")
      last_name = input("what is your last name ?")
      phone = input("what is your phone number ?")
      return Person.addNewFirestore(first_name, last_name,phone)

   else:
      return view.endView()

if __name__ == "__main__":
   #running controller function
   start()