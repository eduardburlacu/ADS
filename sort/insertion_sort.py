"""
Time complexity:
    - best
    - average
    - worst
Space complexity:
"""

def insertion_sort(a:list, _debug=True)->None:
    n = len(a)
    if n<2:
        return
    for i in range(1, n):
        key = a[i]
        s = i-1
        while s>=0 and a[s]>key:
            a[s+1] = a[s]
            s -= 1
        a[s+1] = key
        if _debug:
            print(a)
    return

if __name__=="__main__":
    a = [5, 2, 4, 6, 1, 3]
    print(a)
    insertion_sort(a)




