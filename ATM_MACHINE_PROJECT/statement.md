# ATM MACHINE SYSTEM 

## PROBLEM STATEMENT
This is a python based ATM Machine project that works throuth the terminal. It allows a user tp creat an account , sign in using an account number and ATM PIN , check the balance , and exit the system.

## Features 
The project proviedes the following features.

1. Creat an ATM account 
2. Sign in using account number and ATM PIN 
3. Deposite money 
4. Withdraw money 
5. Add moblie number 
6. Add Gmail ID 
7. Change PIN 
8. Check current bank balance 
9. Print statement receipt opotion 
10. Exite from ATM
11. Return to the main menu

## Main menu 
When the program starts, it Shows three option 
1. creat an account 
2. sign in 
3. exite the system 

### creat an account 
The user can create an account by entering:
Account number and ATM pin 

### sign in 
If an account has already been created , the user can sign in using:
Account number 
ATM PIN 

### Exite 

## ATM MENU 
After creating an account or sighning in ,the ATM menu provides these these option. 

1. YOU WANT TO MAKE DEPOSITE
2. YOU WANT TO WITHDRAW MONEY 
3. YOU MAKE TO TO ADD MOBLILE NO.
4. YOU WANT TO ADD GMAIL ID 
5. YOU WANT TO CHANGE THE PIN 
6. YOU WANT TO CHECK BANK BALANCE 
7. YOU WANT TO PRINT THE STATEMENT RECEIPT 
8. EXITE THE STSTEM AND ENTER IN MAIN MENU 

## Funtion Used 
The project mainly uses two factions. 
recall()

This function controls the main ATM menu 
It handles:
~ account creation 
~ Sign in 
~ Account verification 
~ Exite from the system 
~ Calling the ATM menu 

mf()
This funtions controls the main ATM operstions after login .

It handle :
~ Deposite 
~ Withdraw 
~ Moblie number 
~ Gmail ID 
~ PIN change 
~ Balance checking 
~ Statement option 
~ Returning to ther main menu 

## IMPORTANT VARIABLES 

The project uses some global vairiable to store account information 

CURRENT_AMOUNT = 0.0
ACCOUNT_CREATED = False
MOBILE_NO = none 
ADD_GMAIL = none


## Python concepts used 
This project was created using basic Python concepts such as:

1. Variable 
2. Funtions
3. While loops
4. If-else statement 
5. user input using input()
6. Arthmetic opertors 
7. Function calling 
8. Boolean values 


## lIMITATIONS 
This project is basic terminal-based ATM simulation.

some features are currently simulated and aew not connected to a real banking system.

For example:
~ No real bank database is used 
~ OTP is simulated 
~ No real SMS is sent 
~ NO real Gmail is sent .


## FUTURE IMPROVEMENT 
In the future , this project can be improved by adding:
1. File handling or database storage 
2. Multiple user accounts
3. Real transaction history 
4. Real otp verficaton 
5. Better input validation 
6. money transfer 


## Conclution 
The ATM machine system project is a basic python project designed to simulate common ATM operations through the teminal.

This project helped in understanding how function , loops, conditions ,variables and user input can be combined to creat a simple real-world application 