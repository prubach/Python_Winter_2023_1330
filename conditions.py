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