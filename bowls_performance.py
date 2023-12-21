from time import time
from bowls import sum_of_bowls_recursive, sum_of_bowls_loop, sum_of_bowls_sequence

def time_func(func, n):
    t0 = time()
    print(f'Running {func.__name__} with n={n}')
    res = func(n)
    print(f'Result={res}')
    t1 = time()
    elapsed = round(t1 - t0, 8)
    print(f'Done in {elapsed} sec')

n = 100000000
time_func(sum_of_bowls_loop, n)
time_func(sum_of_bowls_sequence, n)
# Maximum n=998 - max depth exceeded otherwise
#time_func(sum_of_bowls_recursive, n)
