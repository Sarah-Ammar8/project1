
package javaapplication35;

public class Bus {
    private int BusID;
    private String DriverName;
    private String Destination;
    private int TotalSeats;

    public Bus(int BusID, String DriverName, String Destination, int TotalSeats) {
        this.BusID = BusID;
        this.DriverName = DriverName;
        this.Destination = Destination;
        this.TotalSeats = TotalSeats;
    }
    
    public void BusDetails(){
        System.out.println("Bus ID: "+BusID);
        System.out.println("Driver Name: "+DriverName);
        System.out.println("Destination: "+Destination);
        System.out.println("Total Seats: "+TotalSeats);
    }
    
    public void SeatsAvailability(){
        System.out.println("Checking seat availability...");
    }

    public int getBusID() {
        return BusID;
    }

    public void setBusID(int BusID) {
        this.BusID = BusID;
    }

    public String getDriverName() {
        return DriverName;
    }

    public void setDriverName(String DriverName) {
        this.DriverName = DriverName;
    }

    public String getDestination() {
        return Destination;
    }

    public void setDestination(String Destination) {
        this.Destination = Destination;
    }

    public int getTotalSeats() {
        return TotalSeats;
    }

    public void setTotalSeats(int TotalSeats) {
        this.TotalSeats = TotalSeats;
    }
    
    
}
