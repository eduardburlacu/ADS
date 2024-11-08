def print_powers(n:int, base:int = 2):
    if n==1: # Base case
        print(1)
        return 1
    elif n==0: #Edge base case n < base
        return 0
    else:
        prev = print_powers(n//base, base)
        result = base * prev
        if 0 < result <= n:
            print(result)
        return result

if __name__=="__main__":
    print_powers(1023, 2)