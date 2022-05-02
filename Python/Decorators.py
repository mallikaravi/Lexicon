def even_numbers(function):
    def wrap(numbers):
        for i in numbers:
            if i%2==0:
               print(i,"is an even number")
        function()
        print("even numbers") 
      
    return wrap
@even_numbers
def func_needs_decorator():
    print("decorator content printing")
numbers=[1,2,3,4,5,6,7,8,9,10]
func_needs_decorator(numbers)




