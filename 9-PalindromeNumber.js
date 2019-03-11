/**
 * @param {number} x
 * @return {boolean}
 */
var isPalindrome = function(x) {
    let s = String(x);
    let left = 0;
    let right = s.length - 1;
    while (left < right) {
        if (s[left] === s[right]) {
            left += 1;
            right -= 1;
        } else {
            return false;
        }
    }
    return true;
};