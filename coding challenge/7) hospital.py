interface MedicalRecord {
    void addRecord();
    void displayRecord();
}

class Patient implements MedicalRecord {
    public void addRecord() {
        System.out.println("Patient Record Added");
    }

    public void displayRecord() {
        System.out.println("Patient Record");
    }
}

class Doctor implements MedicalRecord {
    public void addRecord() {
        System.out.println("Doctor Record Added");
    }

    public void displayRecord() {
        System.out.println("Doctor Record");
    }
}

public class Main {
    public static void main(String[] args) {
        MedicalRecord p = new Patient();
        MedicalRecord d = new Doctor();

        p.addRecord();
        p.displayRecord();

        d.addRecord();
        d.displayRecord();
    }
}
