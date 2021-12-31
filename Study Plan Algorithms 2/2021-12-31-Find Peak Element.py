"""
From: https://leetcode.com/problems/find-peak-element/
PC:KEYlaWf:
"""

import math

INCREASING = 0
DECREASING = 1
PEAK = 2
VALLEY = 3


class Solution:
    def get(self, nums, ind)  ->  int:
        if ind in [-1, len(nums)]:
            return -math.inf
        return nums[ind]

    def get_increasing_decreasing_peak(self, nums, ind)  ->  int:
        a = self.get(nums, ind-1)
        b = self.get(nums, ind)
        c = self.get(nums, ind+1)
        if a < b:
            if b < c:
                return INCREASING
            assert b > c
            return PEAK
        else:
            if b < c:
                return VALLEY
            assert b > c
            return DECREASING

    def findPeakElement(self, nums: list[int]) -> int:
        ind_lower = -1
        ind_upper = len(nums)
        while ind_lower < ind_upper - 1:
            ind_mid = (ind_upper + ind_lower) // 2
            mode = self.get_increasing_decreasing_peak(nums, ind_mid)
            if mode == PEAK:
                return ind_mid
            elif mode in [INCREASING, VALLEY]:
                ind_lower = ind_mid
            else:
                assert mode == DECREASING
                ind_upper = ind_mid

        assert False, "Shouldn't get here!"


if __name__ == "__main__":
    res = Solution().findPeakElement([1,2,3,1])
    assert res == 2

    res = Solution().findPeakElement([1,2,1,3,5,6,4])
    assert res in [1, 5]

    res = Solution().findPeakElement([1,-2,3,5])
    assert res in [0, 3]

    res = Solution().findPeakElement([3])
    assert res in [0]

    print(f"all done")
