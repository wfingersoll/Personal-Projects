public class DrivingCost {

    public static double drivingCost(double drivenMiles, double milesPerGallon, double dollarsPerGallon) {
        return((drivenMiles/milesPerGallon)*dollarsPerGallon);
    }

    public static void main(String args[]) {
        double milesPerGallon = Double.parseDouble(args[0]);
        double dollarsPerGallon = Double.parseDouble(args[1]);

        System.out.printf("\n%.2f", drivingCost(10, milesPerGallon, dollarsPerGallon));
        System.out.printf("\n%.2f", drivingCost(50, milesPerGallon, dollarsPerGallon));
        System.out.printf("\n%.2f", drivingCost(400, milesPerGallon, dollarsPerGallon));
    }
 
}