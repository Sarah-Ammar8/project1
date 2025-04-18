
package javaapplication34;

import java.util.Scanner;

public class USER {
    private String username;
    private String password;
    
    // دالة لإنشاء حساب جديد
    public void createAccount(Scanner scanner) {
        System.out.print("أدخل اسم المستخدم: ");
        username = scanner.next();

        // التحقق من إدخال كلمة المرور وتأكيدها
        boolean passwordConfirmed = false;
        while (!passwordConfirmed) {
            System.out.print("أدخل كلمة المرور: ");
            String enteredPassword = scanner.next();
            System.out.print("تأكيد كلمة المرور: ");
            String confirmPassword = scanner.next();
            
            if (enteredPassword.equals(confirmPassword)) {
                password = enteredPassword;
                passwordConfirmed = true;
                System.out.println("تم إنشاء حسابك بنجاح!");
            } else {
                System.out.println("كلمتا المرور غير متطابقتين. حاول مرة أخرى.");
            }
        }
    }

    // دالة لتسجيل الدخول (يمكن تحسينها لاحقًا للمصادقة)
    public boolean login(Scanner scanner) {
        System.out.print("أدخل اسم المستخدم: ");
        String enteredUsername = scanner.next();
        System.out.print("أدخل كلمة المرور: ");
        String enteredPassword = scanner.next();

        if (enteredUsername.equals(username) && enteredPassword.equals(password)) {
            System.out.println("تم تسجيل الدخول بنجاح!");
            return true;
        } else {
            System.out.println("اسم المستخدم أو كلمة المرور غير صحيحة.");
            return false;
        }
    }

    // دوال للحصول على بيانات المستخدم
    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    // دالة لتغيير كلمة المرور
    public void changePassword(Scanner scanner) {
        System.out.print("أدخل كلمة المرور الحالية: ");
        String currentPassword = scanner.next();
        
        if (currentPassword.equals(password)) {
            System.out.print("أدخل كلمة المرور الجديدة: ");
            String newPassword = scanner.next();
            System.out.print("تأكيد كلمة المرور الجديدة: ");
            String confirmPassword = scanner.next();

            if (newPassword.equals(confirmPassword)) {
                password = newPassword;
                System.out.println("تم تغيير كلمة المرور بنجاح.");
            } else {
                System.out.println("كلمتا المرور غير متطابقتين. حاول مرة أخرى.");
            }
        } else {
            System.out.println("كلمة المرور الحالية غير صحيحة.");
        }
    }

}
