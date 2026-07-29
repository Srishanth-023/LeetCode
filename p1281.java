class Solution {
    public int subtractProductAndSum(int n) {
        int sum = 0, pdt = 1;

        // // My solution
        // String num = Integer.toString(n);
        
        // int[] numbers = new int[num.length()];

        // for (int i = 0; i < num.length(); i++){
        //     char temp = num.charAt(i);
        //     // int tempNumber = (int)temp;
        //     numbers[i] = Character.getNumericValue(temp);
        //     // numbers[i] = num.charAt(i);
        // }

        // for (int i = 0; i < numbers.length; i++){
        //     sum += numbers[i];
        //     pdt *= numbers[i];
        // }

        // return pdt - sum;


        // General approach
        int num;
        while (n > 0){
            num = n % 10; // sum += n % 10; pdt *= n % 10; n /= 10;
            sum += num;
            pdt *= num;
            n = n / 10;
        }

        return pdt - sum;
    }
}