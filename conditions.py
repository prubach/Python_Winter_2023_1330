p = False
q = True
# https://introcs.cs.princeton.edu/java/71boolean/images/truth-table.png
if p and q:
    print('p and q True')
else:
    print('p and q False')

if p or q:
    print('p or q True')
else:
    print('p or q False')

if p or not q:
    print('p or not q True')
else:
    print('p or not q False')

# XOR
if p ^ q:
    print('p xor q True')
else:
    print('p xor q False')


print('--------------')
a = 10
b = 10

if a >= b:
    print('a>=b')
else:
    print('not a>=b')

if a == b:
    print('a=b')
else:
    print('not a=b')

#if not a == b:
if not a != b:
    print('a!=b')
else:
    print('not a!=b')

s1 = 'abc'
s2 = 'abcd'

if s1 == s2:
    print('s1=s2')
else:
    print('not s1=s2')

y = 1000 if s1 == s2 else -1000
print(y)

s3 = 'abcb'

match s3:
    case 'ab':
        print('s3=ab')
    case 'abc':
        print('s3=abc')
    case _:
        print('s3 is other')
