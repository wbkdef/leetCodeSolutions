"""
From: https://leetcode.com/problems/container-with-most-water/
"""

from __future__ import annotations

from typing import Optional


class Solution:
    def maxArea(self, height: list[int]) -> int:
        i = 0
        j = len(height)-1
        max_water = 0
        while i < j:
            amt_water = (j - i) * min(height[i], height[j])
            max_water = max(max_water, amt_water)
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return max_water


if __name__ == "__main__":
    res = Solution().maxArea([1,8,6,2,5,4,8,3,7])
    assert res == 49

    res = Solution().maxArea([1,1])
    assert res == 1

    res = Solution().maxArea([])
    assert res == 0

    print(f"all done")
