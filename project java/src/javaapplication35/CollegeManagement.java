
package javaapplication35;

import java.util.List;

public class CollegeManagement {
    private String CollegeName;
    private String City;
    private String ContactNumber;
    private List<Department> departments;

    public CollegeManagement(String CollegeName, String City, String ContactNumber,List<Department> departments) {
        this.CollegeName = CollegeName;
        this.City = City;
        this.ContactNumber = ContactNumber;
        this.departments=departments;
    }
    
    
    public void Open(){
        System.out.println("Collage is now open.");
    }
    public void CollegeDetails(){
        System.out.println("Colage Name: "+CollegeName);
        System.out.println("City: "+City);
        System.out.println("Contact Number: "+ContactNumber);
        System.out.println("Departments: ");
        for (Department department:departments){
            department.DepartmentDetails();
        }
        System.out.println("------------------------------------");
        
    }

    public String getCollegeName() {
        return CollegeName;
    }

    public void setCollegeName(String CollegeName) {
        this.CollegeName = CollegeName;
    }

    public String getCity() {
        return City;
    }

    public void setCity(String City) {
        this.City = City;
    }

    public String getContactNumber() {
        return ContactNumber;
    }

    public void setContactNumber(String ContactNumber) {
        this.ContactNumber = ContactNumber;
    }
     
    
}
