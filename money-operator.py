# get what currency and what coins are avaiable
# get the dictonary of what type moneys get and what have to pay
# give what is the exchange
class MoneyOperator():
    def __init__(self, avaiableCurrency, avaiableCoins):
        self.avaiableCurrency = avaiableCurrency
        self.avaiableCoins = avaiableCoins
        self.paymentNum = 0
        self.lastPayment = {"Amount": 0, "Price": 0, "Have to pay": 0, "Paid": 0, "Payment Num": self.paymentNum}
        self.payments = []
        self.payments.append(self.lastPayment)

    def set_avaiableCurrency(self):
        pass

    def get_avaiableCurrency(self):
        return self.avaiableCurrency

    def check_avaiableCurrency(self):
        if type(self.avaiableCurrency) == str:
            return True
        else:
            return False
    
    def set_avaiableCoins(self):
        pass
      