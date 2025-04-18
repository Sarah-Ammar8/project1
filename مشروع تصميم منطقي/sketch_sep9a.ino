#define BUZZER_PIN 10

const int ledPins[]={3,5,7,9};
const int buttonPins[]={2,4,6,8};

int sequence[100]; // تخزين تسلسل العشوائي للاضائات
int inputSequence[100]; // تخزين لبتسلسل الذي سيدخله الاعب
int level=0; // بداية المستوى

void setup(){
  pinMode(BUZZER_PIN,OUTPUT); // ضبط الجرس كمخرج
  for (int i=0;i<4;i++){
    pinMode(ledPins[i], OUTPUT); // ضبط المبات كمخرجات
    pinMode(buttonPins[i],INPUT_PULLUP); // ضبط الاورار كمدخلات
  }
  randomSeed(analogRead(0)); // توليد ارفام عشوائية
}

viod loop(){
  generateSequence(); // توليد التسلسل
  playSequence(); // تشغيل التسلسل
  if (!getUserInput()){
    gameOver(); // اذا كانت المدخلات خاطئة تشغيل دالة النهاية
    rerturn;
  }
  level++; // ويادة المستوى اذا كانت المدخلات صحيحة
  delay(1000); // التاخير بين المستويات
}

void generateSequence(){
  sequence[level]=random(0,4); // توليد ارقام لاضاءة اللمبات
}

void playSequence(){
  for(int i=0;i<=level;i++){
    digitalWrite(ledPins[sequence[i]], HIGH); // تشغيل اللمبات
    delay(500); // الانتظار
    digitalWrite(ledPins[sequence[i]],LOW) // اطفاء اللمبات
    delay(250); // التاخير بين الاضاءات
  }
}

bool getUserInput(){
  for (int i=0;i<=level;i++){
    bool buttonPressed=false;
    while (!buttonPressed){ // الانتظار حتى يتم ضفط الزر
      for(int j=0;j<4;j++){
        if (digitaltalRead(buttonPins[j]==LOW)){ // التحقق من الازرار المضفوطة
          buttonPressed=true;
          inputSequence[i]=j;
          delay(250); // منع الارتداد
        if (inputSequence[i]!=sequence[i]){ // التحقق من تطابق المدخل مع التسلسل
           return false;// اذا كان المدخل خاطئ يرجع false

        }
        }
      }

    }
  }
  return true; // اذا كانت جميع المدخلات ضحيحة يرجع true
}

void gameOver(){
  for (int i=0;i<3;i++)
  {
    for (int j=0;j<4;j++){
      digitalWrite(leadPins[j],HIGH); // تشغيل جميع اللمبات
    }
    tone(BUZZER_PIN,1000,200); //اضدار ضوت عند التاخير
    delay(200); //  مدة التاخير مللي ثانية
    for (int j=0;j<4;j++){
      digitalWrite(leadPins[j],LOW); // اطفاء جميع اللمبات
    }
    delay(200);
  }
  level=0; // اعادة تعيين المستوى الى صفر
}
