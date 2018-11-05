class Solution {
    public int missingNumber(int[] nums) {
        int sum1 = nums.length;
        int sum2 = 0;
        for(int i = 0; i < nums.length; i++) {
            sum1 += i;
            sum2 += nums[i];
    }
        return sum1 - sum2;
    }
}