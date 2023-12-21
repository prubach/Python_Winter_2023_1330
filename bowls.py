#   * * * * * *
#    * * * * *
#     * * * *
#      * * *
#       * *
#        *

n = 100
#TODO given n - number of rows write a function that gives the
# sum of all bowls

# Solution by Cuong Vo
def sum_of_bowls_sequence(n):
    total_sum = int(n*(n+1)/2)
    return total_sum

# Solution by Joanna Marie Corpuz
def sum_of_bowls_loop(n):
    sum_bowls = sum(list(range(n, 0, -1)))
    return sum_bowls


def sum_of_bowls_recursive(n):
    if n == 1:
        return 1
    else:
        res = sum_of_bowls_recursive(n-1) + n
        return res

print('Sum of bowls using sequence: {}'.format(sum_of_bowls_sequence(n)))
print('Sum of bowls using loop: {}'.format(sum_of_bowls_loop(n)))
print('Sum of bowls using recursion: {}'.format(sum_of_bowls_recursive(n)))