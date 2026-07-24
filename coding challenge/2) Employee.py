class Employee {
    String name;

    Employee(String name) {
        this.name = name;
    }

    void calculateSalary() {
        System.out.println("Salary");
    }
}

class PermanentEmployee extends Employee {
    PermanentEmployee(String name) {
        super(name);
    }

    void calculateSalary() {
        System.out.println(name + " Salary = 50000");
    }
}

class ContractEmployee extends Employee {
    ContractEmployee(String name) {
        super(name);
    }

    void calculateSalary() {
        System.out.println(name + " Salary = 20000");
    }
}

public class Main {
    public static void main(String[] args) {
        Employee e;

        e = new PermanentEmployee("Ravi");
        e.calculateSalary();

        e = new ContractEmployee("Sita");
        e.calculateSalary();
    }
}
