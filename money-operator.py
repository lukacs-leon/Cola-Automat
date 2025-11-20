# get what currency and what coins are avaiable
# get the dictonary of what type moneys get and what have to pay
# give what is the exchange
class MoneyOperator():
    def __init__(self, avaiableCurrency, avaiableCoins):
        self.avaiableCurrency = avaiableCurrency
        self.avaiableCoins = avaiableCoins
        self.absoluteAvaiableCoins = ["$", "€", "₽", "₺", "£"]
        self.paymentNum = 0
        self.lastPayment = {"Amount": 0, "Price": 0, "Have to pay": 0, "Paid": 0, "Change": 0, "Payment Num": self.paymentNum}
        self.payments = []
        self.payments.append(self.lastPayment)

    def set_avaiableCurrency(self, availableCurrency):
        if self.check_avaiableCurrency(availableCurrency):
            self.avaiableCurrency = availableCurrency

    def get_avaiableCurrency(self):
        return self.avaiableCurrency

    def check_avaiableCurrency(self, availableCurrency):
        if type(availableCurrency) == str and availableCurrency in self.absoluteAvaiableCoins:
            return True
        else:
            return False
    

    def check_avaiableCoins(self, coins):
        if all(coins) in self.avaiableCoins:
            return True
        else:
            return False
        
    def set_avaiableCoins(self, coins):
        if self.check_avaiableCoins(coins):
            self.avaiableCoins = coins


    def get_avaiableCoins(self):
        return self.avaiableCoins
    
    def check_payment(self, payment):
        if type(payment) == dict and "Amount" in payment and "Price" in payment and "Have to pay" in payment and "Paid" in payment:
            return True
        else:
            return False
    
    def add_payment(self, payment):
        if self.check_payment(payment):
            self.paymentNum += 1
            payment["Payment Num"] = self.paymentNum
            self.payments.append(payment)
            self.lastPayment = payment
    
    def get_last_payment(self):
        return self.lastPayment
    
    def get_payments(self):
        return self.payments
    
    def get_payment_by_num(self, paymentNum):
        for payment in self.payments:
            if payment["Payment Num"] == paymentNum:
                return payment
        return None
    
    def calculate_change(self, have_to_pay, paid):
        if paid >= have_to_pay:
            return paid - have_to_pay
        else:
            return -1
    
    def count_paid(self, coins_paid):
        total_paid = 0
        for coin, quantity in coins_paid.items():
            if coin in self.avaiableCoins:
                total_paid += coin * quantity
            else:
                return -1
        return total_paid
    
    def process_payment(self, amount, price, coins_paid): # coins paid is a dictionary of coin: quantity
        have_to_pay = amount * price
        paid = self.count_paid(coins_paid)
        if paid == -1:
            return f"Invalid coins paid: {coins_paid}"
        change = self.calculate_change(have_to_pay, paid)
        if change == -1:
            return f"Insufficient payment. Have to pay: {have_to_pay}, Paid: {paid}"
        payment = {
            "Amount": amount,
            "Price": price,
            "Have to pay": have_to_pay,
            "Paid": paid,
            "Change": change,
            "Payment Num": self.paymentNum + 1
        }
        self.add_payment(payment)
        return payment
    
# Example usage:
if __name__ == "__main__":
    """
    MoneyOperator = MoneyOperator("$", [.01, .05, .10, .25, .50, 1.00])
    payment = MoneyOperator.process_payment(3, 0.75, {1.00: 1})
    print(payment)
    """
    mo = MoneyOperator("$", [.01, .05, .10, .25, .50, 1.00])
    currency = mo.get_avaiableCurrency()
    coins = mo.get_avaiableCoins()
    last_payment = mo.get_last_payment()
    pay = mo.process_payment(3, 1, {1.00: 3})
    payment_by_num1 = mo.get_payment_by_num(1)
    payment_by_num2 = mo.get_payment_by_num(0)
    test_for_check_avaiableCurrency1 = mo.check_avaiableCurrency("$")
    test_for_check_avaiableCurrency2 = mo.check_avaiableCurrency("X")
    test_for_check_avaiableCurrency3 = mo.check_avaiableCurrency(5)
    test_for_check_avaiableCoins1 = mo.check_avaiableCoins([0.25, 1])
    test_for_check_avaiableCoins2 = mo.check_avaiableCoins([10.00, 20.00])
    test_for_check_avaiableCoins3 = mo.check_avaiableCoins([5.00, 1.00])
    test_for_count_paid1 = mo.count_paid({1.0:2, .25:3})
    test_for_count_paid2 = mo.count_paid({3.00:1})
    test_for_count_paid3 = mo.count_paid({-2.00:2})
    test_for_count_paid4 = mo.count_paid({1.00:-3})
    test_for_check