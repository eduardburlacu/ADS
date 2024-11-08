"""
You are given a string s and an integer k.
Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. The longest substring with at most 2 distinct characters is "ece".
"""
def max_substring(s:str, k:int)->int:
    left = best = 0
    curr = {}
    for right in range(len(s)):
        if s[right] in curr:
            curr[s[right]] += 1
        else:
            curr[s[right]] = 1
        while len(curr)>k:
            if curr[s[left]] == 1:
                del curr[s[left]]
            else:
                curr[s[left]] -= 1
            left += 1
        best = max(best, right - left + 1)
    return best

if __name__=="__main__":
    print(
        max_substring("aabccccdefggg",k=3)
    )
