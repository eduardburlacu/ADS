def is_subseq(s:str,t:str)->bool:
    i = j = 0
    while i < len(s):
        if j == len(t):
            return False
        if s[i] == t[j]:
            i += 1
        j += 1
    return True

if __name__=="__main__":
    assert is_subseq(
        "cr",
        "gbuiuhdusgcargshnoidgnsig"
    )
