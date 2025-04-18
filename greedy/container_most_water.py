"""
Leetcode 11
"""
def maxArea(height:list[int])->int:
    """
    :type height: List[int]
    :rtype: int
    """
    left, right = 0, len(height) - 1
    best = 0
    while left < right:
        if height[left] < height[right]:
            curr = height[left] * (right - left)
            left += 1
        else:
            curr = height[right] * (right - left)
            right -= 1
        best = max(best, curr)
    return best
