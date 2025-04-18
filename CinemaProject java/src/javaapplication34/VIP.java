
package javaapplication34;

public class VIP extends SEAT{
    @Override
    public void chooseSeats(int numSeats) {
        System.out.println("أنت تحجز مقاعد VIP!");
        super.chooseSeats(numSeats);  // استدعاء دالة الكلاس الأب
    }

    @Override
    public void displayAvailableSeats() {
        System.out.println("المقاعد VIP المتاحة (0 لـ متاح، X لـ محجوز):");
        super.displayAvailableSeats();
    }

    // حساب السعر الخاص بمقاعد VIP
    public int getVIPPrice(int ticketPrice) {
        return ticketPrice + 20;  // سعر VIP أعلى بـ 20 ريال
    }

}
