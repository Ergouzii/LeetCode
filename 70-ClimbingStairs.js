/**
 * @param {number} n
 * @return {number}
 */
var climbStairs = function(n) {
    let dp1 = 1;
    let dp2 = 2;
    let dp_step = 0;
    if (n == 1) {
        return dp1;
    } else if (n == 2) {
        return dp2;
    }
    while (n > 2) {
        dp_step = dp1 + dp2;
        dp1 = dp2;
        dp2 = dp_step;
        n -= 1;
    }
    return dp_step
};
