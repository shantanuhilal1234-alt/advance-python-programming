

def fibonacci_memo(n, memo=None):
    if memo is None:
        memo = {}

    
    if n <= 1:
        return n

    
    if n in memo:
        return memo[n]

    
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)

    return memo[n]



n = int(input("Enter n: "))

print("Fibonacci number using Memoization:",
      fibonacci_memo(n))
