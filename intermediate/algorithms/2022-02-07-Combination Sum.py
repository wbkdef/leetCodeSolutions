"""
From: https://leetcode.com/problems/combination-sum/
"""


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        if len(candidates) == 0:
            if target == 0:
                return [[]]
            return []

        first, *rest = candidates
        combos = []
        for i in range(target + 1):
            if i * first > target:
                break
            scs = self.combinationSum(rest, target - i * first)
            combos.extend([first] * i + sc for sc in scs)

        return combos


if __name__ == "__main__":
    assert Solution().combinationSum([2,3,6,7], 7) == [[7], [2,2,3]]
    assert Solution().combinationSum([2,3,5], 8) == [[3,5],[2,3,3],[2,2,2,2]]
    assert Solution().combinationSum([2], 1) == []

    print(f"all done")
