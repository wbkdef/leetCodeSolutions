"""
From: https://leetcode.com/problems/next-permutation/
PC:KEYoViX:
"""


class Solution:
    def nextPermutation(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                all_nums = nums[i-1:]
                next_biggest = min([v for v in all_nums if v > nums[i-1]])
                all_nums.remove(next_biggest)
                nums[i-1] = next_biggest

                for j, v in enumerate(sorted(all_nums)):
                    nums[i+j] = v
                break
        else:
            # make smallest permutation
            for j, v in enumerate(sorted(nums)):
                nums[j] = v


if __name__ == "__main__":
    nums = [1, 2, 3]
    Solution().nextPermutation(nums)
    assert nums == [1, 3, 2]

    nums = [3,2,1]
    Solution().nextPermutation(nums)
    assert nums == [1, 2, 3]

    nums = [1,1,5]
    Solution().nextPermutation(nums)
    assert nums == [1, 5, 1]

    nums = [1, 2, 5, 4, 0]
    Solution().nextPermutation(nums)
    assert nums == [1, 4, 0, 2, 5]

    nums = []
    Solution().nextPermutation(nums)
    assert nums == []

    nums = [8]
    Solution().nextPermutation(nums)
    assert nums == [8]

    print(f"all done")
