// import java.util.ArrayList;

class Solution {
    public double[] convertTemperature(double celsius) {
        // Non-Primitive ArrayList
        // ArrayList<Double> tempConv = new ArrayList<Double>();

        // double kelvin = celsius + 273.15;
        // tempConv.add(kelvin);

        // double fahrenheit = (celsius * (9.0 / 5.0)) + 32;
        // tempConv.add(fahrenheit);

        // double[] tempConvList = new double[tempConv.size()];

        // for (int i = 0; i < tempConv.size(); i++){
        //     tempConvList[i] = tempConv.get(i);
        // } 

        // return tempConvList;

        // Primitive Array
        double kelvin = celsius + 273.15;
        double fahrenheit = (celsius * (9.0 / 5.0)) + 32;

        // double[] tempConv = new double[2];
        // double[] tempConv = {kelvin, fahrenheit};

        // tempConv[0] = kelvin;
        // tempConv[1] = fahrenheit;

        // return tempConv;  
        return new double[] {kelvin, fahrenheit};
    }
}