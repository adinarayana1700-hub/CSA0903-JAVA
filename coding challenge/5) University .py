class Admission {

    void calculateFee() {
        System.out.println("UG Fee = 50000");
    }

    void calculateFee(int pg) {
        System.out.println("PG Fee = 70000");
    }

    void calculateFee(double scholarship) {
        System.out.println("Scholarship Fee = 20000");
    }
}

public class Main {
    public static void main(String[] args) {
        Admission a = new Admission();

        a.calculateFee();      // Undergraduate
        a.calculateFee(1);     // Postgraduate
        a.calculateFee(1.0);   // Scholarship
    }
}
