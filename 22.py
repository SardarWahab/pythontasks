import time
from functools import wraps

# Decorator to log execution time of a function
def log_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record start time
        result = func(*args, **kwargs)  # Execute the function
        end_time = time.time()  # Record end time
        execution_time = end_time - start_time
        print(f"Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

# Example function to demonstrate the decorator
@log_execution_time
def slow_function():
    print("Starting a slow function...")
    time.sleep(2)  # Simulate a slow operation
    print("Function completed.")

@log_execution_time
def add(a, b):
    print(f"Adding {a} and {b}...")
    return a + b

# Main execution
if __name__ == "__main__":
    slow_function()
    result = add(5, 7)
    print(f"Result of add: {result}")
