class Product(object):
    def __init__(self, price, name, weight, brand, cost):
        self.price= price       # price changes due to taxes and status
        self.name= name
        self.weight= weight
        self.brand= brand       # Stays constant
        self.cost= cost         # Stays constant... It's how much it costs the store owner to purchase the product....
        self.status= "For Sale!"
        self.tax = 0            # tax is set by the user
    def sell(self):             # if item is sold, apply method to instance.
        self.status= "SOLD!"
        return self
    def addTax(self,tax):
        self.price = self.price * tax + self.price  # tax can be used as is because it is a parameter the user will input
        return self
    def returns(self,reason,box):   #use boolean reasoning to make code shorter
        if reason == True:
            self.status = "Defective"
            self.price = 0
        else:
            self.status = "For sale"
            if box == False:
                self.status ="Used"
                self.price = self.price - self.price * 0.20  # price * 20% off
        return self 
    
    def displayInfo(self):
        print "Price is $" + str(self.price)    # + no space. Comma inputs space
        print "Item name: " + str(self.name)
        print "Item weighs: " + str(self.weight) + "lbs"
        print "Brand: " + str(self.brand)
        print "Item Cost: $" + str(self.cost)
        print "Current Status: " + str(self.status)
product1=Product(2,"apple", 1, "fuji", 3)
product1.addTax(0.20).displayInfo()             #instance(s)