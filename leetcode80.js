/**
 * @param {number[]} nums
 * @return {number}
 */
var removeDuplicates = function(nums) {
    var count=0;
    if(nums.length<2){
        return nums.length;
    }
    var l=2,r=2; //l慢指针表示处理出的数组的长度，r快指针表示已经检查过的数组的长度
    while(r<nums.length){
        if(nums[l-2]!=nums[r]){
            nums[l]=nums[r];
            ++l; 
        }
        ++r;
    }
    return l;
};