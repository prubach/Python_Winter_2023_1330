try:
    f = open('hello', 'r')
    f_cont = f.readlines()
    print(f_cont)
except OSError as fe:
    print(fe)

