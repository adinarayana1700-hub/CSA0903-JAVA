class Vehicle {
    void calculateRent(int days) {
        System.out.println("Rent");
    }
}

class Car extends Vehicle {
    void calculateRent(int days) {
        System.out.println("Car Rent = " + (days * 1000));
    }
}

class Bike extends Vehicle {
    void calculateRent(int days) {
        System.out.println("Bike Rent = " + (days * 300));
    }
}

class Bus extends Vehicle {
    void calculateRent(int days) {
        System.out.println("Bus Rent = " + (days * 2000));
    }
}

public class Main {
    public static void main(String[] args) {
        Vehicle[] v = {
            new Car(),
            new Bike(),
            new Bus()
        };

        int days = 3;

        for (Vehicle x : v)
            x.calculateRent(days);
    }
}
