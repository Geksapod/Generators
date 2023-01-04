"""This module provide access to Ticket class"""


discount_dict = {"Regular": 0, "Late": 10, "Student": 50, "Advanced": 60}
tickets_list = []


class Ticket:
    """
    This class used to represent ticket to IT-events.

    Args:
        number (str): The number of the ticket.
        price (int): The price of the ticket.
        tick_type (str): The type of the ticket.
        There are only four types of tickets: "Regular", "Late", "Student", "Advanced".
        Advance - discount 40% of the regular ticket price.
        Student - discount 50% of the regular ticket price.
        Late - additional 10% to the regular ticket price.

    Attributes:
        number (str): The number of the ticket.
        price (int): The price of the ticket.
        tick_type (str): The type of the ticket.
        discount (int): Percentage of the discount.
    """


    def __init__(self, number: str, price: int, tick_type: str="Regular"):

        if not len(tickets_list):
            tickets_list.append(self)
        else:
            for ticket in tickets_list:
                if number in ticket.__dict__.values():
                    raise ValueError(f"The ticket No.{number} has been sold already")
            else:
                tickets_list.append(self)

        if not isinstance(tick_type, str):
            raise TypeError("The ticket type must be the string type of data")

        if tick_type not in discount_dict.keys():
            raise ValueError("The type of ticket must correspond to one of the available types: "
                             "\"Regular\", \"Late\", \"Student\", \"Advanced\".")

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