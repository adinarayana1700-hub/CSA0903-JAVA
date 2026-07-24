import java.util.*;

class Book {
    private int id;
    private String title;
    private boolean issued;

    Book(int id, String title) {
        this.id = id;
        this.title = title;
        issued = false;
    }

    void issue() {
        if (!issued) {
            issued = true;
            System.out.println("Book Issued");
        } else
            System.out.println("Already Issued");
    }

    void ret() {
        issued = false;
        System.out.println("Book Returned");
    }

    void display() {
        System.out.println(id + " " + title + " " + (issued ? "Issued" : "Available"));
    }

    int getId() {
        return id;
    }
}

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        Book[] b = new Book[2];
        b[0] = new Book(101, "Java");
        b[1] = new Book(102, "Python");

        int id = sc.nextInt();

        for (Book x : b)
            if (x.getId() == id) {
                x.display();
                x.issue();
                x.ret();
                x.display();
            }
    }
}
