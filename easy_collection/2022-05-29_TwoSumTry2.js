/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
function twoSum(nums, target) {
    numsToInds = {};
    for (key = 0; key < nums.length; key += 1){
        value = nums[key]
        let complement = target - value;
        // console.log(key, value, complement);
        if (numsToInds.hasOwnProperty(complement)) {
            return [key, numsToInds[complement]]
        };
        numsToInds[value] = key;
        // console.log(numsToInds);
    };
    // console.log(numsToInds);
};

ans = twoSum([9, 3, 5, 8, 3, 9, 3], 8)
console.log("ans is: " + ans)