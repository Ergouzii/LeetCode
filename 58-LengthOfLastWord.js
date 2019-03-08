/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(str) {
    let s = str.trim();
    let len = 0;
    for (let i = s.length - 1; i >= 0; i--) {
        if (s[i] === " ") {
            break;
        }
        len += 1;
    }
    return len;
};
