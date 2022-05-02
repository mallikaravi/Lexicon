
from unittest import result


def string_Bits(str):
    new_str=""
    for i in range(0,len(str),2):
        new_str=new_str+str[i]
    return new_str

#print(string_Bits('Hello'))
#print(string_Bits('Hi'))
print(string_Bits('Heeololeo'))

# if i%2==0:
#     result=result+str[i]