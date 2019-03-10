/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    let len = nums.length
    if (len <= 1) {
        return len
    }
    let left = 0;
    let right = 1;
    while (right < len) {
        if (nums[left] !== nums[right]) {
            left += 1;
            nums[left] = nums[right];
        }
        right += 1
    }
    return left + 1
};
