
def is_palindrome(name):
    for i in range(len(name)//2):
        if name[i]!=name[len(name)-1-i]:
            return False
    return True

if __name__=="__main__":
    x = "ded"
    assert is_palindrome(x)



