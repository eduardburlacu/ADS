"""
Given a binary string s (a string containing only "0" and "1").
You may choose up to one "0" and flip it to a "1".
What is the length of the longest substring achievable that contains only "1"?
"""

def max_1bf_len(s:str) -> int:
    left = best = 0
    used = -1
    for right in range(len(s)):
        if s[right]=="0":
            if used>=left:
                left = used + 1
            used = right
        best = max(best, right - left + 1)
    return best

if __name__=="__main__":
    print(max_1bf_len("0101101111"))
