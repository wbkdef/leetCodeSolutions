"""
From: https://leetcode.com/problems/container-with-most-water/
PC:KEYnMKK:
"""

import itertools as it

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # return self.brute(height)
        return self.efficient(height)

    def brute(self, height: list[int]) -> int:
        max_area = 0
        for (i, hi), (j, hj) in it.combinations(enumerate(height), 2):
            area = abs(j-i) * min(hi, hj)
            max_area = max(area, max_area)
        return max_area

    def efficient(self, height: list[int]) -> int:
        # Could be made even more efficient - know the max possible i value, so
        # could eliminate even more using this to bound the area!
        possible_lefts = {}
        highest_so_far = 0
        for i, h in enumerate(height):
            if h > highest_so_far:
                highest_so_far = h
                possible_lefts[i] = h
        print(f" possible_lefts is [[{possible_lefts}]]")

        possible_rights = {}
        highest_so_far = 0
        for i, h in reversed(list(enumerate(height))):
            if h > highest_so_far:
                highest_so_far = h
                possible_rights[i] = h
        print(f" possible_rights is [[{possible_rights}]]")

        max_area = 0
        for il, hl in possible_lefts.items():
            for ir, hr in possible_rights.items():
                if il < ir:
                    area = (ir-il) * min(hl, hr)
                    max_area = max(area, max_area)

        return max_area


if __name__ == "__main__":
    res = Solution().maxArea([1,8,6,2,5,4,8,3,7])
    assert res == 49

    res = Solution().maxArea([1,1])
    assert res == 1

    print(f"All done")