/**
 * @param {string} S
 * @return {number[][]}
 */
var largeGroupPositions = function(S) {
    let start = 0;
    let end = 1;
    let output = [];
    while (end < S.length) {
        while (end < S.length && S[start] == S[end]) {
            end += 1;
        }
        if ((end - start) > 2) {
            output.push([start, end - 1]);
        }
        start = end;
    }
    return output;
};
