abstract class Shape {
    abstract void area();
}

class Circle extends Shape {
    void area() {
        System.out.println("Circle Area = " + (3.14 * 5 * 5));
    }
}

class Rectangle extends Shape {
    void area() {
        System.out.println("Rectangle Area = " + (4 * 6));
    }
}

class Triangle extends Shape {
    void area() {
        System.out.println("Triangle Area = " + (0.5 * 4 * 5));
    }
}

public class Main {
    public static void main(String[] args) {
        Shape[] s = {
            new Circle(),
            new Rectangle(),
            new Triangle()
        };

        for (Shape x : s)
            x.area();
    }
}
