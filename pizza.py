"""This module provide access to Pizza, Extra, Order classes"""
import itertools


class Pizza:
    """
    This class used to represent pizza.

    Args:
        name (str): The name of the pizza.
        description (list): The list of the main ingredients of pizza topping.
        price (int): The price of the pizza.

    Attributes:
        name (str): The name of the pizza.
        description (list): The list of the main ingredients of pizza topping.
        price (int): The price of the pizza.
    """

    def __init__(self, name: str, description: list, price: int):

        self.name = name
        self.description = description
        self.price = price

    def __str__(self):

        return f"{self.name} ({', '.join(self.description)})"


class Extra:
    """
    This class used to represent extra ingredient of pizza topping.

    Args:
        name (str): The name of the extra ingredient.
        price (int): The price of the extra ingredient.

    Attributes:
        name (str): The name of the extra ingredient.
        price (int): The price of the extra ingredient.
    """

    def __init__(self, name: str, price: int):

        self.name = name
        self.price = price

    def __str__(self):

        return f"extra {self.name}"


class Order:
    """
    This class used to represent order of the pizza of the day.

    Args:
        number (str): The number of the order.
        pizza (Pizza): The pizza added to the order.
        quantity (int): The quantity of the pizza, it defaults to 1.

    Attributes:
        number (str): The number of the order.
        pizza (Pizza): The pizza added to the order.
        quantity (int): The quantity of the pizza, it defaults to 1.
    """

    def __init__(self, number: str, pizza: Pizza, quantity: int = 1):

        self.number = number
        self.pizza = pizza
        self.quantity = quantity
        self.ordered_pizza_name = self.pizza.name
        self.exta_list = []
        self.ordered_pizza_price = self.pizza.price

    def add_extra(self, extra: Extra):
        """
        Add instances of Extra class to the self.exta_list.
        Add mark "+" to the name of the ordered pizza that mean the ordered pizza contains extra ingredient(s).
        Update price of the ordered pizza adding price of the extra ingredient.
        """

        if extra in self.exta_list:
            raise ValueError(f"The {extra} has been added already")

        else:
            if "+" not in self.ordered_pizza_name:
                self.ordered_pizza_name = f"{self.ordered_pizza_name}+"
            self.exta_list.append(extra)
            self.ordered_pizza_price += extra.price

    def remove_extra(self, extra: Extra):
        """
        Remove instances of Extra class from the self.exta_list.
        If the order does not have extra ingredients, name of the ordered pizza must not have mark "+".
        Update price of the ordered pizza subtracting price of the extra ingredient.
        """

        if extra not in self.exta_list:
            raise ValueError(f"There is not {extra} in the order")

        else:
            self.exta_list.remove(extra)
            self.ordered_pizza_price -= extra.price
            if not len(self.exta_list):
                self.ordered_pizza_name.replace("+", "")

    def __extra_description_secq(self):
        """
        Return objects from the self.exta_list and apply .__str__() method.
        """

        for i in self.exta_list:
            yield str(i)

    def __str__(self):

        return f"Order No. {self.number} - {self.ordered_pizza_name} " \
               f"({', '.join(itertools.chain(self.pizza.description, self.__extra_description_secq()))}) - " \
               f"{self.quantity} pcs - {self.ordered_pizza_price * self.quantity} UAH"





