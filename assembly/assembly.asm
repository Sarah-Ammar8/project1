.MODEL SMALL
.STACK 100H
.DATA
    msg1 DB 'Enter a string: $'       ; رسالة طلب إدخال النص
    msg2 DB 10, 'Converted String: $' ; رسالة النص المحوّل
    buffer DB 100 DUP('$')            ; مساحة تخزين النص المدخل

.CODE
MAIN PROC
    MOV AX, @DATA  ; تحميل عنوان البيانات إلى AX
    MOV DS, AX     ; تحميل عنوان البيانات إلى سجل DS

    ; طباعة رسالة الإدخال
    MOV DX, OFFSET msg1
    MOV AH, 09H
    INT 21H

    ; قراءة النص من المستخدم
    MOV DX, OFFSET buffer  ; تحميل عنوان التخزين
    MOV AH, 0AH            ; مقاطعة قراءة سلسلة نصية
    INT 21H

    ; تحويل الأحرف الصغيرة إلى كبيرة
    MOV SI, OFFSET buffer+2  ; تجاوز أول بايتين (حجم الإدخال وأقصى حجم)
CONVERT:
    MOV AL, [SI]             ; تحميل الحرف الحالي
    CMP AL, 0DH              ; هل هو مفتاح الإدخال (Enter)؟
    JE PRINT_RESULT           ; إذا نعم، انتهى الإدخال

    CMP AL, 'a'              ; هل الحرف أصغر من 'a'؟
    JL NEXT_CHAR             ; إذا نعم، انتقل إلى الحرف التالي
    CMP AL, 'z'              ; هل الحرف أكبر من 'z'؟
    JG NEXT_CHAR             ; إذا نعم، انتقل إلى الحرف التالي

    SUB AL, 32               ; تحويله إلى حرف كبير
    MOV [SI], AL             ; تخزين الحرف المحوّل

NEXT_CHAR:
    INC SI                   ; الانتقال إلى الحرف التالي
    JMP CONVERT              ; تكرار العملية

PRINT_RESULT:
    ; طباعة رسالة النص المحوّل
    MOV DX, OFFSET msg2
    MOV AH, 09H
    INT 21H

    ; طباعة النص المحوّل
    MOV DX, OFFSET buffer+2
    MOV AH, 09H
    INT 21H

    ; إنهاء البرنامج
    MOV AH, 4CH
    INT 21H

MAIN ENDP