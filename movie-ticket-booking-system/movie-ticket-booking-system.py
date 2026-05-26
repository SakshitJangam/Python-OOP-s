# Movie Ticket Booking System...
class MovieTicket:

    def __init__(self, movie_name, seat_number, price):
        self.__movie_name = movie_name
        self.__seat_number = seat_number 
        self.__price = price
        self.__status = 'available'
        self.__ticket = []

    def book_ticket(self, name, seatnum, amount):
        if self.__status == 'available':
            self.__ticket.append(name)
            self.__ticket.append(seatnum)
            self.__ticket.append(amount)
            self.__status = 'booked'
            return 'Booked Successfully..'

        else:
            return "Ticket already Booked"
            

    def cancel_ticket(self, name, seatnum, amount):
        if self.__status == 'booked':
            self.__ticket.clear()
            self.__status = 'available'
            return "Ticket Cancelled Successfully.."
            
        else:
            return "Ticket is not booked yet"

    def update_seat(self, new_seat):
        if self.__status == 'available':
            self.__seat_number = new_seat
            return 'Seat changed Succesfully...'

        else:
            return 'Seat Booked Already...'

    def get_ticket_info(self):
        return f'Ticket Info: Name: {self.__movie_name} | Seat number{self.__seat_number} | Total Amount {self.__price} '


ticket1 = MovieTicket("Avengers", "A12", 250)

print(ticket1.book_ticket("Sakshit", "A12", 250))
print(ticket1.get_ticket_info())

print(ticket1.cancel_ticket("Sakshit", "A12", 250))
print(ticket1.get_ticket_info())


ticket2 = MovieTicket("Joker", "B15", 300)

print(ticket2.book_ticket("Rohan", "B15", 300))
print(ticket2.get_ticket_info())

print(ticket2.update_seat("C10"))
print(ticket2.get_ticket_info())