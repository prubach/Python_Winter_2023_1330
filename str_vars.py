s = 'abcdefghłąśąąąę'
print(s)
print(ord('a'))
print(ord('A'))
print(ord('ź'))

print('avsavsab\nagfaggw\\ra\\negwg2wghq')
s1 = 'avsavsab\tagfaggw\ta\\tnegwg2wghq'
print(s1)
print(s1[2])
print(s1[2:])
print(s1[:5])
print(s1[-5:])
# No new line at the end
print('-------------------', end='')
print('aagae')
print('-------------------')

s2 = 'avsavsab\tagfaggw\ta\ttnegwg2wghq'
s2a = s2.split('\t')
print(s2a)
print(s2a[1])

print('|'.join(s2))
print('|'.join(s2a))
print(''.join(s2a))
print('--------------------')
s3 = 'avsavsab\nagfaggw\nahethe\ntnegwg2wghq'
s3a = s3.splitlines()
print(s3a)

print('----------------')
print('I can\'t')
print("I can\'t")
print("I can't \"Pawel\"")
print("I can't " + "\"Pawel\"")
print()
print('----------------')
s4 = 'avsavsab\tagfaggw\ta\ttnegwg2wghq'
# If not found returns -1
f_vs = s4.find('vs')
print(f'vs found: {f_vs}')
# If not found throws ValueError
f_vs = s4.index('vs')
print(f'vs index: {f_vs}')
f_vs = s4.rindex('vs')
print(f'vs rindex: {f_vs}')
f_vs = s4.count('vs')
print(f'vs count: {f_vs}')