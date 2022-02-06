"""
From: https://leetcode.com/problems/jump-game/submissions/
"""


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        can_get_to_end_from = len(nums) - 1

        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= can_get_to_end_from:
                can_get_to_end_from = i
            print(f" i, can_get_to_end_from is [[{i, can_get_to_end_from}]]")

        return can_get_to_end_from == 0

if __name__ == "__main__":
    assert Solution().canJump([2,3,1,1,4]) == True
    assert Solution().canJump([3,2,1,0,4]) == False

    print(f"all done")
