"""

"""
if __name__=="__main__":
    #Naively building a string
    greet = "Hello!"
    reconstruct = ""
    #This is bad. sum_i=1 ^N i = O(N^2)
    for c in greet:
        reconstruct = reconstruct + c
    print(reconstruct)
    chars = []
    for c in greet:
        chars.append(c)
    reconstruct = "".join(chars)
    print(reconstruct)
