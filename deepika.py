def fibonacci(n):
    fib_series = [0, 1]  # Initialize the Fibonacci series with the first two numbers

    # Generate the Fibonacci series
    for i in range(2, n):
        next_num = fib_series[-1] + fib_series[-2]
        fib_series.append(next_num)

    return fib_series


# Test the function
n = int(input("Enter the number of terms for Fibonacci series: "))
print(f"Fibonacci series with {n} terms:")
print(fibonacci(n))
print(asdfg)
print(2345t6y)print(dhinakaran)
print("this is dhinakaran")
