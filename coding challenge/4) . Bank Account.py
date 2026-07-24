class BankAccount {
    private int accNo;
    private String name;
    private double balance;

    BankAccount(int a, String n, double b) {
        accNo = a;
        name = n;
        balance = b;
    }

    void deposit(double amt) {
        balance += amt;
    }

    void withdraw(double amt) {
        if (amt <= balance)
            balance -= amt;
        else
            System.out.println("Insufficient Balance");
    }

    void showBalance() {
        System.out.println("Balance = " + balance);
    }
}

public class Main {
    public static void main(String[] args) {
        BankAccount b = new BankAccount(101, "Ravi", 5000);

        b.deposit(1000);
        b.withdraw(2000);
        b.showBalance();
    }
}
