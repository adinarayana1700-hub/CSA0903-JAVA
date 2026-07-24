class Student {
    int roll;
    String name;
    int m1, m2, m3;

    Student(int r, String n, int a, int b, int c) {
        roll = r;
        name = n;
        m1 = a;
        m2 = b;
        m3 = c;
    }

    int total() {
        return m1 + m2 + m3;
    }

    double average() {
        return total() / 3.0;
    }

    String grade() {
        if (average() >= 90) return "A";
        else if (average() >= 75) return "B";
        else if (average() >= 50) return "C";
        else return "Fail";
    }
}

public class Main {
    public static void main(String[] args) {
        Student[] s = {
            new Student(1, "Ravi", 90, 85, 95),
            new Student(2, "Sita", 80, 75, 70)
        };

        Student topper = s[0];

        for (Student x : s) {
            System.out.println(x.name + " Total=" + x.total() +
                    " Avg=" + x.average() +
                    " Grade=" + x.grade());

            if (x.total() > topper.total())
                topper = x;
        }

        System.out.println("Topper: " + topper.name);
    }
}
