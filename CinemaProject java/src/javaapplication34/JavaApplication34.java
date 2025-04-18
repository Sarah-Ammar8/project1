
package javaapplication34;

import java.util.Scanner;

public class JavaApplication34 {

   
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // 1. الترحيب بالمستخدم
        System.out.println("مرحبًا بك في نظام حجز السينما!");

        // 2. إنشاء حساب
        USER user = new USER();
        user.createAccount(scanner);

        // 3. التحقق من العمر
        System.out.print("أدخل عمرك: ");
        int age = scanner.nextInt();
        if (age < 18) {
            System.out.println("عذراً، بعض الأفلام غير متاحة لمن هم أقل من 18 عامًا.");
        }

        // 4. اختيار السينما
        CINEMA cinema = new CINEMA();
        cinema.chooseCinema();

        // 5. اختيار الفيلم ووقت العرض
        MOVIE movie = new MOVIE();
        movie.chooseMovie();

        // 6. حجز المقاعد
        System.out.println("هل تريد حجز مقاعد VIP؟ (نعم/لا)");
        String vipChoice = scanner.next();

        SEAT seat;  // استخدام الهيمنة (Polymorphism)
        int ticketPrice = 50;

        if (vipChoice.equalsIgnoreCase("نعم")) {
            seat = new VIP();  // إنشاء كائن من VIP
            ticketPrice = ((VIP) seat).getVIPPrice(ticketPrice);  // حساب السعر الخاص بـ VIP
        } else {
            seat = new SEAT();  // إنشاء كائن من نوع Seat
        }

        // عرض المقاعد المتاحة
        seat.displayAvailableSeats();

        System.out.println("كم عدد المقاعد التي تريد حجزها؟");
        int numSeats = scanner.nextInt();

        // التحقق من توفر عدد المقاعد المطلوب
        if (numSeats > seat.getAvailableSeatsCount()) {
            System.out.println("عذراً، لا توجد مقاعد كافية متاحة. المتاح هو " + seat.getAvailableSeatsCount() + " مقعد.");
        } else {
            seat.chooseSeats(numSeats);
        }

        // 7. حساب السعر والدفع
        MONEY payment = new MONEY(ticketPrice * numSeats);
        payment.processPayment();

        // 8. تأكيد الحجز
        System.out.println("تم الحجز بنجاح! استمتع بمشاهدة فيلم " + movie.getSelectedMovie() + " في " + cinema.getSelectedCinema() + " في وقت " + movie.getSelectedTime());
    }

    }
    

