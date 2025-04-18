#include <iostream>
#include <iomanip>
#include <string>
#include <cstdlib>
using namespace std;
void exit();
void ticket_reservation();
int main()
{
    string username;
     cout << "Please enter user name and password, please. "<< endl;
    cout << "User name, please: ";
    getline(cin , username);
    int attempts=3;
    while(attempts>0)
    {

    int password, confirmpassword;
    cout << "Password numbers, please:: ";
    cin >> password;

    cout << "Confirm password, please:: ";
    cin >> confirmpassword;
    system("cls");
        if (password==confirmpassword)
        {

            cout << "\n************************************************************"<< endl;
            cout << "\nWelcome "<< username << " in program  ticket reservation ^_^ .\n"<< endl;
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
        system("cls");
        ticket_reservation();


    return 0;
}

inline void exit()
{
    cout << "You have been exited from the program. \n"<< setw(15) << "Good bye ^_^ ."<< endl;

}
inline void ticket_reservation()
{
    for(int i=0;i<1;i++)
    {
        int type_ticket;
    double price_ticket;
    cout << "Types of tickets: \n 1. First class ticket price\" 150.0$ \". \n 2. Medium ticket (Ticket next to the window) price\" 80.0$ \". \n "
    "3. Regular ticket price\" 40.0$ \".\n\n *Choose the ticket type(1, 2, 3), please. If you want to exit, enter the number (0) : "<< endl;
    cin >> type_ticket;
    cout << endl;
    if (type_ticket==0)
    {
        exit();
        break;

    }
    switch(type_ticket)
    {
    case 0:
        break;
    case 1:
        price_ticket=150.0;
        break;
    case 2:
        price_ticket=80.0;
        break;
    case 3:
        price_ticket=40.0;
        break;

    default:
       {
            cout << "\nYou enter incorrect number.\n\n"<< setw(30) << "Good bye ^_^ .\n";
             exit();
             break;
       }
    }
    int num_seats;
    cout << "\nEnter the number of seats you wish to reserve, please. If you want to exit, enter the number (0) : \n";
    cin >> num_seats;// num_seats =seats number
    cout << endl;
    if (num_seats==0)
    {
        exit();
        break;

    }

    double amount_paid;
    double amount_required= price_ticket*num_seats;
    cout << "\nThe amount required is \" " << amount_required << " $\" .\n"
    "Enter the required amount, please. If you want to exit, enter the number (0) :\n";
    cin >> amount_paid;
    cout << endl;
    if (amount_paid==0)
    {
        exit();
        break;

    }
    double rest;
    if (amount_paid>amount_required)
    {
        rest= amount_paid-amount_required;
        cout << "\nThe amount paid is greater than the requested amount. \n The rest: \""<< rest << " $\" .\n";
    }
    else if (amount_paid==amount_required)
    {
        cout << "\nThe required amount has been paid and there is nothing left.\n";
    }
    else
    {
        int can_seats=num_seats-static_cast<int>(amount_paid/price_ticket);//cancellation of seats.
        rest=amount_paid-(num_seats -can_seats)*price_ticket;
        cout << "\nThe amount paid is less than the requested amount. \nCanceled  \""<< can_seats << " \" of seats.\nThe rest: \" "<< rest<<
        "$ \".\n"<< endl;

    }
    cout << "********************************Thank you for using the program.******************************** \n\n "<<endl;
    string answer;
    cout << "Do you want to book another ticket (yes or no)?";
    cin >> answer;
    cout << endl;
    if (answer=="Yes" || answer=="yes")
     {
        i++;
     }

    else if(answer=="No" || answer=="no")
    {
        cout << "Thank you for using the program. \n\n "<< setw(30)<< "Good bye ^_^ ."<< endl;
        break;
    }
}
}
