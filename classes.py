class bankAccount():

    def __init__(self, cName, cAccountNumber, cBallance):
        self.cName = cName
        self.cAccountNumber = cAccountNumber
        self.cBallance = cBallance

    def Ballance(self):
        return self.cBallance

customer1 = bankAccount("mike", "1234567", "1234.36")
customer2 = bankAccount("jeff","3654245","65.36")
customer3 = bankAccount("Jay","4674532","12482.36")

