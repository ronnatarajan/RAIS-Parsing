from bigO import bigO

# must have bigO installed
# pip install big-O-calculator

def example_function(n):
    # Example function to analyze
    result = sum(range(n))
    return result

# Estimate the time complexity of example_function
time_complexity = bigO(example_function, (1000, 2000, 3000), n_runs=10)
print(f"Estimated time complexity: {time_complexity}")

