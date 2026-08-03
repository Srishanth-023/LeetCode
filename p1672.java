class Solution {
    public int maximumWealth(int[][] accounts) {
        int richest = 0, sum = 0;

        for (int[] account : accounts){
            for (int asset : account){
                sum += asset;
            }
            
            if (sum > richest){
                richest = sum;
            }
            sum = 0;
        }

        return richest;
    }
}