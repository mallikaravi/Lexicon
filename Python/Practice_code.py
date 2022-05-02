

# name = input("what is your name? ")
# print("Hello"+ name)

# birth_year=input("Enter your birth year:")

# age=2022-int(birth_year)
# print(age)

# first=input("First")
# second=input("second")
# sum=int(first)+int(second)
# print("sum:" +str(sum))

# course="Python forbeginners"
# print(course.upper())
# print(course.find('for'))
# print(course.replace('t','4'))
# print('Python' in course)


# temperature=25
# if temperature>30:
#     print("Its a hot day") 
#     print("drink plenty of water")
# elif temperature>20:
#     print("Its a nice day")
# elif temperature>10:
#     print("Its bit cold")
# else:
#     print("Its cold")
# print("Done")


# weight=int(input("Weight:"))
# unit=input("(K)g or (L)bs:")
# if unit.upper()=="K":
#     converted=weight/0.45
#     print("Weight in Lbs:"+str(converted))
# else:
#     converted=weight*0.45
#     print("Weight in kgs:"+str(converted) )   

# names= ["John","Bob","Mary"]
# names[0]="Jon"
# print(names[-1])
# print(names)
# print(names[0:3])

#numbers=[1,2,3,4,5,6]
# numbers.insert(0,-1)
# print(numbers)
# print(10 in numbers)#prints false
# print(len(numbers))

# for item in numbers:
#     print(item)


# numbers=range(5,10,2)
# for number in numbers:
#     print(number)
#numbers =(1,2,3)

# fullname="John Smith"
# age=20
# is_new=True
 
# first="John"
# second="Smith"
# message=f'{first} [{second}] is a coder'
# print(message)

# price=1000000
# has_good_credit=True

# if has_good_credit:
#     down_payment=0.1*price
# else:
#     down_payment=0.2*price
# print(f"Down payment:${down_payment}")

# has_high_income=True
# has_good_credit=True
# if has_high_income or has_good_credit:
#     print("Eligible for loan") 

 
#OOps in python

# class Person():
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         return f"Hi,its{self.name}"
# Person=Person("John",23) 

# print(Person.greet())

# class Employee:
#     def __init__(self,first,last,pay):
#         self.first=first
#         self.last=last
#         self.pay=pay
#         self.email=first+'.'+last+'@company.com'
#     def full_Name(self):
#         return '{} {}'.format(self.first,self.last)

# emp_1=Employee('corey','Ravi',60000)
# emp_2=Employee('Test','Ravi',65000)

# print(emp_1)
# print(emp_2)


# print(emp_1.email)
# print(emp_2.email)

# print('{} {}'.format(emp_1.first,emp_1.last))
#print(emp_2.full_Name())
#print(Employee.full_Name(emp_1))

#OOPs
# class Car:
#     pass


# ford=Car()#instance of a class
# honda=Car() 
# audi=Car()  

# ford.speed=200#adding attributes
# honda.speed=220
# audi.speed=250
# ford.color='red'
# honda.color='blue'
# audi.color='white'

# print(ford.color)
# print(ford.speed)
# ford.speed=300
# ford.color='green'
# print(ford.color)
# print(ford.speed)


# class Rectangle:
#     def __init__(self,height,width):
#         self.height=height
#         self.width=width
    
# rect1=Rectangle(20,60)
# rect2=Rectangle(50,40)

# print(rect1.height*rect1.width)

# class Car:
#     def __init__(self,speed,color):
#         print(speed)
#         print(color)
#         self.speed=speed
#         self.color=color
#         print("The init methodis called")

# ford=Car(200,'red')#instance of a class
# honda=Car(234,'blue') 
# audi=Car(345,'red')  

# # ford.speed=200#adding attributes
# # honda.speed=220
# # audi.speed=250
# # ford.color='red'
# # honda.color='blue'
# # audi.color='white'

# # print(ford.color)
# # print(ford.speed)
# # ford.speed=300
# # ford.color='green'
# print(ford.color)
# print(ford.speed)

#decorators
def decorator_divide(func):
    def wrapper_func(a,b):
        print('divide',a ,' and', b)
        if b==0:
            print("the division with zero is not allowed")
            return
        return a/b 
    return wrapper_func 
    # @decorator_divide
# def divide(x,y):
#     return x/y
# print(divide(15,0))
  
    
# @decorator_func
# def say_hello():
#     print("hello world")

# # hello=decorator_func(say_hello)
# # hello()
# say_hello()

# def my_fun(num):
#     sum=0
#     for i in range(num+1):
#        sum=sum+i
#     return sum
