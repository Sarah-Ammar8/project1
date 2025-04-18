#include <iostream>
#include <string>
#include <cstdlib>
#include <iomanip>
using namespace std;
void Exercises();
void Examples();
void Explan();
void choose();
int main()
{
    string username;
     cout << "Please enter user name and password, please. "<< endl;
    cout << "User name, please: ";
    getline(cin , username);
    int attempts=3;
    while(attempts>0)
    {

    int password, confirmpassword; // confirmpassword=confirm password
    cout << "Password numbers, please:: ";
    cin >> password;

    cout << "Confirm password, please:: ";
    cin >> confirmpassword;
    system("cls");
        if (password==confirmpassword)
        {

            cout << "\n************************************************************"<< endl;
            cout << "\nWelcome "<< username << " in program learning language C++ ^_^ .\n"<< endl;
            cout << "************************************************************\n"<< endl;
            break;

        }

       else
             {
                 attempts--;
                 cout << "The password or confirm password is not right. Try again you have "<< attempts << " attempt remaining *_* .\n\n";


             }
    }
        if (attempts==0)
        {
            cout << "You have exceeded the allowed attempts limit. You have been exited from the program. \n\n"<<setw(30)<<
            " Good bye ^_^ ."<< endl;
            return 0;
        }

        choose();

    return 0;
}


inline void Exercises()
 {
   int score=0;
   char answer1, answer2, answer3, answer4, answer5, answer6, answer7, answer8, answer9, answer10;
   cout << "*Choose the correct answer (a , b , c ,or d)::\n\n"<< "1. What is the output of the following code?\nint x=10;\ncout <<x<<endl;\n "<<
   "a) 5\n b) 22\n c) 10\n d) Random value\n";
   cin >> answer1;
   if (answer1=='c')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (c) 10.\n";
       system("cls");
       cout << "2. What is the type of the following variable?\nchar='s';\n a) Integer\n b) Character\n c) Floating-point\n d) String\n";
       cin >> answer2;
   if (answer2=='b')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (b) Character.\n";
       system("cls");
       cout << "3. What is the output of the following code?\ncout <<""Hello World!<<endl;\n "<<
   "a) Hello World!\n b) hello World!\n c) hello world.\n d) hello! \n";
   cin >> answer3;
   if (answer3=='a')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (a) Hello World!.\n";
       system("cls");
       cout << "4. Which of the following is a loop?\n a) if \n b) if-else \n c) switch \n d)  while\n";
       cin >> answer4;
        if (answer4=='d')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (d) while.\n";
       system("cls");
       cout << "5. What is the output of the following code?\nint x=6, y=10*(5+x);\ncout <<y<<endl;\n "<<
   "a) 102\n b) 50\n c) 110 \n d) 56 \n";
   cin >> answer5;
   if (answer5=='c')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (c) 110.\n";
       system("cls");
       cout << "6. What is the output of the following code?\nstring name=\"Sarah Ammar\";\ncout <<name<<endl;\n "<<
   "a) Sarah\n b) Ammar\n c) sarah ammar \n d) Sarah Ammar \n";
   cin >> answer6;
   if (answer6=='d')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (d) Sarah Ammar.\n";
       system("cls");
       cout << "7. All of the following are conditional statements except?\n "<<
   "a) if\n b) for\n c) switch \n d) if-else \n";
   cin >> answer7;
   if (answer7=='b')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (b) for.\n";
       system("cls");
       cout << "8. What is the output of the following code?\nint x=5, y=10*(5+x);\n if(x>y)\n   cout<< x;\n else\n   cout<< y;\n"<<
   " a) 100\n b) 50\n c) 5 \n d) 20 \n";
   cin >> answer8;
   if (answer8=='a')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (a) 100.\n";
       system("cls");
       cout << "9. Requires the input value for x ?\n a) cout >> x;\n b) cout << x;\n c) cin >> x; \n d) cin << x; \n";
   cin >> answer9;
   if (answer9=='c')
   {
       cout << "correct answer\n";
        ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (c) cin >> x; .\n";
       system("cls");
       cout << "10. What is the output of the following code?\nfor(int x=0;x<5;x++)\n   cout <<x<<"   "<<endl;\n "<<
   "a) 0   1   2   3   4\n b) 0   1\n c) 1   2   3   4   5 \n d) 3   4   5 \n";
   cin >> answer10;
   if (answer10=='a')
   {
       cout << "correct answer\n";
       ++score;
   }
   else
       cout << "Wrong answer. The correct answer is (a) 0   1   2   3   4.\n";
       system("cls");

       cout << "Sum of points= "<< score << "0% ."<< endl;
       if(score>=7)
        cout << "You are good ^_^."<< endl;
       else
        cout << "I device you to go back to the lesson explanation part *_*."<< endl;



 }

inline void Examples()
{
cout << "#include <iostream>\nusing namespace std;\nint main()\n{\n   int number;\n  cout << \"Hello.\"<< endl;\n "<<
        " cout << \"enter number:: \";\n  cin >> number; // number=8\n  cout <<\"The number is \"<< number;\n\n  return 0;\n}\n"<<
        "\nThe output are\n Hello\n enter number:: \n The number is 8\n"<< endl;

/* #include <iostream>
    using namespace std;

    int main()
    {
        int number;
        cout << \"Hello.\"<< endl;
        cout << "enter number:: ";
        cin >> number; // number=8
        cout <<"The number is "<< number;

        return 0;
    }*/
        cout << "-------------------------------------------"<< endl;
cout << "#include <iostream>\nusing namespace std;\nint main()\n{\n   int grade=80;\n  if(grade>=50)\n     \n   cout << \"pass\";\n "<<
        " else \n   cout << \"fail\";\n\n  return 0;\n}\n"<<
        "\nThe output is\n pass\n"<< endl;
/* #include <iostream>
    using namespace std;

    int main()
    {
        int grade=80;
        if(grade>=50)
           cout << "pass";
        else
           cout << "fail";

        return 0;
    }*/
        cout << "-------------------------------------------"<< endl;
cout << "#include <iostream>\nusing namespace std;\nint main()\n{\n   for(int x=0;x<20;x++)\n cout << \"   \"<< x;\n"<<
        "\n  return 0;\n}\n"<<
        "\nThe output are\n 0   1   2   3   4   5   6   7   8   9   10   11   12   13   14   15    16   17   18   19\n"<< endl;
/* #include <iostream>
    using namespace std;

    int main()
    {
         for(int x=0;x<20;x++)
            cout << "   "<< x;

              return 0;
    }*/
        cout << "-------------------------------------------"<< endl;
cout << "#include <iostream>\nusing namespace std;\nint sum2();\nvoid sum1()\n{\n   int x=5,y=9;\n   cout << x+y<< endl;\n}\n\nint main()\n{\n "<<
        "  sum1();\n cout << sum2()<<endl;\n\n  return 0;\n}\nint sum2()\n{\n   int x=5,y=9;\n\n   return x+y;\n}\n"<<
        "\nThe output are\n 14\n14\n"<< endl;
/* #include <iostream>
    using namespace std;
    int sum2();
    void sum1()
    {
       int x=5,y=9;
          cout << x+y<< endl;
    }
    int main()
    {
         sum1();
         cout << sum2()<<endl;

              return 0;
    }
    int sum2()
    {
       int x=5,y=9;
         return x+y;
    } */
    cout << "-------------------------------------------"<< endl;
cout << "#include <iostream>\nusing namespace std;\nint main()\n{\n   int array_[4]={4,6,8,3};\n "<<
        "cout <<array_[0]<< \"  \"<<array_[1]<< "  "<<array_[2]<< "  "<<array_[3];\n\n  return 0;\n}\n"<<
        "\nThe output are\n 4  6  8  3\n"<< endl;
/* #include <iostream>
    using namespace std;

    int main()
    {
        int array_[4]={4,6,8,3};
        cout <<array_[0]<< "  "<<array_[1]<< "  "<<array_[2]<< "  "<<array_[3];
              return 0;
    }*/
}
inline void Explan()
{
    string examples,explanation;
    int number;
    cout << "Choose what you want from these topics:: \n 1. Introduction to C++ language.\n 2. Basic concepts.\n "<<
    "3. Data input and output.\n 4. Control structures of selection.\n 5. Loops.\n 6. Functions.\n 7. Arrays.\n "<<
    " Choose the option number::  ";
    cin >> number;
    cout << endl;
    switch(number)
    {
case 1:

    cout << " C++ is a high_level programming language that is widely used in software development.It is considered one of the language "<<
    "derived from the C language, originally developed by \"Bjarne Stroustrup\" in 1983.\n\n C++ is known for being a versatile and very powerful "
    <<"programming language. It can be used in the development of a wide range of applications such as desktop software, web application, "<<
    "games, system application, artificial intelligence, and more.\n\n In conclusion, C++ is a powerful and widely used programming language "
    << "that can be used in the development of a variety of applications. Learning it requires patience and regular practice, but it is worth"<<
    " the effort due to the benefits it provides in software development."<< endl;
    break;
case 2:
    cout << "The rules of the C++ language include a set of concepts and basic rules that must be followed when writing source code. "<<
    "Here are some important rules in C++:\n\n 1. Program start: The program must have a *main()* function, which serves as the entry point."
    <<" The commands inside the *main()* function are executed when the program starts.\n 2. Source Code: The source code is written in text "
    << "files using a suitable text editor. The file should be saved with the extension \".cpp.\" \n 3. Comments: Comments can be added in "
    << "the source code to explain the code and make it more understandable. Comments are ignored during program execution. \"//\" can be "<<
    "used for single_line comments, and \"/* */\" for multi_line comments.\n 4. Variable: Variable must be defined before they are used. " <<
    "Initial values can be assigned to variables during their definition or at a later time.\n 5. Primitive Types: C++ provides a range of "
    << "primitive types such as (int, float, double, char, bool) and others. The type of variables must be specified when they are defined."
    << "\n 6. Constants: Constants can be defined using the \"const\" keyword. Constants are values that cannot be changed during program "<<
    "execution.\n 7. Arithmetic Operations: Basic arithmetic operations such as addition (+), subtraction (-), multiplication (*), and division"
    <<" (/) can be used in C++. Other operations like remainder (%) and increment (++) and decrement (--) are also available.\n 8. Conditional "
    << "Statement: Conditional statement such as (if, else and switch) can be used to make decisions based on variable values or specific cases."
    << "\n 9. Loops: Iteration loops such as (for, while, and do-while) can be used to repeatedly execute a set of commands until a certain "<<
    "condition is met.\n 10. Functions: Functions can be defined to execute a set of commands. Functions can be called from within the *main()* "
    <<"function or from other functions."<< "\n\n These are some basic rules in the C++ language, and there may be other rules depending on "<<
    "the context and application."<< endl;
    break;

case 3:
    {
        cout << "In C++, you can perform data input and output using the input/output streams provided by the standard library. The main stream "<<
    "objects used for input and output are \"cout\" and \"cin\", respectively.\n\n Data output: To display output on the console, you can use "
    << "the \"cout\" object, which is associated with the standard output stream. You can use the \"<<\" operator to insert values from the output."<<
    "\n\n Data input: To get input from the user, you can use the \"cin\" object, which is associated with the standard input stream.You can use the "
    <<"\">>\" operator to insert values from the output.\n\n Remember to include the \"<iostream>\" header at the beginning of your program to use "<<
    "input/output streams in C++."<< endl;
     cout << "Do you want examples:";
    cin >> examples;
    if (examples=="Yes" || examples== "yes")
        {
            cout << "\n#include <iostream>\nusing namespace std;\nint main()\n{\n   int number;\n  cout << \"Hello.\"<< endl;\n "<<
            " cout << \"enter number:: \"\n  cin >> number; // number=8\n  cout <<\"The number is \"<< number;\n\n  return 0;\n}\n"<<
            "\nThe output are\n Hello\n enter number:: \n The number is 8"<< endl;

        }
        system("cls");
    break;
    }
case 4:
   {
       cout << "In the C++ language, conditional statements are used to make decisions based on specific values. Here are some common conditional"
    << " statements in C++: \n\n 1. if statement: It is used to execute a specific code if a certain condition is met.\n 2. if-else statement: "
    << "It is used to execute a specific code if a certain condition is met, or execute a different code if the condition is not met.\n 3. " <<
    "Nested if statement: It is used to include conditional statements within each other.\n 4. switch statement: It is used to execute different"
    << " code based on the specific value of a variable.\n\n These are some basic conditional statements in C++. You can use them to add control "
    << "logic to your programs and execute appropriate conditions and decisions based on the desired situation."<< endl;
    cout << "Do you want examples:";
    cin >> examples;
    if (examples=="Yes" || examples== "yes")
        {
            cout << "\n#include <iostream>\nusing namespace std;\nint main()\n{\n   int grade=80;\n  if(grade>=50)\n     {\n   cout << \"pass\";\n "
            <<" else (grade<50)\n  cout << \"fail\";\n\n  return 0;\n}\n"<<
            "\nThe output is\n pass"<< endl;
            system("cls");
        }
    break;
    }
case 5:
    {
        cout << "In the C++ language, loops are used to repeatedly execute a piece of code until a certain condition is met. There are three "
    << "main types of loops in C++: \n\n 1. \"for\" loop: It is used to execute a specific code a certain number of times. The loop "
    << "specifies the starting value, the continuation condition, and the step that changes in each iteration.\n 2. \"while\" loop: It "<<
    " is used to execute a specific code as long as a certain condition is true. The condition is checked before each iteration, and if "<<
    "it evaluates to true, the code is executed.\n 3. \"do-while\" loop: It is used to execute a specific code as long as a certain condition "<<
    "is true, but it ensures that the code is executed at least once. The condition is checked at the end of each iteration.\n\n Loops in C++ "<<
    "can be used to execute a specific code repeatedly based on certain condition. They are commonly used to process a set of data or repeat "
    << "actions until a specific criterion is met. The condition and control of loop repetition are determined based on the program's needs and "
    "desired situation."<<endl;
       cout << "Do you want examples:";
    cin >> examples;
    if (examples=="Yes" || examples== "yes")
        {
            cout << "\n#include <iostream>\nusing namespace std;\nint main()\n{\n   for(int x=0;x<20;x++)\n{\n cout << "   "<< x;\n}\n"<<
            "\n  return 0;\n}\n"<<
            "\nThe output are\n 0   1   2   3   4   5   6   7   8   9   10   11   12   13   14   15    16   17   18   19"<< endl;
            system("cls");
        }
    break;
    }
case 6:
  {
       cout << "In the C++ language, functions are used to organize code and break it down into smaller, reusable units.Functions execute a "<<
    "set of instructions when called from within the program. There are several important points related to functions in C++:\n\n 1. Function "
    << "Definition: A function is defined by specifying the return type (if it returns a value), the function name, and the parameter list (if "
    << "any).\n 2. Function Call: A function is called by mentioning its name with parentheses. The return value of the function can be stored "
    << "in a variable if the function returns a value.\n 3. Parameters: Functions can receive parameters to pass values to them. The type and "
    << "name of each parameter are specified in the function definition, and the corresponding values are passed when calling the function \n "
    << "4. Return Value: Functions can return a value of the specified type in their definition using the \"return\" statement. \"return\" is "
    << "used to return a value and terminate the execution of the function.\n\nFunctions in C++ are used to organize code, achieve reusability,"
    << " and simplify programs. You can define your own functions and call them according to your program's needs."<< endl;
    cout << "Do you want examples:";
    cin >> examples;
    if (examples=="Yes" || examples== "yes")
        {
            cout << "\n#include <iostream>\nusing namespace std;\nint sum2();\nvoid sum1()\n{\n   int x=5,y=9;\n   cout<< x+y<< endl;;\n}\n\nint main()\n{\n "<<
            "  sum1();\n  cout << sum2()<<endl;\n\n  return 0;\n}\nint sum2()\n{\n   int x=5,y=9;\n\n   return x+y;\n}\n"<<
            "\nThe output are\n 14\n14"<< endl;

        }
        system("cls");
    break;
  }
case 7:
   {
        cout<<"Array Definition: An array is defined by specifying the type of the elements it contains and the name of the array. The size of the "<<
    "array can be specified during the definition or later using constants or variable.\n 2. Accessing Array Elements: Array element are accessed "
    << "using pointers and the element index. Array indices start from zero, where the first element in the array is considered to have an index "
    << "of zero. Array elements can be accessed using the \"[]\" operator.\n 3. Array Size: The size of an array can be determined using the (sizeof)"
    << " expression, which specifies the size of the array in bytes.\n 4. Passing Arrays to Functions: Arrays can be passed as a parameters to "<<
    "functions. When an array is passed as a parameter, the pointer to the first element in the array is passed.\n\nArrays are used in C++ too store "
    << "and manage collections of values in an organized and efficient manner. You can access array elements, determine their size, and pass them to "
    <<"functions." << endl;
    cout << "Do you want examples:";
    cin >> examples;
    if (examples=="Yes" || examples== "yes")
        {
            cout << "\n#include <iostream>\nusing namespace std;\nint main()\n{\n   int array_[4]={4,6,8,3};\n "<<
            "cout <<array_[0]<< "  "<<array_[1]<< "  "<<array_[2]<< "  "<<array_[3];\n\n  return 0;\n}\n"<<
            "\nThe output are\n 4  6  8  3"<< endl;

        }
        break;
   }

default:
    cout << "You enter incorrect number."<< endl;break;
    }
           cout << "\nDo you want:\n 1. Explanation of another topic.\n 2. Go to the exercises.\n "<<
           "3. Exit the program.\n Choose the option number:: ";
           cin >>number;
           system("cls");
           switch(number)
           {
    case 1:
    Explan();
    break;
    case 2:
    Exercises();
    break;
    case 3:
    cout << "Good bye."<< endl;
    break;
    default:
        cout << "You enter incorrect number."<< endl;
        break;

           }

    }

inline void choose()
{
    int number;
    cout << "Choose what you want from the following topics: \n" << "1. Explanation of language topics.\n" <<
    "2. Examples.\n" <<"3. Exercises.\n"<< "4. Exit the program.\n"<<"\n*Choose the option number:: ";
    cin >> number;
    system("cls");
    switch(number)
    {
    case 1:
    Explan();
    break;
    case 2:
    Examples();
    break;
    case 3:
    Exercises();
    break;
    case 4:
    cout << "Good bye ^_^."<< endl;
    break;
    default:
       {
           cout << "You enter incorrect number."<< endl;
        cout << "Good bye ^_^ ."<< endl;
       }
        break;
    }
}
