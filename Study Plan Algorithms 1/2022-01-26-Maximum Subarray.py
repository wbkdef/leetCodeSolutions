"""
From: https://leetcode.com/problems/maximum-subarray/submissions/
"""


from typing import Optional, Literal, Set
import itertools as it


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum_so_far = [nums[0]]

        for i in range(1, len(nums)):
            max_sum_so_far.append(max(0, max_sum_so_far[-1]) + nums[i])

        return max(max_sum_so_far)


if __name__ == "__main__":
    res = Solution().maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
    assert res == 6

    res = Solution().maxSubArray([1])
    assert res == 1

    res = Solution().maxSubArray([5,4,-1,7,8])
    assert res == 23

    print(f"all done")
