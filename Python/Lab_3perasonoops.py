class Person():
    def __init__(self):
        pass
    def walk(self):
        print("Walking")
class Staff():
    def __init__(self):
        pass       
    def work(self):
        print("Working")
class BusDriver(Person,Staff):
    def __init__(self):
        pass
    def driving(self):
        print ("driving bus")
s=Staff()
b=BusDriver()
b.walk()
b.work()
b.driving()
