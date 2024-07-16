# Train booking problem using "OOPS" concept

from random import randint
class Train:

    def __init__(self, trainNo):
        self.trainNo = trainNo

    def book(self, fro, to):
        print(f"Ticket is booked in train no: {self.trainNo} from {fro} to {to}")

    def getstatus(self):
        print(f"Train no: {self.trainNo} is running on time")

    def getfare(self, fro, to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(200, 5000)}")
    
t = Train(123334)
t.book("Bengaluru", "Chennai")
t.getstatus()
t.getfare("Bengaluru", "Chennai")