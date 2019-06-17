def showAllView(list):
   print('In our db we have %i users. Here they are:', len(list))
   for item in list:
      print(item.id,item.name(),item.phone)
def startView():
   print('MVC - the simplest example')
   print('Do you want to see everyone in my db?[y/n] or add an entry ?[a]')
def endView():
   print('Goodbye!')