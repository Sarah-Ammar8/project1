
package javaapplication35;

import java.util.List;

public class Auditorium {
    private String AuditoriumName;
    private List<String> EventList;
    private String Date;
    private String Time;
    private int TotalSeats;
    private Department department;

    public Auditorium(String AuditoriumName, List<String> EventList, String Date, String Time, int TotalSeats, Department department) {
        this.AuditoriumName = AuditoriumName;
        this.EventList = EventList;
        this.Date = Date;
        this.Time = Time;
        this.TotalSeats = TotalSeats;
        this.department = department;
    }
    
    
    public void BookEvents(String event){
        EventList.add(event);
        System.out.println("Event \'"+event+"\' has been booked in the auditorium.");
    }

    public String getAuditoriumName() {
        return AuditoriumName;
    }

    public void setAuditoriumName(String AuditoriumName) {
        this.AuditoriumName = AuditoriumName;
    }

    public List<String> getEventList() {
        return EventList;
    }

    public void setEventList(List<String> EventList) {
        this.EventList = EventList;
    }

    public String getDate() {
        return Date;
    }

    public void setDate(String Date) {
        this.Date = Date;
    }

    public String getTime() {
        return Time;
    }

    public void setTime(String Time) {
        this.Time = Time;
    }

    public int getTotalSeats() {
        return TotalSeats;
    }

    public void setTotalSeats(int TotalSeats) {
        this.TotalSeats = TotalSeats;
    }

    public Department getDepartment() {
        return department;
    }

    public void setDepartment(Department department) {
        this.department = department;
    }
    
    
}
