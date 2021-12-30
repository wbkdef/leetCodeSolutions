"""
From: https://leetcode.com/problems/next-permutation/
PC:KEYoViX:
"""


class Solution:
    def search(self, nums: list[int], target: int) -> int:
        """ return the index of target if it is in nums, or -1 if it is not
        in nums """
        return self.search_(nums, target, 0, len(nums)-1)

    def could_be_between(self, nums: list[int], target: int,
                         ind_lower: int, ind_upper: int):
        if target in {nums[ind_lower], nums[ind_upper]}:
            return True
        if nums[ind_lower] < target < nums[ind_upper]:
            return True
        elif nums[ind_lower] > nums[ind_upper]:
            if target > nums[ind_lower] or target < nums[ind_upper]:
                return True
        return False

    def search_(self, nums: list[int], target: int,
                ind_lower: int, ind_upper: int)  ->  int:
        if len(nums) == 0:
            return -1
        assert ind_lower <= ind_upper
        if nums[ind_lower] == target:
            return ind_lower
        if nums[ind_upper] == target:
            return ind_upper

        if ind_upper <= ind_lower + 1:  # Not found
            return -1

        ind_mid = (ind_lower + ind_upper)//2
        res1 = res2 = -1
        if self.could_be_between(nums,  target, ind_lower, ind_mid):
            res1 = self.search_(nums,  target, ind_lower, ind_mid)
        if self.could_be_between(nums,  target, ind_mid+1, ind_upper):
            res2 = self.search_(nums,  target, ind_mid+1, ind_upper)
        assert min(res1, res2) == -1

        return max(res1, res2)


if __name__ == "__main__":
    nums = [4,5,6,7,0,1,2]
    res = Solution().search(nums, 0)
    assert res == 4

    nums = [4,5,6,7,0,1,2]
    res = Solution().search(nums, 3)
    assert res == -1

    nums = [1]
    res = Solution().search(nums, 0)
    assert res == -1

    nums = []
    res = Solution().search(nums, 0)
    assert res == -1

    nums = [3, 1]
    res = Solution().search(nums, 1)
    assert res == 1

    nums = [3, 1]
    res = Solution().search(nums, 2)
    assert res == -1

    print(f"all done")
