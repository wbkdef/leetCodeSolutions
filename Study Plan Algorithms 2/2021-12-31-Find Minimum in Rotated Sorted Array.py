"""
From: https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
PC:KEYcNkv:
"""


class Solution:
    def findMin(self, nums: list[int]) -> int:
        ind_lower = 0
        ind_upper = len(nums) - 1
        while ind_lower < ind_upper - 1:
            if nums[ind_lower] < nums[ind_upper]:
                # Must be sorted
                break
            ind_mid = (ind_upper + ind_lower) // 2
            if nums[ind_mid] > nums[ind_lower]:
                ind_lower = ind_mid
            else:
                ind_upper = ind_mid

        return min(nums[ind_lower], nums[ind_upper])


if __name__ == "__main__":
    res = Solution().findMin([3,4,5,1,2])
    assert res == 1

    res = Solution().findMin([4,5,6,7,0,1,2])
    assert res == 0

    res = Solution().findMin([11,13,15,17])
    assert res == 11

    print(f"all done")
