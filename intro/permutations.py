def permutations(rem:str, prefix:str = ""):
    if len(rem) == 0:
        print(prefix)
    else:
        for n in range(len(rem)):
            if n==len(rem)-1:
                permutations(
                    rem[:n], prefix+rem[n]
                )
            else:
                permutations(
                    rem[:n]+ rem[n+1:], prefix+rem[n]
                )

if __name__=="__main__":
    permutations("abc")