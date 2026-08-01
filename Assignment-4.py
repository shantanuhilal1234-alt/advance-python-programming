# Dynamic Programming - Fibonacci
# Using Memoization and Tabulation

# Memoization Method
def fib_memo(num, cache=None):

    if cache is None:
        cache = {}

    if num in cache:
        return cache[num]

    if num <= 1:
        return num

    cache[num] = fib_memo(num - 1, cache) + fib_memo(num - 2, cache)
    return cache[num]

# Tabulation Method
def fib_tab(num):

    if num <= 1:
        return num

    table = [0] * (num + 1)
    table[1] = 1

    for i in range(2, num + 1):
        table[i] = table[i - 1] + table[i - 2]

    return table[num]

# Main Program
n = int(input("Enter Fibonacci Position: "))
memo_result = fib_memo(n)
tab_result = fib_tab(n)

print("\nResult using Memoization :", memo_result)
print("Result using Tabulation  :", tab_result)
Comment:-
Enter Fibonacci Position: 10

Result using Memoization : 55
Result using Tabulation  : 55
