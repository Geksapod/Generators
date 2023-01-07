"""This module provide access to Ticket class"""


discount_dict = {"Regular": 0, "Late": 10, "Student": 50, "Advanced": 60}
tickets_list = []


def check_type(tick_type: str):
    """
    Raises:
        TypeError if type of the argument is not string.
        ValueError if the argument is not equal to one of the keys of the discount_dict.

    Args:
        tick_type (str): The type of the ticket.
    """

    if not isinstance(tick_type, str):
        raise TypeError("The ticket type must be the string type of data")

    if tick_type not in discount_dict.keys():
        raise ValueError("The type of ticket must correspond to one of the available types: " 
                         "\"Regular\", \"Late\", \"Student\", \"Advanced\".")


class Ticket:
    """
    This class used to represent ticket to IT-events.
    There are only four types of tickets: "Regular", "Late", "Student", "Advanced".
    Regular does not have discount.
    Advance - discount 40% of the regular ticket price.
    Student - discount 50% of the regular ticket price.
    Late - additional 10% to the regular ticket price.

    Attributes:
        number (str): The number of the ticket.
        price (int): The price of the ticket.
        tick_type (str): The type of the ticket.
        discount (int): Percentage of the discount.
    """

    def __init__(self, number: str, price: int, tick_type: str = "Regular"):
        """
        Initialisation of the attributes the class Ticket.

        Args:
            number (str): The number of the ticket.
            price (int): The price of the ticket.
            tick_type (str): The type of the ticket.
        """

        check_type(tick_type)
        add_ticket_to_list(self, number, tickets_list)
        self.number = number
        self.price = price
        self.tick_type = tick_type
        self.discount = discount_dict[self.tick_type]

    def price_ticket(self):
        """
        Return price with discount.
        """

        total_price = self.price - (self.price * self.discount / 100)
        return total_price

    def __str__(self):
        return f"Ticket No.{self.number} - {self.price_ticket()} UAH"


def add_ticket_to_list(ticket: Ticket, number: str, tickets_list: list):
    """
    Update tickets_list of instances of class Ticket if the list does not contain ticket with such number already.

    Args:
        ticket (Ticket): The instance of class Ticket.
        number (str): The number of the ticket.
        tickets_list (list): The list of the tickets.
    """

    if not len(tickets_list):
        tickets_list.append(ticket)
    else:
        for tick in tickets_list:
            if number in tick.__dict__.values():
                raise ValueError(f"The ticket No.{number} has been sold already")
        else:
            tickets_list.append(ticket)
