/**
 * @param {number[]} nums
 * @return {number}
 */
var missingNumber = function(nums) {
    let inputSum = nums.reduce((a, b) => {return a + b}, 0);
    let n = nums.length;
    return parseInt(n * (n + 1) / 2) - inputSum;
};