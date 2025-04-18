
package javaapplication34;

import java.util.Scanner;

public class SEAT implements BOOKING{
    // حالة المقاعد (true = متاح، false = محجوز)
    protected boolean[] seats = {true, true, true, true, true};

    @Override
    public void displayAvailableSeats() {
        System.out.println("المقاعد المتاحة (0 لـ متاح، X لـ محجوز):");
        for (int i = 0; i < seats.length; i++) {
            System.out.print(seats[i] ? "0 " : "X ");
        }
        System.out.println();
    }

    // دالة لاختيار المقاعد
    @Override
    public void chooseSeats(int numSeats) {
        int[] chosenSeats = new int[numSeats];
        Scanner scanner = new Scanner(System.in);

        for (int i = 0; i < numSeats; i++) {
            int seatChoice;
            do {
                // طلب رقم المقعد من المستخدم
                System.out.print("أدخل رقم المقعد " + (i + 1) + " (1-5): ");
                seatChoice = scanner.nextInt();
                if (seatChoice < 1 || seatChoice > seats.length) {
                    System.out.println("رقم المقعد غير صحيح، حاول مرة أخرى.");
                } else if (!seats[seatChoice - 1]) {
                    System.out.println("المقعد غير متاح، اختر مقعدًا آخر.");
                }
            } while (seatChoice < 1 || seatChoice > seats.length || !seats[seatChoice - 1]);

            // حجز المقعد
            seats[seatChoice - 1] = false;
            chosenSeats[i] = seatChoice;
            System.out.println("تم حجز المقعد رقم " + seatChoice + " بنجاح.");
        }
    }

    // حساب عدد المقاعد المتاحة
    public int getAvailableSeatsCount() {
        int count = 0;
        for (boolean seat : seats) {
            if (seat) {
                count++;
            }
        }
        return count;
    }

}
