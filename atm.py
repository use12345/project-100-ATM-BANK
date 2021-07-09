
class Atm(object):
    def __init__(self,atmcardnumber,pinnumber):
        self.atmcardnumber=atmcardnumber
        self.pinnumber=pinnumber
    def CashWithdrawl(self,amount):
        newamount=50000-amount
        print("CashWithdrawl Successfully") 
        print("your balance is"+str(newamount))
    def BalanceEnquiry(self):
        print("your balance is 50000")    
    def CashDeposit(self):
        print("CashDeposit Successfully")
def main():
    atmcardnumber=input("insert your card number")
    pinnumber=input("insert your pin number")

    atm1=Atm(atmcardnumber,pinnumber)
    print(atm1.BalanceEnquiry())
    print(atm1.CashDeposit())
    print(atm1.pinnumber)
    amount=int (input("enter amount"))
    print(atm1.CashWithdrawl(amount))
if __name__=="__main__":
    main()




             