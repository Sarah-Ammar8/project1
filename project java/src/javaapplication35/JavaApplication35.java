
package javaapplication35;

import java.util.ArrayList;
import java.util.List;

public class JavaApplication35 {

    public static void main(String[] args) {
        // انشاء قسم
        Department csDepartment=new Department(1,"Computer Scinece","Dr.Ammar",30,200);
        
        // انشاء مدرجات
        ArrayList<String> events=new ArrayList<>();
        events.add("Tech Talk");
        events.add("Cultural Fest");
        Auditorium auditorium=new Auditorium("Main Auditorium",events,"2024-09-25","10:00 AM",500,csDepartment);
        csDepartment.addAuditorium(auditorium);
        
        // انشاء صف دراسي
        Classroom classroom=new Classroom(101,"A",csDepartment);
        
        // انشاء سكن
        Hostel hostel=new Hostel(1,"Block A","Room 101");
        
        // انشاء طالب وربطه بالصف والسكن
        Student student1=new Student(1,"Ahmmed","Male",3,classroom,hostel);
        
        // اضافة الطالب الى القسم
        List<Student> students=new ArrayList<>();
        students.add(student1);
        csDepartment=new Department(1,"Computer Scinece","Dr.Ammar",30,200);
        
        // انشاء ادارة الكلية وربط القسم بها
        List<Department> departments=new ArrayList<>();
        departments.add(csDepartment);
        CollegeManagement collage=new CollegeManagement("Engineering Collage","Cairo","123456789",departments);
        
        // عرض تفاصيل الكلية
        collage.CollegeDetails();
        
        // عرض تفاصيل الطالب
        student1.StudentDelatails();
        
    }
    
}
