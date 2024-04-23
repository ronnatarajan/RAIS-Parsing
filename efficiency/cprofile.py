import cProfile

def example_function():
    # Example function to analyze
    result = sum(range(1000000))
    return result

if __name__ == "__main__":
    cProfile.run("example_function()")

