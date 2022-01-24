"""
From: https://leetcode.com/problems/minimum-size-subarray-sum/
"""

import math


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        cum_sum = [0]
        for num in nums:
            cum_sum.append(cum_sum[-1] + num)

        min_len = len(nums) + 1
        i = 0
        j = 1
        while j < len(cum_sum):
            if cum_sum[j] - cum_sum[i] >= target:
                min_len = min(min_len, j-i)
                i += 1
            else:
                j += 1

        if min_len == len(nums) + 1:
            min_len = 0

        return min_len


if __name__ == "__main__":
    res = Solution().minSubArrayLen(target = 7, nums = [2,3,1,2,4,3])
    assert res == 2

    res = Solution().minSubArrayLen(target = 4, nums = [1,4,4])
    assert res == 1

    res = Solution().minSubArrayLen(target = 11, nums = [1,1,1,1,1,1,1,1])
    assert res == 0

    print(f"all done")
