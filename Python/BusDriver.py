from Person import *
from Staff import *
class BusDriver(Person,Staff):
    def __init__(self):
        pass
    def driving(self):
        print ("driving bus")

#s=Staff()
b=BusDriver()
b.walk()
b.work()
b.driving()    