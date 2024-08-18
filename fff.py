# Function to calculate the factorial of a number
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Function to check if a number is prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# Function to find all prime numbers within a given range
def find_primes(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# Main logic
number = 5  # Number to calculate factorial for
range_start = 10  # Start of range for finding primes
range_end = 50    # End of range for finding primes

# Calculating the factorial of the given number
fact = factorial(number)

# Finding all prime numbers within the specified range
prime_numbers = find_primes(range_start, range_end)

# Storing the results in a dictionary
results = {
    "factorial": fact,
    "primes": prime_numbers
}

# Display the results
print(f"Factorial of {number}: {results['factorial']}")
print(f"Prime numbers between {range_start} and {range_end}: {results['primes']}")
