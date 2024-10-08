import time

balance = 1000  # Initial balance
password = 1234  # pincode
print()
print(""" ------------------------------WELCOME-------------------------------- """)
print()
print("    Please insert Your ATM card")
time.sleep(3)
pin = int(input("    Please enter your pin code : "))
if pin == password:
    while 1:
        print()
        print(
            "    Choices Are : ",
            """  Withdraw ----> 1
                    Deposit  ----> 2
                    Balance  ----> 3
                    Exit     ----> 4
        """,
            sep="",
        )
        choice = int(input("    Please enter a valid choice( Digit ) : "))

        if choice == 1:  # withdraw
            print()
            amt = int(input("    Please enter the amount to withdraw : "))
            if amt > balance:
                print()
                print("    Insufficient funds... Please check your balance !")
            else:
                balance = balance - amt
                print()
                print(f"    Successfully withdrawn {amt} from your balance!")
        elif choice == 2:  # deposit
            print()
            amt = int(input("    Enter the amount to deposit : "))
            balance = balance + amt
            print()
            print(f"    Successfully Deposited {amt} to your balance !")
        elif choice == 3:  # To check balance
            print(
                """
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
         Balance is : %.4f            
        ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        """
                % (balance)
            )
        elif choice == 4:  # Exit
            print()
            print("    You had quit !")
            break
        else:  # user entered invalid choice
            print()
            print("    Please Make sure you have entered a valid choice !")
        print(
            """ ---------------------------------------------------------------------- """
        )
else:
    print("    please Enter correct pin code !")
print(""" --------------------------------END----------------------------------- """)
