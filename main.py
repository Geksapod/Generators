import generator as g


if __name__ == "__main__":
    #1
    try:
        generator = g.geom_sequence(12, 5)
        for item in generator:
            if item == 50:
                generator.close()
            print(item, end=", ")
    except TypeError as error:
        print(error)
    print()
    print("-"*40)

    #2
    try:
        for item in g.range_gen(-2, 19, 2):
            print(item, end=", ")
    except (TypeError, ValueError) as error:
        print(error)
    print()
    print("-"*40)

    #3
    try:
        for number in g.prime_number(30):
            print(number, end=", ")
    except TypeError as error:
        print(error)
    print()
    print("-"*40)

    #4
    n = 10
    list_1 = [i ** 3 for i in range(2, n)]
    print(list_1)
    print("-"*40)



