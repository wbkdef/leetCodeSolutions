"""
From: https://leetcode.com/problems/subsets-ii/
"""


from typing import Optional, Literal, Set
import itertools as it


class Solution:
    def subsetsWithDup(self, nums: list[int]) -> list[list[int]]:
        all_subsets = [[]]
        for key, vals in it.groupby(sorted(nums)):
            n_vals = len(list(vals))
            new_subsets = [s+[key]*nv
                for s in all_subsets
                for nv in range(n_vals+1)
            ]
            all_subsets = new_subsets
        return sorted(all_subsets)


if __name__ == "__main__":
    res = Solution().subsetsWithDup([1,2,3])
    assert res == sorted([[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]])

    res = Solution().subsetsWithDup([1,2,2])
    assert res == [[],[1],[1,2],[1,2,2],[2],[2,2]]

    res = Solution().subsetsWithDup([0])
    assert res == [[],[0]]

    print(f"all done")
