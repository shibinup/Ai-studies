
def decarator_fun(fun) :
    def wrapper(args):
        
        rst=fun(args)

        return [i*3 for i in rst]


    return wrapper

@decarator_fun
def reverse_list(lst):
    return lst[::-1]

@decarator_fun
def correct(lst):
    return lst

print(reverse_list([1,2,3,4]) )
print(correct([12,23,34,45]))