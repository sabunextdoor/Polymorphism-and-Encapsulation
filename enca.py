class computer:
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("selling Price: ",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price

c=computer()
c.sell()

c.setmaxprice(1000)
c.sell()