"""
From: https://leetcode.com/problems/search-in-rotated-sorted-array-ii/
"""


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        return self.search_(nums, target, 0, len(nums) - 1)

    def search_(self, nums: list[int], target: int,
                ind_low: int, ind_high: int) -> bool:
        low = nums[ind_low]
        high = nums[ind_high]
        ind_mid = (ind_low + ind_high)//2
        if low == target or high == target:
            return True
        if ind_low >= ind_high - 1:
            return False
        if low < high:
            # Numbers Should be ordered in-between ind_low and ind_high
            if low < target < high:
                return self.search_(nums, target, ind_low, ind_mid)\
                       or self.search_(nums, target, ind_mid, ind_high)
            else:
                return False
        elif high <= low:
            # Numbers Should be high and increasing to the left of this
            # interval, then jump down and increase again up to low
            if high < target < low:
                return False
            else:
                return self.search_(nums, target, ind_low, ind_mid)\
                       or self.search_(nums, target, ind_mid, ind_high)


if __name__ == "__main__":
    assert Solution().search(nums = [2,5,6,0,0,1,2], target = 0) == True
    assert Solution().search(nums = [2,5,6,0,0,1,2], target = 3) == False

    print(f"all done")
