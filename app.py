def simple_atm():
    ChuaBal = 1000.0

    print("┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓")
    print("┃           BANKING SYSTEM             ┃")
    print("┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛")

    while True:
        print(f"\n  [ CURRENT BALANCE: ${ChuaBal:,.2f} ]")
        print("  " + "━" * 34)
        print("  (1) Check Balance")
        print("  (2) Deposit Funds")
        print("  (3) Withdraw Cash")
        print("  (4) Exit System")
        print("  " + "━" * 34)

        ChuaChoice = input("  Select Option (1-4): ")

        if ChuaChoice == '1':
            print(f"\n  >> Verified Balance: ${ChuaBal:,.2f}")

        elif ChuaChoice == '2':
            try:
                ChuaAmount = float(input("  >> Deposit Amount: $"))
                if ChuaAmount > 0:
                    ChuaBal += ChuaAmount
                    print(f"  >> Deposited: ${ChuaAmount:,.2f}")
                else:
                    print("  >> [!] Invalid Amount.")
            except ValueError:
                print("  >> [!] Please enter numbers only.")

        elif ChuaChoice == '3':
            try:
                ChuaAmount = float(input("  >> Withdrawal Amount: $"))
                if ChuaAmount > 0:
                    if ChuaAmount <= ChuaBal:
                        ChuaBal -= ChuaAmount
                        print(f"  >> Withdrawn: ${ChuaAmount:,.2f}")
                    else:
                        print("  >> [!] Insufficient Funds.")
                else:
                    print("  >> [!] Invalid Amount.")
            except ValueError:
                print("  >> [!] Please enter numbers only.")

        elif ChuaChoice == '4':
            print("\n  " + "•" * 36)
            print("   Thank you for banking with us!")
            print("  " + "•" * 36 + "\n")
            break
        else:
            print("  >> [!] Invalid selection.")

if __name__ == "__main__":
    simple_atm()