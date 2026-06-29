
def fibonacci(n):
    a, b = 1, 2 
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")  
        a, b = b, a + b  

N = int(input("Input: "))
fibonacci(N)
