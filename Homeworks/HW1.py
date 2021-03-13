odd_list = [1,3,5,7,9]  # odd numbers
even_list = [0,2,4,6,8]     # even numbers

numbers = odd_list + even_list  # merging two lists

numbers = [i*2 for i in numbers]    # multiplying each element by two

#   printing type of elements
for i in numbers:
    print(type(i))