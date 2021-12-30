"""
From: https://leetcode.com/problems/next-permutation/
PC:KEYoViX:
"""


class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        return [self.find_ind_first_instance_of(nums, target, 0, len(nums) - 1),
                self.find_ind_last_instance_of(nums, target, 0, len(nums) - 1)]

    def find_ind_first_instance_of(self, nums: list[int], target: int,
                                   ind_lower: int, ind_upper: int) -> int:
        "Returns -1 if not found"
        if len(nums) == 0:
            return -1
        lower = nums[ind_lower]
        upper = nums[ind_upper]
        if lower == target:
            return ind_lower
        if ind_upper <= ind_lower + 1:
            if upper == target:
                return ind_upper
            return -1

        ind_mid = (ind_lower + ind_upper) // 2
        mid = nums[ind_mid]
        if mid >= target:
            return self.find_ind_first_instance_of(nums, target,
                                                   ind_lower, ind_mid)
        return self.find_ind_first_instance_of(nums, target,
                                                   ind_mid, ind_upper)

    def find_ind_last_instance_of(self, nums: list[int], target: int,
                                   ind_lower: int, ind_upper: int) -> int:
        "Returns -1 if not found"
        if len(nums) == 0:
            return -1
        lower = nums[ind_lower]
        upper = nums[ind_upper]
        if upper == target:
            return ind_upper
        if ind_upper <= ind_lower + 1:
            if lower == target:
                return ind_lower
            return -1

        ind_mid = (ind_lower + ind_upper) // 2
        mid = nums[ind_mid]
        if mid > target:
            return self.find_ind_last_instance_of(nums, target,
                                                   ind_lower, ind_mid)
        return self.find_ind_last_instance_of(nums, target,
                                                   ind_mid, ind_upper)

if __name__ == "__main__":
    nums = [5,7,7,8,8,10]
    res = Solution().searchRange(nums, 8)
    assert res == [3,4]

    nums = [5,7,7,8,8,10]
    res = Solution().searchRange(nums, 6)
    assert res == [-1,-1]

    nums = [5,7,7,8,8,9, 10]
    res = Solution().searchRange(nums, 9)
    assert res == [5,5]

    nums = []
    res = Solution().searchRange(nums, 0)
    assert res == [-1,-1]

    print(f"all done")
