num_list = [3, 5, 21, 7, 14, 8, 11, 3, 14, 24]
list_2nd_powers = [ i**2 for i in num_list ]

print(list_2nd_powers)
print(sorted(list_2nd_powers))
print(sorted(list_2nd_powers, reverse=True))

set_2nd_powers = set(list_2nd_powers)
print(set_2nd_powers)
# Error below
#print(set_2nd_powers[2])
sorted_list = sorted(list(set_2nd_powers))
print(sorted_list)

