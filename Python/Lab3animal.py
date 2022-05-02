class Animal():
    def __init__(self):
        pass
    def eat(self):
      print ("eating..nom..nom")

class Horse(Animal) :
    def __init__(self):
        Animal.__init__(self)
        pass
    def neigh(self):
      print("neigh!") 
    
      
class Dog(Animal):
    def __init__(self):
        Animal.__init__(self)
        pass

    def bark(self):
     print("voofvoof!")