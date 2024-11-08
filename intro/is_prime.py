"""
Check if a number is prime. O(sqrt(N)) time complexity
"""
def is_prime(n:int)->bool:
    x = 2
    while x * x <=n:
        if n%x==0:
            return False
        x += 1
    return True

if __name__=="__main__":
    print(
        is_prime(777896981)
    )
