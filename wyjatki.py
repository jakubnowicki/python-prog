lista = []

try:
    #assert False
    # lista[0]
    a = 1 / 0
#except: <-- łap wszystkie błędy - zła praktyka
#except Exception: --//--
except ZeroDivisionError:
    print("Dzielono przez zero, ale idziemy dalej")
    a = 0
except IndexError as e:
    print("Pojwił się błąd indeksowania:", e)
    a = None
else:  # kiedy nie ma żadnego wyjątu
    print("Wszystko ok, nie ma co się zatrzymywać, idziemy dalej")
finally:
    print("Zamykamy pliki itp.")

print(a)

print("Reszta programu")

# ----- rzucanie błędów

def _czas_przejazdu(odleglosc):
    if odleglosc < 0:
        raise ValueError("Odległość nie może być mniejsza od zera")
    czas = 1 / (24.5 / odleglosc)
    return czas

def czas_przejazdu(odleglosc):
    try:
        _czas_przejazdu(odleglosc)
    except ValueError as e:
        print("Nie można policzyć czasu przejazdu ponieważ:", e)
    except ZeroDivisionError:
        print("O, dzielenie przez zero! tego nie oczekiwaliśmy")
        raise  # <-- ponowne rzucenie wyjątku który złapaliśmy
    finally:
        print("Zdziałało finally")

czas_przejazdu(-1)
czas_przejazdu(0)
