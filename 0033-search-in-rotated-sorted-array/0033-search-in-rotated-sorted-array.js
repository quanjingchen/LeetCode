/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    var min = findMin(nums);
    if (min === 0) {
        return binarySearch(nums, target);
    }
    
    if (target < nums[0] && target > nums[nums.length - 1]) {
        return -1;
    }
    
    if (target >= nums[0]) {
        return binarySearch(nums.slice(0, min), target);
    }
    
    var ans = binarySearch(nums.slice(min, nums.length), target);    
    if (ans === -1) return -1;
    return ans + min;
};

var findMin = function(nums) {
    var low = 0;
    var high = nums.length - 1;
    if (nums[low] < nums[high]) {
        return low;
    }
    while (low < high) {
        var mid = Math.floor((low + high) / 2);
        if (nums[mid] > nums[high]) {
            low = mid + 1;
        } else if (nums[mid] < nums[high]) {
            high = mid;
        }
    }
    return low;
}

var binarySearch = function(nums, target) {
    var low = 0;
    var high = nums.length - 1;
    while (low <= high) {
        var mid = Math.floor((low + high) / 2);
        if (nums[mid] > target) {
            high = mid - 1;
        } else if (nums[mid] < target) {
            low = mid + 1;
        } else {
            return mid
        }
    }
    return -1; 
}