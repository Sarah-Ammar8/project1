
package javaapplication34;

import java.util.Scanner;

public class MOVIE {
    // قائمة الأفلام المتاحة
    private String[] movies = {"فيلم آرم", "جونغ كوك: آي آم ستيل", "فيلم آخر"};
    
    // أوقات العرض المتاحة لكل فيلم
    private String[][] showTimes = {
        {"10:00 AM", "1:00 PM", "5:00 PM"},  // أوقات عرض فيلم آرم
        {"11:00 AM", "3:00 PM", "7:00 PM"},  // أوقات عرض جونغ كوك
        {"12:00 PM", "4:00 PM", "8:00 PM"}   // أوقات عرض فيلم آخر
    };

    // الفيلم والوقت الذي اختاره المستخدم
    private String selectedMovie;
    private String selectedTime;

    // دالة لاختيار الفيلم
    public void chooseMovie() {
        System.out.println("اختر الفيلم:");
        for (int i = 0; i < movies.length; i++) {
            System.out.println((i + 1) + ". " + movies[i]);
        }

        Scanner scanner = new Scanner(System.in);
        int choice = scanner.nextInt();  // المستخدم يختار الفيلم
        selectedMovie = movies[choice - 1];  // تخزين الفيلم المختار
        System.out.println("لقد اخترت " + selectedMovie);

        // استدعاء دالة لاختيار وقت العرض بناءً على الفيلم المختار
        chooseShowTime(choice - 1);
    }

    // دالة لاختيار وقت العرض بناءً على الفيلم المختار
    private void chooseShowTime(int movieIndex) {
        // عرض أوقات العرض المتاحة للفيلم المختار
        System.out.println("اختر وقت العرض للفيلم '" + movies[movieIndex] + "':");
        for (int i = 0; i < showTimes[movieIndex].length; i++) {
            System.out.println((i + 1) + ". " + showTimes[movieIndex][i]);
        }

        Scanner scanner = new Scanner(System.in);
        int timeChoice = scanner.nextInt();  // المستخدم يختار وقت العرض
        selectedTime = showTimes[movieIndex][timeChoice - 1];  // تخزين الوقت المختار
        System.out.println("لقد اخترت وقت العرض: " + selectedTime);
    }

    // دالة للحصول على الفيلم المختار
    public String getSelectedMovie() {
        return selectedMovie;
    }

    // دالة للحصول على وقت العرض المختار
    public String getSelectedTime() {
        return selectedTime;
    }

}
