/**
 * @param {number[]} nums
 * @return {number}
 */
var majorityElement = function(nums) {
    var a = {};
    var majority = Math.floor(nums.length / 2);
    for(let i=0;i<nums.length;i++){
        //必须对a进行初始化，否则会报错
        if (a[nums[i]] == null) {
            a[nums[i]] = 0;
        }
            a[nums[i]]++;
            if(a[nums[i]]>majority){
                return nums[i];
            }
    }
   
};
var majorityElement = function(nums) {
    var count = {};
    var majorityCount = Math.floor(nums.length / 2);

    for (let i = 0; i < nums.length; i++) {
        if (count[nums[i]] == null) {
            count[nums[i]] = 0;
        }
        count[nums[i]]++;
        
        if (count[nums[i]] > majorityCount) {
            return nums[i];
        }
    }
};
