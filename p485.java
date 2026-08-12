class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int count = 0;
        int highestCount = 0;

        for (int num : nums){
            if (num == 1){
                count++;
                // if (count > highestCount){
                //     highestCount = count;
                // }
            } else{
                highestCount = Math.max(highestCount, count);
                count = 0;
            }
        }

        // return highestCount;
        return highestCount > count ? highestCount : count;
    }
}