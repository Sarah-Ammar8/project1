
package javaapplication34;

import java.util.Scanner;

public class CINEMA {
        // قائمة السينمات المتاحة
    private String[] cinemas = {"سينما 1", "سينما 2", "سينما 3"};
    private String selectedCinema;

    // دالة لاختيار السينما
    public void chooseCinema() {
        System.out.println("اختر السينما:");
        for (int i = 0; i < cinemas.length; i++) {
            System.out.println((i + 1) + ". " + cinemas[i]);
        }

        Scanner scanner = new Scanner(System.in);
        int choice = scanner.nextInt();  // المستخدم يختار السينما
        selectedCinema = cinemas[choice - 1];  // تخزين السينما المختارة
        System.out.println("لقد اخترت " + selectedCinema);
    }

    // دالة لاسترجاع السينما المختارة
    public String getSelectedCinema() {
        return selectedCinema;
    }

}
