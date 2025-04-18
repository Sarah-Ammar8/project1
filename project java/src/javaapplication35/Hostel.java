
package javaapplication35;

public class Hostel {
    private int StudenID;
    private String BlockNumber;
    private String RoomNumber;

    public Hostel(int StudenID, String BlockNumber, String RoomNumber) {
        this.StudenID = StudenID;
        this.BlockNumber = BlockNumber;
        this.RoomNumber = RoomNumber;
    }
    
    
    public void HostelDetails(){
        System.out.println("Block Number: "+BlockNumber);
        System.out.println("Room Number: "+RoomNumber);
        System.out.println("------------------------------------");
    }
    public void CheckIn(){
        System.out.println("Student "+StudenID+" cheaked in.");
    }
    public void CheckOut(){
        System.out.println("Student "+StudenID+" cheaked out.");
    }

    public int getStudenID() {
        return StudenID;
    }

    public void setStudenID(int StudenID) {
        this.StudenID = StudenID;
    }

    public String getBlockNumber() {
        return BlockNumber;
    }

    public void setBlockNumber(String BlockNumber) {
        this.BlockNumber = BlockNumber;
    }

    public String getRoomNumber() {
        return RoomNumber;
    }

    public void setRoomNumber(String RoomNumber) {
        this.RoomNumber = RoomNumber;
    }
    
    
}
