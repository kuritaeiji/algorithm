def fibonacci(n, dp = None):
    if dp == None:
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1

    if dp[n]:
        return dp[n]

    result = fibonacci(n-1, dp) + fibonacci(n-2, dp)
    dp[n] = result
    return result

print(fibonacci(44))

def dp_fibonacci(n):
    dp = [1] * (n + 1)
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

print(dp_fibonacci(44))