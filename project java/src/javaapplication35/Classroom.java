
package javaapplication35;

public class Classroom {
    private int ClasslD;
    private String Section;
    private Department department;
    private boolean IsOccupied;

    public Classroom(int ClasslD, String Section,Department department) {
        this.ClasslD = ClasslD;
        this.Section = Section;
        this.department = department;
        this.IsOccupied=false;
    }


    
    public void ClassrommDetails(){
        System.out.println("Class lD: "+ClasslD);
        System.out.println("Section: "+Section);
        department.DepartmentDetails();
    }
    
    public void IsOccupied(boolean IsOccupied){
        if(IsOccupied){
            System.out.println("Classroom is currently occupied.");
        }
        else{
            System.out.println("Classroom is available.");
        }
    }

    public int getClasslD() {
        return ClasslD;
    }

    public void setClasslD(int ClasslD) {
        this.ClasslD = ClasslD;
    }

    public String getSection() {
        return Section;
    }

    public void setSection(String Section) {
        this.Section = Section;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }

    public boolean isIsOccupied() {
        return IsOccupied;
    }

    public void setIsOccupied(boolean IsOccupied) {
        this.IsOccupied = IsOccupied;
    }

    
    
    
}
