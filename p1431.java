class Solution {
    public List<Boolean> kidsWithCandies(int[] candies, int extraCandies) {
        // boolean[] result = new boolean[candies.length];
        List<Boolean> result = new ArrayList<>();

        int greatest = 0;
        for (int candy : candies){
            if (candy > greatest){
                greatest = candy;
            }
        }

        for (int i = 0; i < candies.length; i++){
            candies[i] += extraCandies;

            if (candies[i] >= greatest){
                result.add(i, true);
            } else{
                result.add(i, false);
            }
        }

        return result;
    }
}