for i in [1, 2, 3, 4, 5, 6]:
    if i == 1:
        print("Witaj")
    elif i % 2:  # rzutowanie na bool - tylko 0 na False
        print("Hej! " + str(i))
    else:
        print("Hop! " + str(i))