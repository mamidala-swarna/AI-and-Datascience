class Payment:
    def pay(self):
        print("Genric Payment")
class CreditCardPayment(Payment):
    def pay(self,credit_card_number,credit_card_cvv):
        print("Credit Card Payment Selected")
class NetBankingPayment(Payment):
    def pay(self,user_id,password):
        print("Net Banking Payment Selected")
class UPIPayment(Payment):
    def pay(self,vpa,qr_code):
        print("UPI Payment Selected")