
package javaapplication35;

public class Student {
    private int StudenID;
    private String StudentName;
    private String Gender;
    private int Year;
    private Classroom classromm;
    private Hostel hostel;

    public Student(int StudenID, String StudentName, String Gender, int Year,Classroom classromm,Hostel hostel) {
        this.StudenID = StudenID;
        this.StudentName = StudentName;
        this.Gender = Gender;
        this.Year = Year;
        this.classromm=classromm;
        this.hostel=hostel;
        
    }
    
    public void StudentDelatails(){
        System.out.println("Studen ID: "+StudenID);
        System.out.println("Studen Name: "+StudentName);
        System.out.println("Gender: "+Gender);
        System.out.println("Year: "+Year);
        classromm.ClassrommDetails();
        if (hostel != null){
            hostel.HostelDetails();
        }
        System.out.println("------------------------------------");
    }
    
    public void PayFees(){
        System.out.println(StudentName+" has paid the fees.");
    }
    public void IsPresent(){
        System.out.println(StudentName+" is persent.");
    }

    public int getStudenID() {
        return StudenID;
    }

    public void setStudenID(int StudenID) {
        this.StudenID = StudenID;
    }

    public String getStudentName() {
        return StudentName;
    }

    public void setStudentName(String StudentName) {
        this.StudentName = StudentName;
    }

    public String getGender() {
        return Gender;
    }

    public void setGender(String Gender) {
        this.Gender = Gender;
    }

    public int getYear() {
        return Year;
    }

    public void setYear(int Year) {
        this.Year = Year;
    }

    public Classroom getClassromm() {
        return classromm;
    }

    public void setClassromm(Classroom classromm) {
        this.classromm = classromm;
    }

    public Hostel getHostel() {
        return hostel;
    }

    public void setHostel(Hostel hostel) {
        this.hostel = hostel;
    }

  
    
    
}
