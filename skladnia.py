for i in [1, 2, 3, 4, 5, 6]:
    if i == 1:
        print("Witaj")
    elif i % 2:  # rzutowanie na bool - tylko 0 na False
        print("Hej! " + str(i))
    elif i == 6:
        pass  # nic nie robi - pusty blok kodu
    else:
        print("Hop! " + str(i))

bool(0)  # False
bool(123)  # True
bool("")  # False
bool("każdy ninny string")  # True

i = 0
while i < 5:  # tutaj przeskakuje continue
    print(i)
    i += 1
    if i == 3:
        break
    if i == 1:
        continue
    # nie ma operatora i++
#po pętli - tutaj przeskakuje break

for x in [1, 2, 3]:
    for y in ["a", "b", "c"]:
        if x == 1 and y == "b":
            break  # nie wychodzi z pętli nadrzędnej
        print(x, y)

print("3 > 2 > 1:", 3 > 2 > 1)  # "łańcuszki" porównań - interpretowane jak w matematyce