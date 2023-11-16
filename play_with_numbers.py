num_list = [3, 5, 7, 8, 11, 14, 24]

'''
TODO
1. List the subsequent 2nd powers of every element from the list
2. Sum the 2nd powers of all elements in the list
'''
sum_els = 0.0
for i in num_list:
    print(i**2)
    sum_els += (i ** 2)
print(sum_els)

print('----------------')
list_2nd_powers = [ i**2 for i in num_list ]
#list_2nd_powers = [ i**2 for i in num_list if i > 10]
print(list_2nd_powers)
print(sum(list_2nd_powers))