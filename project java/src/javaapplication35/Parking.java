
package javaapplication35;

public class Parking {
    private int Slotld;
    private String VehicleNumber;
    private String VehicleOwnerName;

    public Parking(int Slotld, String VehicleNumber, String VehicleOwnerName) {
        this.Slotld = Slotld;
        this.VehicleNumber = VehicleNumber;
        this.VehicleOwnerName = VehicleOwnerName;
    }

    
    public void ParkVehicle(){
        System.out.println("Vehicle "+VehicleNumber+" parked by "+VehicleOwnerName);
    }
            
     public int getSlotld() {
        return Slotld;
    }

    public void setSlotld(int Slotld) {
        this.Slotld = Slotld;
    }

    public String getVehicleNumber() {
        return VehicleNumber;
    }

    public void setVehicleNumber(String VehicleNumber) {
        this.VehicleNumber = VehicleNumber;
    }

    public String getVehicleOwnerName() {
        return VehicleOwnerName;
    }

    public void setVehicleOwnerName(String VehicleOwnerName) {
        this.VehicleOwnerName = VehicleOwnerName;
    }
    
}
