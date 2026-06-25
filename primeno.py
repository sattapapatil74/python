def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

nums = [7, 10, 13, 1, 29]
for num in nums:
    if is_prime(num):
        print(f"{num} is Prime")
    else:
        print(f"{num} is Not Prime")

        
