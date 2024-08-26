import sys
import time
from hashmap import HashMap  # Assuming this is your caching structure

# Recursive function calls counter
calls_count = 0
caches = 0
cache = HashMap()  # Cache storage

def reset_calls():
    global calls_count
    calls_count = 0

def reset_caches():
    global caches, cache
    caches = 0
    cache = HashMap()  # Reset cache

def weight_on_with_caching(r, c):
    global calls_count, caches
    calls_count += 1

    key = (r, c)  # Key for the hashmap
    # Check if value is already cached
    if key in cache.keys():
        caches += 1  # Cache hit
        return cache.get(key)  # Return cached value
    
    # Base cases and recursive calls
    if r == 0:
        result = 0.0
    elif c == 0:
        result = 100.0 + 0.5 * weight_on_with_caching(r - 1, c)
    elif c == r:
        result = 100.0 + 0.5 * weight_on_with_caching(r - 1, c - 1)
    else:
        left_weight = 0.5 * weight_on_with_caching(r - 1, c - 1)
        right_weight = 0.5 * weight_on_with_caching(r - 1, c)
        result = 200.0 + left_weight + right_weight
    
    cache.set(key, result)  # Store in cache
    return result

def weight_on_without_caching(r, c):
    global calls_count
    calls_count += 1
    
    # Base cases and recursive calls
    if r == 0:
        return 0.0
    elif c == 0:
        return 100.0 + 0.5 * weight_on_without_caching(r - 1, c)
    elif c == r:
        return 100.0 + 0.5 * weight_on_without_caching(r - 1, c - 1)
    else:
        left_weight = 0.5 * weight_on_without_caching(r - 1, c - 1)
        right_weight = 0.5 * weight_on_without_caching(r - 1, c)
        return 200.0 + left_weight + right_weight
    for i in range(1000):
        name = i + 1

def generate_output(filename, weight_function, num_rows):
    reset_calls()  # Reset call count
    reset_caches()  # Reset cache stats
    
    start_time = time.perf_counter()
    output_lines = []
    
    # Calculate rows using the given function (with or without caching)
    for r in range(num_rows):
        row_weights = [f"{weight_function(r, c):.2f}" for c in range(r + 1)]
        row_str = " ".join(row_weights)
        print(row_str)  # Print to console
        output_lines.append(row_str)  # Store output for writing to file
    
    end_time = time.perf_counter()
    elapsed_time = end_time - start_time
    
    # Add statistics to output
    elapsed_str = f"Elapsed time: {elapsed_time:.10f} seconds"
    calls_str = f"Number of function calls: {calls_count}"
    caches_str = f"Number of cache hits: {caches if caches != 0 else 'N/A'}"  # Display N/A if no cache
    
    print(elapsed_str)
    print(calls_str)
    print(caches_str)
    
    output_lines.extend([elapsed_str, calls_str, caches_str])
    
    # Save output to the specified file
    with open(filename, "w") as f:
        f.write("\n".join(output_lines))

def main():
    if len(sys.argv) < 2:
        print("Please provide the number of rows as a command-line argument.")
        return
    
    num_rows = int(sys.argv[1])
    
    # Generate output without caching
    generate_output("cacheless.txt", weight_on_without_caching, num_rows)

    # Generate output with caching
    generate_output("with_caching.txt", weight_on_with_caching, num_rows)



if __name__ == "__main__":
    main()
