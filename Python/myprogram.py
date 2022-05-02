# import mymodule
# def func():
#     print("Hello World")

# if __name__=="__main__":
#    #print("Hello")
#    try:


#     except Exception:    


# try:
#     f=open('testfile','r')
#     f.write('Hello world')
# except IOError:
#     print("Error:could not find file")
# else:
#     print("content written successfully")
#     f.close()

# finally:
#     print("Always execute finally code blocks")

#Decorators
# s='Global var'
# def func():
#     print(globals().keys())

# func()

# 

# def hello():
#     return "Hi Haithem!"

# def other(func):
#     print("Other code would go here")
#     print(func())

# other(hello)

# def new_decorator(func):
#     def wrap_func():
#         print("code would be here")

#         func()
#         print("code here will be executed sfter func")
#     return wrap_func


# @new_decorator
# def func_needs_decorator():
#     print("Thisfunction is in need of decorator")
# # func_needs_decorator()

# # func_needs_decorator=new_decorator(func_needs_decorator)

# func_needs_decorator()



#Regular Expressions,regex or regexp


# import re

# # split_term='@'

# # phrase='What is the domain name of someone with email:hello@gmail.com'

# # print(re.split(split_term,phrase))
# # print(re.findall('match','test phrase match in middel'))

# def multi_re_find(patterns,phrase):
#     for pattern in patterns:
#         print("searching the phrase using re check:%r"%pattern)
#         print(re.findall(pattern,phrase))
#         print('\n')

#        
#  #A pattern followed by meta-character *is repeated zero or more times.
#         #Replace the *with +and pattern must apear at least once.
#         #Using?pattern appears zero or one time.
#         #{m}
#         #{m,n}


# test_phrase='sdsd..sssdddd...sdddsdsdsd...dsds...dsssss...sssssd....sddd'
# test_patterns=['sd*',
# 'sd+',
# 'sd?',
# 'sd{3}',
# 'sd{2,3}']

# multi_re_find(test_patterns,test_phrase)
# import re

# test_phrase='Thisis a string with some numbers 1233 and a symbol#hashtag'
# def multi_re_find(patterns,phrase):
#     for pattern in patterns:
#         print("searching the phrase using re check:%r"%pattern)
#         print(re.findall(pattern,phrase))
#         print('\n')


# # test_patterns=['[a-z]+','[A-Z]+','[a-zA-z]+']
# test_patterns=[r'\d+',#digits
#               r'\D+',#non-digits
#               r'\s+',#white space"
#               r'\S+',#non white spae
#               r'\w+',#alphanumeric
#               r'\W',#non alphanumeric
#               ]
# multi_re_find(test_patterns,test_phrase)

