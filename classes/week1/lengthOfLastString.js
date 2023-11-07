/**
 * @param {string} s
 * @return {number}
 */
var lengthOfLastWord = function(s) {
    let trimmedString = s.trim();
    splitString = trimmedString.split(` `)
    arrayLength = splitString.length
    lastWordIndex = arrayLength - 1
    lastWord = splitString[lastWordIndex]
    return lastWord.length;
};

