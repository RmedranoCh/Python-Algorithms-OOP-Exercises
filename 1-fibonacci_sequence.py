def fibonacci(n):
    sequence = [0, 1]
    
    if n < len(sequence):
        return sequence[n]
    
    for i in range(2, n + 1):
        next_value = sequence[i - 1] + sequence[i - 2]
        sequence.append(next_value)
    
    return sequence[n]

try:
    position = int(input("Enter Fibonacci position (ej. 10): "))
    
    result = fibonacci(position)
    
    print(f"Value at position {position} is: {result}")

except ValueError:
    print("Error: Invalid number.")