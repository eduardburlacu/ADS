"""
Time complexity: O(n^2) always
Space complexity: O(1) always
"""
def bubble_sort(a:list)->None:
    n = len(a)
    if n==0:
        return
    for i in range(n-1):
        for j in range(n-1-i):
            if a[j] > a[j+1]:
                a[j], a[j+1]=a[j+1],a[j]
    return

if __name__=="__main__":
    a = [5,4,3,2,1]
    print(a)
    bubble_sort(a)
    print(a)