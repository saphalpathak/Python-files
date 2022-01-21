class Train:
    def __init__(self,no_of_seats):
        print("*****Welcome to Indian Railway*****")
        self.no_of_seats = no_of_seats
    def book(self):
        number = int(input("Enter a number of seats you want to book: "))
        self.no_of_seats = no_of_seats - number
        print(self.no_of_seats)


booking = Train(100)
booking.book()
        