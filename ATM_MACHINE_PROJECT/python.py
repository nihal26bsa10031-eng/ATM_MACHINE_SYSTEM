
CURRENT_AMOUNT = 0.0
ACCOUNT_CREATED = False
MOBILE_NO = None
ADD_GMAIL = None


# !! MAIN MENU OF ATM FOR CREATE OR SIGN IN ACCOUNT !!
# I USED recall() FUNCTION FOR MAIN MENU SETUP !!
def recall():
    global ACCOUNT_CREATED , A_C , ATM_PIN
    
    while True :
        print("$$$$$$$$$$$$$$$$$$$$$$$$$$¥¥¥ W E L C O M E  T O  NEW  A T M  M A C H I N E  $$$$$$$$$$$$$$$$$$$$$$$$$$$$")
        print("  ")
        print("======================")
        print("1. CREATE AN ACCOUNT")
        print("2. SIGN IN ")
        print("3.EXIT THE SYSTEM")
        print("======================")
        print("  ")

        N = int(input("Enter a number :    "))
        if N == 1 :
         print("--------------------------------------------------")
         print("YOU CHOOSE NUMBER 1.")
         print("--------------------------------------------------")
         print("  ")
         print("ENTER  YOUR A_C NUMBER")
         A_C=int(input("Enter YOUR A_C number :   ")) 
         print("  ")
         print("ENTER YOUR ATM PIN")
         ATM_PIN=(int(input("Enter YOUR ATM pin :      ")))
         print("  ")
         ACCOUNT_CREATED = True
         print("--------------------------------------------------")
         print("Your A/C number is",A_C )
         print("  ")
         print("Your ATM pin is",ATM_PIN)
         print("--------------------------------------------------")
         print("  ")
         print("CURRENT AMOUNT_ :  ",CURRENT_AMOUNT)
         
         print("----------------YOU CREATED AN ACCOUNT SUCCESFULLY , C O N G R A T U  L A T I O N S--------------------")
         print("Would you like to continue with ATM or not(y/n)")
         print("  ")
         x  = input("Enter your choice :        ")
         if x =="n":
          recall()
         elif x =="y":
# WE CALL mf() FUNCTION AFTER THE MAIN MENU FOR THE SECOND MENU !!
           mf()
       
        elif N == 2:
            if ACCOUNT_CREATED == False :
                 print("--------------------------------------------------------------------")
                 print("PLEASE CREATE AN ACCOUNT FIRST")
                 print("--------------------------------------------------------------------")
                 print("  ")
                 print("YOU CANNOT SIGN IN WITHOUT AN ACCOUNT")
                 recall()
            else:
                 print("--------------------------------------------------")
                 print("YOU CHOOSE NUMBER 2.")
                 print("--------------------------------------------------")
                 A_C_no=int(input("Enter your ACCOUNT NUMBER :  "))
                 P_I_N = int(input("Enter your ATM PIN number :  "))
           
                 if A_C == A_C_no and ATM_PIN == P_I_N:
                     print("----------------------------------------") 
                     print("!! ACCESS GRANTED !!")
                     print("----------------------------------------") 
                     print("  ")
                     print("----------------------------------------") 
                     print("!! LOGIN SUCCESFUL !!")
                     print("----------------------------------------") 
                     mf()
                
                 else :                    
                     print("----------------------------------------") 
                     print("!! ACCESS DENIED !!")
                     print("----------------------------------------") 
                     print("  ")
                     print("===========================================")
                     print("you enter wrong ACCOUNT NUMBER OR PIN number")
                     print("===========================================")
                     print("  ")
                     print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")  
                    
        elif N == 3:
               print("========================= YOU ARE SUCCESFULLY EXIT , BYE =========================== ")
               print("")
               print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")
               break 
              
        else :
            print("!! YOU CHOOSE INVALID OPTION !!")  
            print("  ") 
            print("PLEASE ENTER 1 , 2 , OR , 3.")
# I USED mf() FUNCTION FOR THE FURTHER MENU SETUP AFTER MAIN MENU !!
def mf():
      # INTERNAL SYSTEM AFTER PRESSING 1 OR 2 !
       global CURRENT_AMOUNT , ATM_PIN , MOBILE_NO , ADD_GMAIL
       while True :
        print("======================================")
        print("1. YOU WANT TO MAKE DEPOSIT")
        print("  ")
        print("2.YOU WANT TO WITHDRAW MONEY.")
        print("  ")
        print("3.YOU WANT TO ADD MOBILE NO.")
        print("  ")
        print("4. YOU WANT TO ADD GMAIL ID")
        print("  ")
        print("5  YOU WANT TO CHANGE THE PIN")
        print("  ")
        print("6. YOU WANT TO CHECK BANK BALANCE")
        print("  ")
        print("7. YOU WANT TO PRINT THE STATEMENT RECEIPT")
        print("  ")
        print("8. EXIT THE SYSTEM AND ENTER IN MAIN MENU")
        print("  ")
        print("========================================")
        print("  ")
        O = input("CHOOSE FROM ABOVE OPTION :  ")
# AFTER PRESSING 1 DEPOSIT SYSTEM WORK !!
        if O == "1":
            print("--------------------------------------------------")
            print("you choose number 1.")
            print("--------------------------------------------------")
            print("  ")
            DEPOSIT=int(input("ENTER MONEY TO DEPOSIT :  "))
            if DEPOSIT <=0:
                print("---------------------------------------------------------------")
                print("PLEASE ENTER A VALID AMOUNT")
                print("---------------------------------------------------------------")
            else :  
                print("-------------------------------------------------------------------------------------------")
                print("DROP YOUR MONEY IN THE FRONT CHECK BOX")
                print("--------------------------------------------------------------------------------------------")
         
                print("WAIT FOR A SECOND  ...............")
                print("  ")
                print("CONGRATULATIONS YOUR DEPOSIT AMOUNT WAS", float(DEPOSIT))
                CURRENT_AMOUNT+= DEPOSIT
                print("  ")
                print("=======================================")
                print("CURRENT_AMOUNT is :    ", CURRENT_AMOUNT)
                print("=======================================")
                print("IF YOU HAVE ANY QUERY ABOUT DEPOSIT CONTACT NO._221122")
                print("  ")
                print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")    
  
        elif O == "2" :
# IT IS FOR TO WITHDRAW MONEY FROM THE ATM !!
            print("--------------------------------------------------")
            print("YOU CHOOSE NUMBER 2.")
            print("--------------------------------------------------")
            WITHDRAW = int(input("Enter MONEY TO WITHDRAW :  "))
            if WITHDRAW <= 0 :
                print("---------------------------------------------------------------")
                print("PLEASE ENTER A VALID AMOUNT")
                print("---------------------------------------------------------------")
            elif WITHDRAW <= CURRENT_AMOUNT:
                  CURRENT_AMOUNT -= WITHDRAW
                
                  print("!! PLEASE COLLECT YOUR CASH !! ")
                  print("============================")
                  print("YOUR WITHDRAW :    " , WITHDRAW)
                  print("============================")
                  print("YOUR CURRENT BALANCE IS :     " , CURRENT_AMOUNT)
            else:
                 print("!! INSUFFICIENT BALANCE !!")
                 print("YOUR CURRENT BALANCE IS : " , CURRENT_AMOUNT)
# THIS IS FOR UPLOADING YOUR NUMBER IN YOUR ATM ACCOUNT !! 
        elif O == "3" :
             print("--------------------------------------------------")
             print("You choose number 3.")
             print("--------------------------------------------------")
             print("  ")  
             MOBILE_NO=int(input("ENTER YOUR 10 DIGIT MOBILE  NUMBER :  ")) 
             print("----------------------------------------------------------------------------") 
             print("Your New mobile number was",MOBILE_NO)
             print("----------------------------------------------------------------------------")
             print("YOU GETTING YOUR ALL BANK MESSAGES ON THIS NO. AND DON'T SHARE YOUR OTP TO ANYONE")
             print("  ")
             print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")    
  
        elif O == "4" :
# THIS IS FOR UPLOADING YOUR MAIL ID IN YOUR ATM ACCOUNT !! 
            print("--------------------------------------------------")
            print("YOU CHOOSE NUMBER 4.")
            print("--------------------------------------------------") 
            ADD_GMAIL=input("ENTER YOUR MAIL ID :  ")
            print("==========================================")
            print("YOUR NEWLY ADDED MAIL ID WAS :   ",ADD_GMAIL)
            print("=========================================")
            print("  ")
            print("YOU GETTING YOUR ALL BANK MAILS ON THIS GMAIL AND DON'T SHARE YOUR MAIL TO ANYONE")
            print("  ")
            print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")
   
        elif O == "5":
 # THIS IS FOR CHANGING YOUR ATM PIN NUMBER IN YOUR ATM ACCOUNT !!
             print("--------------------------------------------------")
             print("YOU CHOOSE NUMBER 5.")   
             print("--------------------------------------------------")
             print("  ") 
             print("=======================")
             print("1. BY ENTERING OLD PIN")
             print("------------------------------------------------")
             print("2.BY MOBILE NO. OTP")
             print("--------------------------------------------------")
             print("3.BY GMAIL OTP")
             print("---------------------------------------------------")
             print("4.EXIT")
             print("=======================")
   
             M=int(input("ENTER NUMBER TO CHANGE THE PASSWORD :  "))
             if M== 1:
                  print("-----------------------------------------------")
                  print("YOU CHOOSE NUMBER 1.")
                  print("-------------------------------------------------")
                  print("  ")
                  OLD_PIN=int(input("ENTER YOUR OLD PIN :  "))
                  if OLD_PIN == ATM_PIN :
                      print("======================Access GRANTED=========================")
                      NEW_PIN = int(input("ENTER YOUR NEW PIN"))
                      ATM_PIN=NEW_PIN
                      print(ATM_PIN)
                      print("  ")
                      print("-----------------------------------------------------------------")
                      print("!! YOUR PIN CHANGED SUCCESFULLY !!")
                      print("------------------------------------------------------------------")
                      print("  ")
                      print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")
         
                  else:
                      print("=====================")
                      print("YOU ENTER WRONG PIN !!")
                      print("=====================")
              
             elif M == 2:
                
                  print("--------------------------------------------------")
                  print("YOU CHOOSE NUMBER 2.")
                  print("--------------------------------------------------")
                  print("  ")
                  print("-------------------------------------------------------------------------------")
                  print("YOUR MOBILE NO. IS YOUR OTP for NOW ")
                  print("We will send message to you , you need to tap on YES ")
# we are supposing that the customer tap on the YES Button
                  print("-------------------------------------------------------------------------------")
                  OTP=int(input("ENTER YOUR _ DIGIT OTP"))
                  if OTP == MOBILE_NO:
                     
                      print("=====================ACCESS GRANTED =========================")
                      print("  ")
                      NEW_PIN=int(input("Enter Your New Pin :  "))
                      ATM_PIN=NEW_PIN
                      print(ATM_PIN)
                      print("!! YOUR PIN CHANGED SUCCESFULLY !!")
                      print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")
              
                  else :
                      print("========================================")
                      print("you give wrong OTP or your number was not added in the SYSTEM !! ")
                      print("========================================")
              
             elif M == 3:
                 print("----------------------------------------")
                 print("YOU CHOOSE NUMBER 3")
                 print("-----------------------------------------")
                 print("  ")
                 print("=================================================")
                 print("FOR NOW YOUR GMAIL (.......@gmail.com) WAS YOUR OTP")
                 print("we will send mail to you, ACCEPT it and the PIN will change")
                 print("=================================================")
 # We are supposing that the Customer ACCEPT it
                 OTP=(input("Enter your OTP"))
                 if OTP == ADD_GMAIL :
                    
                     print("========================ACCESS GRANTED=========================")
                     print("  ")
                     NEW_PIN=int(input("ENTER NEW PIN :  "))         
                     ATM_PIN=NEW_PIN
                     print("!! YOUR PIN CHANGED SUCCESFULY !!")
                     print("  ")
                     print("--------------------------------------T H A N K   Y O U  S I R  OR  M A M  C O M E  A G A I N -------------------------------------------")
            
                 else:
                      print("========================")
                      print("!!YOU ENTERED WRONG OTP OR YOUR GMAIL WAS NOT ADDED IN THE SYSTEM !!") 
                      print("========================")
                      
        elif  O == "6" :
#THIS SYSTEM WORK FOR CHECK YOUR ATM BALANCE !!
            print("======================")
            print("YOU CHOOSE NUMBER 6.")
            print("======================")
            print("  ")
            print("------------------------------------------------------------------------------------------")
            print("YOUR CURRENT BALANCE IS :",CURRENT_AMOUNT)
            print("------------------------------------------------------------------------------------------")
            print("==================== T H A N K Y O U  F O R  U S I N G  O U R  A T M  C O M E  A G A I N ======================")
        elif O == "7" :
# THIS SYSTEM IS WORK FOR PRINTING THE RECEIPT OF THE STATEMENT !!
             print("======================")
             print("YOU CHOOSE NUMBER 7.")
             print("======================")
             print("  ")
             print("PLEASE COLLECT YOUR RECEIPT FROM THE BELOW BOX")
             
        elif O == "8" : 
#THIS SYSTEM IS FOR  EXIT THE MENU AND ENTER IN MAIN MENU         
             print("======================")
             print("YOU CHOOSE NUMBER 8.")
             print("======================")
             print("  ")
             print("==================== T H A N K Y O U  F O R  U S I N G  O U R  A T M  C O M E  A G A I N ======================")
             break
        else:
             print("----------------------------------")
             print("!! INVALID OPTION !!")
             print("----------------------------------")
             print("  ")
             print("-----------------------------------------------------")
             print("!! PRINT ENTER VALID OPTION !!")
             print("------------------------------------------------------")
             
recall()
