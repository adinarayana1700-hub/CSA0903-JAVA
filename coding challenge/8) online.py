class Product {
    int price = 500;
}

class Order {
    void bill(Product p, int qty) {
        System.out.println("Total = " + (p.price * qty));
    }
}

public class Main {
    public static void main(String[] args) {
        Product p = new Product();
        Order o = new Order();

        o.bill(p, 2);
    }
}
