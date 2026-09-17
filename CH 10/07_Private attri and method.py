class Account:
    def __init__(self,user_name,IBAN,acc_no,acc_pin):
        self.name =user_name
        self.IBAN_no = IBAN
        self.acc_no = acc_no
        self.__acc_pin = acc_pin # Private attribute

    def __reset_pin(self,new_pin) :
        self.__acc_pin = new_pin
        return new_pin

acc1 = Account("Ayra","PK0981287345",1193,88024)
print("Account holder", acc1.name)
print("Account IBAN NO:", acc1.IBAN_no)
print("Account number :", acc1.acc_no)
# print(acc1.__acc_pin)
# print(acc1.reset_pin(112234))
