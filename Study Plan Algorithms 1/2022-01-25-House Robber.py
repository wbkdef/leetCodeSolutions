"""
From: https://leetcode.com/problems/power-of-two/
"""


from typing import Optional, Literal, Set
import itertools as it


class Solution:
    def rob(self, nums: list[int]) -> int:
        most_rob_up_to = [0, 0]

        for i in range(len(nums)):
            most_rob_up_to.append(max(most_rob_up_to[-1],
                                      most_rob_up_to[-2]+nums[i]))

        assert len(most_rob_up_to) == len(nums) + 2
        return most_rob_up_to[-1]


if __name__ == "__main__":
    res = Solution().rob([1,2,3,1])
    assert res == 4

    res = Solution().rob([2,7,9,3,1])
    assert res == 12

    print(f"all done")
