def priter(n:int):
    for i in range(1, n+1):
        print(i)

def pr_down(n: int):
    if n == 1:
        print(1)
    else:
        pr_down(n - 1)
        print(n)


def pr_up(n: int):
    if n >= 10:
        return
    print(n)
    pr_up(n+1)
    return

if __name__=="__main__":
    #pr_down(10)
    pr_up(1)
