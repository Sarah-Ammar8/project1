
package javaapplication34;

import java.util.Scanner;

public class MONEY {
    private int ticketPrice;

    public MONEY(int price) {
        this.ticketPrice = price;
    }

    // عملية الدفع الأساسية
    public void processPayment() {
        System.out.println("سعر التذكرة: " + ticketPrice + " ريال");

        Scanner scanner = new Scanner(System.in);
        int money;
        do {
            // المستخدم يدخل المبلغ المطلوب للدفع
            System.out.print("أدخل المبلغ للدفع: ");
            money = scanner.nextInt();
            if (money < ticketPrice) {
                System.out.println("المبلغ غير كافٍ، حاول مرة أخرى.");
            }
        } while (money < ticketPrice);

        // التأكيد على الدفع
        if (money > ticketPrice) {
            System.out.println("تم الدفع بنجاح. الباقي: " + (money - ticketPrice) + " ريال.");
        } else {
            System.out.println("تم الدفع بنجاح.");
        }
    }

    // تحميل زائد لدعم الدفع بواسطة البطاقة
    public void processPayment(String cardNumber) {
        System.out.println("تم الدفع باستخدام البطاقة: " + cardNumber);
    }

}
