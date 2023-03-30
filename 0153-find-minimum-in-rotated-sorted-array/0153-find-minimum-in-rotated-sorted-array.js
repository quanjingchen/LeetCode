/**
 * @param {number[]} nums
 * @return {number}
 */
var findMin = function(nums) {
    var left = 0;
    var right = nums.length - 1;
    if (nums[left] < nums[right]) {
        return nums[left];
    }
    while (left < right) {
        var mid = Math.floor((left + right) / 2);
        if (nums[mid] > nums[right]) {
            left = mid + 1;
        } else if (nums[mid] < nums[right]) {
            right = mid;
        }
        
    }
    
    return nums[right];
    
};