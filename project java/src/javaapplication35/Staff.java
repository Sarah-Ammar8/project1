
package javaapplication35;

public class Staff {
    private int StaffID;
    private String StaffName;
    private Department department;
    private double Salary;

    public Staff(int StaffID, String StaffName, Department department, double Salary) {
        this.StaffID = StaffID;
        this.StaffName = StaffName;
        this.department = department;
        this.Salary = Salary;
    }
    
    
    public void StaffDetails(){
        System.out.println("Staff ID: "+StaffID);
        System.out.println("Staff Name: "+StaffName);
        department.DepartmentDetails();
        System.out.println("Salary: "+Salary);
        System.out.println("------------------------------------");
    }

    public int getStaffID() {
        return StaffID;
    }

    public void setStaffID(int StaffID) {
        this.StaffID = StaffID;
    }

    public String getStaffName() {
        return StaffName;
    }

    public void setStaffName(String StaffName) {
        this.StaffName = StaffName;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

    public double getSalary() {
        return Salary;
    }

    public void setSalary(double Salary) {
        this.Salary = Salary;
    }
    
    
}
