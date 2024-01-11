def squares(numbers):
    for i in numbers:
        yield i*i
my_list= squares([1,2,3,4,5])
#print(my_list)
for numbers in my_list:
    print(numbers)
#print(next(my_list))
#print(next(my_list))
#print(next(my_list))
#print(next(my_list))
#print(next(my_list))
#print(next(my_list))


