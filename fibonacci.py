def fibonacci(n):
    a = 0
    b = 1
    result = [a,b]
    for i in range(n):
        c = a + b
        a = b
        b = c
        result.append(c)
    
    return result

print(fibonacci(5)) 