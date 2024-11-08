"""
Given a string s, determine if all characters have the same frequency.
For example, given s = "abacbc", return true.
All characters appear twice. Given s = "aaabb", return false.
"a" appears 3 times, "b" appears 2 times.
"""
def is_equal_freq(s:str)->bool:
    hashmap = dict()
    for ch in s:
        if ch in hashmap:
            hashmap[ch] += 1
        else:
            hashmap[ch] = 1
    return len(set(hashmap.values())) == 1

if __name__=="__main__":
    assert is_equal_freq("BHaHaBHaB")