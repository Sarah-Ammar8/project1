
package javaapplication35;

import java.util.ArrayList;
import java.util.List;

public class Department  {
    private int DepartmentID;
    private String DepartmentName;
    private String HoName;
    private int TotalStaffs;
    private int TotalStudents;
    private List<Student> studens;
    private List<Staff> staffs;
    private List<Auditorium> auditoriums;
    

    public Department(int DepartmentID, String DepartmentName, String HoName, int TotalStaffs, int TotalStudents) {
        this.DepartmentID = DepartmentID;
        this.DepartmentName = DepartmentName;
        this.HoName = HoName;
        this.TotalStaffs = TotalStaffs;
        this.TotalStudents = TotalStudents;
        this.studens=studens;
        this.staffs=staffs;
        this.auditoriums = new ArrayList<>(); 
    }
    
    
    public void DepartmentDetails(){
        System.out.println("Department ID: "+DepartmentID);
        System.out.println("Department Name: "+DepartmentName);
        System.out.println("Head of Department: "+HoName);
        System.out.println("Total Staffs: "+TotalStaffs);
        System.out.println("Total Students: "+TotalStudents);
        System.out.println("------------------------------------");
    }
    
    public void ShowEvents(){
        System.out.println("Showing department event...");
    }
    
    public void addAuditorium(Auditorium auditorium){
        auditoriums.add(auditorium);
    }
    

    public int getDepartmentID() {
        return DepartmentID;
    }

    public void setDepartmentID(int DepartmentID) {
        this.DepartmentID = DepartmentID;
    }

    public String getDepartmentName() {
        return DepartmentName;
    }

    public void setDepartmentName(String DepartmentName) {
        this.DepartmentName = DepartmentName;
    }

    public String getHoName() {
        return HoName;
    }

    public void setHoName(String HoName) {
        this.HoName = HoName;
    }

    public int getTotalStaffs() {
        return TotalStaffs;
    }

    public void setTotalStaffs(int TotalStaffs) {
        this.TotalStaffs = TotalStaffs;
    }

    public int getTotalStudents() {
        return TotalStudents;
    }

    public void setTotalStudents(int TotalStudents) {
        this.TotalStudents = TotalStudents;
    }

    public List<Student> getStudens() {
        return studens;
    }

    public void setStudens(List<Student> studens) {
        this.studens = studens;
    }

    public List<Staff> getStaffs() {
        return staffs;
    }

    public void setStaffs(List<Staff> staffs) {
        this.staffs = staffs;
    }

    public List<Auditorium> getAuditoriums() {
        return auditoriums;
    }

    public void setAuditoriums(List<Auditorium> auditoriums) {
        this.auditoriums = auditoriums;
    }
    
    
}
