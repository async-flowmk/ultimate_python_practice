class Train:
    def __init__(self):
        pass
    def info(self,ticket,seat_no,fare_info):
        self.book_ticket = ticket
        self.get_status = seat_no
        self.get_fare = fare_info
        print(f"Book Ticket from {self.book_ticket}.\nYour seat no is {self.get_status} and price is {self.get_fare}")

passenger = Train()
passenger.info("Lahore to karachi",56,4000)