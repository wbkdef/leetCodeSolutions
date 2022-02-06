"""
From: https://leetcode.com/problems/sort-colors/
"""


class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.nums = nums
        self.move({0}, {1, 2})
        self.move({0, 1}, {2})

        # self.sortColors_one_pass(nums)

    def move(self, to_left: set[int], to_right: set[int]):
        left = 0
        right = len(self.nums) - 1
        while left < right:
            if self.nums[left] in to_left:
                left += 1
                continue
            if self.nums[right] in to_right:
                right -= 1
                continue
            self.nums[left], self.nums[right] \
                = self.nums[right], self.nums[left]

    def sortColors_one_pass(self,
                            nums: list[int]) -> None:
        """ A one pass approach.  I definitely think that two simpler passes
        is preferrable!  And still O(n)! """
        head_0s = 0
        head_1s = 0
        head_2s = len(nums) - 1
        while head_1s <= head_2s:
            if nums[head_0s] == 0:
                head_0s += 1
                # b/c this only happens at the start when there are no ones yet
                head_1s += 1
                continue
            if nums[head_1s] == 1:
                head_1s += 1
                continue
            if nums[head_2s] == 2:
                head_2s -= 1
                continue

            if nums[head_1s] == 0:
                nums[head_0s], nums[head_1s] = \
                    nums[head_1s], nums[head_0s]
                continue
            if nums[head_2s] == 0:
                nums[head_0s], nums[head_2s] = \
                    nums[head_2s], nums[head_0s]
                continue

            assert nums[head_1s] == 2
            assert nums[head_2s] == 1
            nums[head_1s], nums[head_2s] = \
                nums[head_2s], nums[head_1s]
            head_1s += 1
            head_2s -= 1

if __name__ == "__main__":
    inp = [2, 0, 2, 1, 1, 0]
    Solution().sortColors(inp)
    assert inp == [0,0,1,1,2,2]

    inp = [2,0,1]
    Solution().sortColors(inp)
    assert inp == [0,1,2]

    print(f"all done")
