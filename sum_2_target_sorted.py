
def is_sum_2_target(arr, targ):
    left = 0
    right = len(arr) - 1

    while left<right:
        s = arr[left] + arr[right]
        if s<targ:
            left += 1
        elif s>targ:
            right -= 1
        else:
            return True
    return False

if __name__=="__main__":
    a = [1, 3, 4, 7, 8, 8, 9, 10]
    t = 15
    assert is_sum_2_target(a, t)
