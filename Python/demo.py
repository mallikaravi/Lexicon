#print("Hello World")
#print("This is also a string")
#print("use \n to print a new line")

#length=len("Hello World")
#print(length)

#s="Hello World"
#print(s[1])
#print(s[1:])prints after 1 index
#print(s[:3])prints upto 3 index
#print(s[:])prints all words
#print(s[:-1])prints helloworl
#print(s[::2])Hlowrd
#print(s[::-1])prints reverse
#s="Hello World"

#print(s.upper())
#print(s.split())
#print(s.split('W'))
#print('one:{p},Two:{p},Three:{p}'.format(p='Hello'))
#print('Object 1:{a},Object 2:{b},Object 3:{c}'.format(a='Hello',b='Hi',c='something'))

#my_list=['A string',23,100.134,'T']
#print(my_list)
#print(len(my_list))

#my_list=['one','two','three',4,5]
#print(my_list[0])
#print(my_list[:3])prints first three elemets
#print(my_list +['new item'])
#my_list=my_list+['new item']
#print(my_list*2)

# my_list=[1,2,3]
# my_list.append("append me!")
# popped_item=my_list.pop()
# print(popped_item)
# print(my_list)
# new_list=['a','e','x','h','c']
# #new_list.reverse()
# new_list.sort()
# print(new_list)




# lst_1=[1,2,3]
# lst_2=[4,5,6]
# lst_3=[7,8,9]

# matrix=[lst_1,lst_2,lst_3]
# print(matrix)
# print(matrix[0])
# print(matrix[0][0]) first element in first matrix
# first_col=[row[0] for row in matrix]
# print(first_col) prints [1,4,7]

#Dictionaries
#my_dic={'key1':123,'key2':[10,33,45],'key3':['item0','item1','item3']}
#print(my_dic['key3'])prints values at key 3
#print(my_dic['key3'][0])printskey 3 at index 0
#my_dic['key1']+=12
#print(my_dic['key1'])

# d={}
# d['animal']='Dog'
# d['answer']=42
# print(d)

#grabbing elements
# d={'key1':{'nestkey':{'subnestkey':'123'}}}
# print(d['key1']['nestkey']['subnestkey'])

# d={'key1':1,'key2':2,'key3':3}
# print(d.items())

#Tupples are like lists,immutable
#t=(1,'two',3)
#print(t)
#print(t[-1])prints 3
#print(t.index("two"))

#sets



# x=set()
# x.add(1)
# x.add(2)
# x.add(1)
# print(x)
# x=[1,1,1,2,2,2,33,3,3,3,3,4,4,]
# print(set(x))

# a=True
# print(1>2)

# total=0
# expenses =[]
# for i in range(7):
#     expenses.append(float(input("Enter an expense:")))

#     total=sum(expenses)


#     print("you spent $",total,sep='')

#Loops in python

# my_list=[1,2,3,4,5]

# for cake in my_list:
#     print(cake+cake)
 
# ages ={'Bob':3,'Sowji':5,'Maha':10}
# for key in ages:
#      print("This is the key")
#      print (key)
#      print("This is the value")
#      print (ages[key])

#mypairs=[(1,10),(3,30),(5,50)]

# i=1
# while i<5:
#     print("i is:{}".format(i))
# i=i+1

# my_list=list(range(1,6))
# print(my_list)

# for i in range(1,11,3):
#     print(i)


   #list comprehension 
# x=[1,2,3,4]
# out=[]
# for item in x:
#     out.append(item**2)

# print(item**2 for item in x)  
   
   #Functions in python
# def giveMeHello():
#     return 'hello'


# print(giveMeHello())
# def evenCheck(num):
#     print("I am checking to see if{}iseven!".format(num))
#     print(num%2==0)
# evenCheck(42)  


# def addEvenOnly(num1,num2):
#     if(num1%2!=0)or(num2%2!=0):
#         return False
#     else:
#         return num1+num2
# x=addEvenOnly(1,2)
# Y=addEvenOnly(1,2)

# print(x)
# print(Y)

# my_list=[1,2,3,4,5,6,7,8,9,10]
# evens=filter(lambda num:num%2==0,my_list)
# print(list(evens))


#Scope in python
# x=15

# def printer():
#    x=30
#    return x
# print(x)
# print(printer())
# print(x)

# 1.NAme assignment will create or change local names by default
#2.locl,enclosing functions,global,builtin
#LEGB rule
#L:Local-Assigned within a function(def or lambda)
#E:Enclosing function locals-name in local scope of any and all enclosing func
#G:Global-Assigned at top level of module file or declared in a def withinfile
#B Built-in-preassigned in the built in names module:open,range,Syntax error....

#local
# f=lambda x:x**2
# name="Khaled"
# #Enclosing function locals
# def greet():
#    global name

#    def hello():
#         print("Hello" +name)
   
#    hello()
# greet()



# x=50
# def fun():
#    global x
#    print('x is',x)
#    x=2
#    print('changed local x to ',x)

# fun()
# print('x is',x)

# l=[1,2,3]
# l.count(2)

# print(type(1))class integer
# print(type([]))class int
# print(type(()))tupple
# print(type({}))dict

# class Sample():
#    pass
# x=Sample()

# print(type(x))

# class Dog():
#    species="mammal"
#    def _init_(self,breed):
#       self.breed=breed
#       self.name=name

# sam=Dog('lab','Sam')


# print(sam.species)

# class Circle():
#    pi=3.14
#    def _init_(self,radius=1):
#       self.radius=radius
#    def area(self):
#       return self.radius*self.radius*circle.pi


#    def setRadius(self,radius):
#         self.radius=radius
#    def getRadius(self,radius):
#         return self.radius
# c=Circle()
# c.setRadius(2)
# print('Radius is:',c.getRadius())
# print('Area is:',c.area())


#Inheritance
# class Animal():#Base class
#    def __init__(self):
#        print("Animal created")
#    def whoAmI(self):
#       print("Animal")
#    def eat(self):
#       print("Eating....") 

# class Dog(Animal):#Derived class
#    def __init__(self):
#        Animal.__init__(self) 
#        print("Dog created")
#    def whoAmI(self):
#       print("Dog")
#    def bark(self):
#       print("Woof!")

# d=Dog()
# d.whoAmI()
# d.eat()
# d.bark()


# class Book():
#    def __init__(self,title,author,pages):
#       print("A book is created")
#       self.title=title
#       self.author=author
#       self.pages=pages
   
#    def __str__(self):
#       return "Title:%s,author:%s,pages:%s"%(self.title,self.author,self.pages)
#    def __len__(self):
      
#       return self.pages
#    def __del__(self):
   
#       print("A book has been destroyed!")
       
# book=Book("Python book","Haithem",300)
# print(book)
# print(len(book))
# del book






