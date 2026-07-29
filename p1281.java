class Solution {
    public int subtractProductAndSum(int n) {
        int sum = 0;
        int pdt = 1;

        String num = Integer.toString(n);
        
        int[] numbers = new int[num.length()];

        for (int i = 0; i < num.length(); i++){
            char temp = num.charAt(i);
            // int tempNumber = (int)temp;
            numbers[i] = Character.getNumericValue(temp);
            // numbers[i] = num.charAt(i);
        }

        for (int i = 0; i < numbers.length; i++){
            sum += numbers[i];
            pdt *= numbers[i];
        }

        return pdt - sum;
    }
}