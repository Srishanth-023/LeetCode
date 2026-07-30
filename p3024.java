class Solution {
    public String triangleType(int[] nums) {
        boolean res1 = (nums[0] + nums[1]) > nums[2]; 
        boolean res2 = (nums[0] + nums[2]) > nums[1]; 
        boolean res3 = (nums[1] + nums[2]) > nums[0];

        if (res1 && res2 && res3){
            if (nums[0] == nums[1] && nums[0] == nums[2]){
                return "equilateral";
            } else if (nums[0] != nums[1] && nums[0] != nums[2] && nums[1] != nums[2]){
                return "scalene";
            }
        } else{
            return "none";
        }

        return "isosceles";
    }
}