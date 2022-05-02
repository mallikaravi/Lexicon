



def end_Other(X,Y):
     X=X.lower()
     Y=Y.lower()  
     if Y.endswith(Y)or X.endswith(Y):
        return True
     else:
        return False
   
#print(end_Other('Hiabc','abc'))
#print(end_Other('AbC','HiaBc'))
print(end_Other('abc','abXabc'))

# def end_other(a,b):
#    a=a.lower()
#    b=b.lower()

#    return a[-(len(b)):]==b or a==b[-(len(a)):]
# print(end_Other('abc','abXabc'))