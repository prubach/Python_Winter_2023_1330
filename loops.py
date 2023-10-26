for i in range(0, 5):
    print(f'i={i}')
print('---------------')
for i in range(0, 8, 2):
    print(f'i={i}')

print('---------------')
for i in reversed(range(-5, 15, 3)):
    print(f'i={i}')

print('---------------')
j=1
while j < 10:
    # j = j + 1
    j += 1
    if j == 3:
        continue
    if j == 8:
        break
    print(f'j={j}')

