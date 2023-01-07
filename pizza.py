"""This module provide access to Pizza, Extra, Order classes"""
import datetime as dt
import itertools


pizza_dict = {}


class Pizza:
    """
    This class used to represent pizza.

    Attributes:
        name (str): The name of the pizza.
        description (list): The list of the main ingredients of pizza topping.
        price (int): The price of the pizza.
    """

    def __init__(self, name: str, description: list, price: int):
        """
        Initialisation of the attributes of the class Pizza.

        Args:
            name (str): The name of the pizza.
            description (list): The list of the main ingredients of pizza topping.
            price (int): The price of the pizza.
        """

        self.name = name
        self.description = description
        self.price = price

    def __str__(self):

        return f"{self.name} ({', '.join(self.description)})"


class Extra:
    """
    This class used to represent extra ingredient of pizza topping.

    Attributes:
        name (str): The name of the extra ingredient.
        price (int): The price of the extra ingredient.
    """

    def __init__(self, name: str, price: int):
        """
        Initialisation of the attributes of the class Extra.

        Args:
            name (str): The name of the extra ingredient.
            price (int): The price of the extra ingredient.
        """

        self.name = name
        self.price = price

    def __str__(self):

        return f"extra {self.name}"


class Order:
    """
    This class used to represent order of the pizza of the day.

    Attributes:
        number (str): The number of the order.
        pizza (Pizza): The pizza added to the order.
        quantity (int): The quantity of the pizza, it defaults to 1.
    """

    def __init__(self, number: str, pizza: Pizza, quantity: int = 1):
        """
        Initialisation of the attributes of the class Order.

        Args:
            number (str): The number of the order.
            pizza (Pizza): The pizza added to the order.
            quantity (int): The quantity of the pizza, it defaults to 1.
        """

        self.number = number
        self.pizza = pizza
        self.quantity = quantity
        self.ordered_pizza_name = self.pizza.name
        self.extra_list = []
        self.ordered_pizza_price = self.pizza.price

    def add_extra(self, extra: Extra):
        """
        Add instances of Extra class to the self.extra_list.
        Add mark "+" to the name of the ordered pizza that mean the ordered pizza contains extra ingredient(s).
        Update price of the ordered pizza adding price of the extra ingredient.
        """

        if extra in self.extra_list:
            raise ValueError(f"The {extra} has been added already")

        else:
            if "+" not in self.ordered_pizza_name:
                self.ordered_pizza_name = f"{self.ordered_pizza_name}+"
            self.extra_list.append(extra)
            self.ordered_pizza_price += extra.price

    def remove_extra(self, extra: Extra):
        """
        Remove instances of Extra class from the self.extra_list.
        If the order does not have extra ingredients, name of the ordered pizza must not have mark "+".
        Update price of the ordered pizza subtracting price of the extra ingredient.
        """

        if extra not in self.extra_list:
            raise ValueError(f"There is not {extra} in the order")

        else:
            self.extra_list.remove(extra)
            self.ordered_pizza_price -= extra.price
            if not len(self.extra_list):
                self.ordered_pizza_name.replace("+", "")

    def __extra_description_secq(self):
        """
        Return objects from the self.extra_list and apply .__str__() method.
        """

        for i in self.extra_list:
            yield str(i)

    def __str__(self):

        return f"Order No. {self.number} - {self.ordered_pizza_name} " \
               f"({', '.join(itertools.chain(self.pizza.description, self.__extra_description_secq()))}) - " \
               f"{self.quantity} pcs - {self.ordered_pizza_price * self.quantity} UAH"


def week_of_pizza(number: int, pizza: Pizza, pizza_dict: dict):
    """
    Update dictionary of pizza where key is number of day of the week and
    value is instance of class Pizza.
    If number less than 0 and great than 8 raises ValueError.

    Args:
        number (int): Number of the day of the week.
        pizza (Pizza): Instances of class Pizza.
        pizza_dict (dict): Dictionary where keys are numbers of the days of the week and
        values are instances of classes Pizza.
    """

    if 0 < number < 8:
        pizza_dict.update({number: pizza})
    else:
        raise ValueError("The number must be great than 0 and less than 8")


def pizza_of_the_day(pizza_dict: dict):
    """
    Return value from pizza dictionary (pizza_dict) - instance of class Pizza.
    The key of returned value is equal of number of the day of week today.

    Args:
        pizza_dict (dict): Dictionary where keys are numbers of the days of the week and
        values are instances of classes Pizza.
    """

    if len(pizza_dict) == 7:
        day_of_week_today = dt.datetime.now().isoweekday()
        return pizza_dict[day_of_week_today]
    raise ValueError("The dictionary must have 7 items.")
