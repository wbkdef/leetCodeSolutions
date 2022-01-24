"""
From: https://leetcode.com/problems/subsets/
"""


from typing import Optional, Literal, Set


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        all_subsets = [[]]
        for num in nums:
            new_subsets = [s + [num] for s in all_subsets]
            all_subsets = all_subsets + new_subsets
        return all_subsets


if __name__ == "__main__":
    res = Solution().subsets([1,2,3])
    assert res == [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

    res = Solution().subsets([0])
    assert res == [[],[0]]

    print(f"all done")
