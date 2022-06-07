/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
    // console.log(nums)
    nums.sort((a, b) => a > b ? 1 : a < b ? -1 : 0);
    // console.log(nums)

    i = 0;
    j = nums.length - 1;

    while (i < j) {
        console.log(i, j)
        if (nums[i] + nums[j] > target) {
            j -= 1;
        } else if (nums[i] + nums[j] < target) {
            i += 1;
        } else {
            return [i, j]
        };
    };

    return undefined
};

ans = twoSum([9, 3, 5, 8, 3, 9, 3], 8)
console.log("ans is: " + ans)