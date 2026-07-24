class Device {
    void show() {
        System.out.println("Device");
    }
}

class Light extends Device {
    void show() {
        System.out.println("Light ON - Power: 20W");
    }
}

class Fan extends Device {
    void show() {
        System.out.println("Fan ON - Power: 75W");
    }
}

class AirConditioner extends Device {
    void show() {
        System.out.println("AC ON - Power: 1500W");
    }
}

public class Main {
    public static void main(String[] args) {
        Device[] d = {
            new Light(),
            new Fan(),
            new AirConditioner()
        };

        for (Device x : d)
            x.show();
    }
}
