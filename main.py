import generator as g
import statistic as s
import pizza as p
import datetime as dt
import ticket as t
import timeit
import itertools
import json


if __name__ == "__main__":

    #Task #1
    print(f"{'Task #1':-^60}")

    try:
        generator = g.geom_sequence(15, 5)
        for item in generator:
            if item == 80:
                generator.close()
            print(item, end=", ")
    except TypeError as error:
        print(error)

    print("\n")


    #Task #2
    print(f"{'Task #2':-^60}")

    try:
        for item in g.range_gen(-2, 30, 2):
            print(item, end=", ")
    except (TypeError, ValueError) as error:
        print(error)

    print("\n")


    #Task #3
    print(f"{'Task #3':-^60}")

    try:
        for number in g.prime_number(50):
            print(number, end=", ")
    except TypeError as error:
        print(error)

    print("\n")


    #Task #4
    print(f"{'Task #4':-^60}")

    n = 10
    list_1 = list(itertools.starmap(pow, [(i, 3) for i in range(2, n)]))

    stp = """
import itertools
"""
    s1 = """
n = 10
list_1 = list(itertools.starmap(pow, [(i, 3) for i in range(2, n)]))
"""

    print(list_1, " -> ", end="")
    print(timeit.timeit(stmt=s1, setup=stp, number=1000000), "c")

    s2 = """
n = 10
list_2 = list(i ** 3 for i in range(2, n))
"""

    n = 10
    list_2 = list(i ** 3 for i in range(2, n))

    print(list_2, " -> ", end="")
    print((timeit.timeit(stmt=s2, number=1000000)), "c", "\n")


    #Task #5
    print(f"{'Task #5':-^60}")

    try:
        file_to_test = "Home_task.txt"
        file_stat = s.Statistic(file_to_test)

        print(file_stat, "\n")

    except FileNotFoundError as error:
        print(error)


    #Task #6
    print(f"{'Task #6':-^60}")

    try:
        pizza_1 = p.Pizza("Pepperoni", ["Tomato sauce", "mozzarella", "pepperoni"], 260)
        pizza_2 = p.Pizza("Margherita", ["Tomato sauce", "mozzarella", "tomatoes", "provencal herbs"], 250)
        pizza_3 = p.Pizza("Hawaiian", ["Tomato sauce", "mozzarella", "chickeni", "pineapple", "tomatoes"], 250)
        pizza_4 = p.Pizza("Four cheese", ["Cream sauce", "mozzarella", "ricotta", "parmesan", "gorgonzola"], 260)
        pizza_5 = p.Pizza("Provence", ["Cream sauce", "mozzarella", "gorgonzola", "chicken", "french mustard"], 260)
        pizza_6 = p.Pizza("Vegetariana", ["Tomato sauce", "champignons", "arugula", "tomatoes",
                                          "Pesto sauce", "provencal herbs", "black olives"], 220)
        pizza_7 = p.Pizza("With porcini mushrooms", ["Cream sauce", "mozzarella", "gorgonzola", "porcini"], 260)

        extra_1 = p.Extra("mozzarella", 35)
        extra_2 = p.Extra("tomatoes", 15)
        extra_3 = p.Extra("salami", 30)
        extra_4 = p.Extra("parmesan", 35)
        extra_5 = p.Extra("champignons", 15)
        extra_6 = p.Extra("chicken fillet", 30)

        pizza_dict = {1: pizza_1, 2: pizza_2, 3: pizza_3, 4: pizza_4, 5: pizza_5, 6: pizza_6, 7: pizza_7}
        day_of_week_today = dt.datetime.now().isoweekday()
        pizza_of_the_day = pizza_dict[day_of_week_today]

        order_1 = p.Order("0001", pizza_of_the_day)
        order_1.add_extra(extra_1)
        order_1.add_extra(extra_2)
        order_1.add_extra(extra_3)
        # order_1.add_extra(extra_3)
        order_1.remove_extra(extra_3)
        # order_1.remove_extra(extra_3)
        print(order_1, "\n")

    except ValueError as error:
        print(error)


    #Task #7
    print(f"{'Task #7':-^60}")

    try:
        ticket_1 = t.Ticket("0001", 150, tick_type="Student")
        ticket_2 = t.Ticket("0002", 150)
        ticket_3 = t.Ticket("0003", 150, tick_type="Advanced")
        ticket_4 = t.Ticket("0004", 150, tick_type="Late")
        ticket_5 = t.Ticket("0005", 150, tick_type="Late")
        # ticket_6 = t.Ticket("0005", 150, tick_type="Late")

        print("List of sold tickets", "-" * 25, sep="\n")
        for ticket in t.tickets_list:
            print(ticket)

        with open("sold_tickets.json", "w") as f:
            json.dump(t.tickets_list, f, default=lambda obj: obj.__dict__)

        with open("sold_tickets.json", "r") as f:
            data = json.load(f)
            print(data)

    except (TypeError, ValueError) as error:
        print(error)











