import multiprocessing

multiprocessing.set_start_method('fork')


def compute(n):
    return [na*2 for na in n]

# Create a Pool with 4 worker processes
with multiprocessing.Pool(4) as p:
    
    # Apply the compute() function asynchronously to a sequence of arguments
    result = p.apply_async(compute, [[10,20]])

    # Wait for the result to be ready
    result.wait()

    # Get the result
    print(result.get())
    