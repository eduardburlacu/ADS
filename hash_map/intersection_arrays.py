"""
2248. Intersection of Multiple Arrays
Given a 2D array nums that contains n arrays of distinct integers,
  return a sorted array containing all the numbers that appear in all n arrays.
For example, given nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], return [3, 4]. 3 and 4 are the only numbers that are in all arrays.
"""
def intersect(nums:list[list[int]]):
    freq = dict()
    for num in nums:
        for n in num:
            if n in freq:
                freq[n] += 1
            else:
                freq[n] = 1
    out = []
    l = len(nums)
    for i in freq:
        if freq[i] == l:
            out.append(freq[i])
    return sorted(out)

if __name__=="__main__":
    print(
        intersect([[1,2,3],[2,3,4],[3,4,5]])
    )