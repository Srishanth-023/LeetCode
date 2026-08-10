class Solution {
    public int largestAltitude(int[] gain) {
        int[] altitude = new int[gain.length + 1];
        altitude[0] = 0;
        int temp = altitude[0];
        int greatest = altitude[0];

        for (int i = 0; i < gain.length; i++){
            temp += gain[i];
            altitude[i + 1] = temp;

            if (altitude[i + 1] > greatest){
                greatest = altitude[i + 1];
            }
        }

        return greatest;
    }
}