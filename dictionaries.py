my_dict = {}
my_dict['Jan'] = 31
my_dict['Feb'] = 28
my_dict['Mar'] = 31
my_dict[1025] = 'abc'
my_dict['Mar'] = 30

print(my_dict)

my_dict2 = {'Jan': 31, 'Feb': 28, 'Mar': 30, 1025: 'abc'}
for k in my_dict2.keys():
    print(f'{k} = {my_dict2[k]}')

print('-----------------')
for k, v in my_dict2.items():
    print(f'{k}: {v}')

print('-----------------')
for v in my_dict2.values():
    print(v)
