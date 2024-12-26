import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ParkingManagementSystem {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.println("Welcome to the Parking Management System!");
        System.out.print("Enter the maximum capacity of the parking lot: ");
        int maxCapacity = scanner.nextInt();
        scanner.nextLine();

        ParkingManagementSystem parkingSystem = new ParkingManagementSystem(maxCapacity);

        while (true) {
            System.out.println("\nChoose an option:");
            System.out.println("1. Park a vehicle");
            System.out.println("2. Unpark a vehicle");
            System.out.println("3. Show current occupancy");
            System.out.println("4. List parked vehicles");
            System.out.println("5. Check availability");
            System.out.println("6. Exit");

            int choice = scanner.nextInt();
            scanner.nextLine();

            switch (choice) {
                case 1:
                    System.out.print("Enter the vehicle name to park: ");
                    String vehicleToPark = scanner.nextLine();
                    parkingSystem.parkVehicle(vehicleToPark);
                    break;
                case 2:
                    System.out.print("Enter the vehicle name to unpark: ");
                    String vehicleToUnpark = scanner.nextLine();
                    parkingSystem.unparkVehicle(vehicleToUnpark);
                    break;
                case 3:
                    parkingSystem.printOccupancy();
                    break;
                case 4:
                    parkingSystem.listParkedVehicles();
                    break;
                case 5:
                    parkingSystem.checkAvailability();
                    break;
                case 6:
                    System.out.println("Exiting the Parking Management System. Goodbye!");
                    scanner.close();
                    return;
                default:
                    System.out.println("Invalid choice. Please try again.");
            }
        }
    }
    private int maxCapacity;
    private int currentOccupancy;

    private List<String> parkedVehicles;

    public ParkingManagementSystem(int maxCapacity) {
        this.maxCapacity = maxCapacity;
        this.currentOccupancy = 0;
        this.parkedVehicles = new ArrayList<>();
    }

    public boolean parkVehicle(String vehicle) {
        if (currentOccupancy >= maxCapacity) {
            System.out.println("Parking lot is full.");
            return false;
        } else if (parkedVehicles.contains(vehicle)) {
            System.out.println("Vehicle " + vehicle + " is already parked.");
            return false;
        } else {
            parkedVehicles.add(vehicle);
            currentOccupancy++;
            System.out.println("Vehicle " + vehicle + " parked successfully.");
            return true;
        }
    }

    public boolean unparkVehicle(String vehicle) {
        if (parkedVehicles.contains(vehicle)) {
            parkedVehicles.remove(vehicle);
            currentOccupancy--;
            System.out.println("Vehicle " + vehicle + " unparked successfully.");
            return true;
        } else {
            System.out.println("Vehicle " + vehicle + " is not parked in the parking lot.");
            return false;
        }
    }

    public void printOccupancy() {
        System.out.println("Current occupancy: " + currentOccupancy + " out of " + maxCapacity);
    }

    public void listParkedVehicles() {
        if (parkedVehicles.isEmpty()) {
            System.out.println("No vehicles are currently parked.");
        } else {
            System.out.println("Parked vehicles: " + String.join(", ", parkedVehicles));
        }
    }

    public void checkAvailability() {
        int availableSpots = maxCapacity - currentOccupancy;
        System.out.println("Available spots: " + availableSpots);
    }
}
