
def f():
    """
    Przykładowa funkcja, drukjuje powitanie
    """
    print("Hej!")

print(f.__doc__)
assert f() is None

def odpowiedz_na_pytanie_o_wszechswiat():
    return 42
    # po return linijki się nie wykonają

assert odpowiedz_na_pytanie_o_wszechswiat() == 42

def czy_parzysta(n):
    # return not (n % 2)
    if n % 2:
        return False
    return True

def first_element(collection):
    if collection:
        return collection[0]
    #return None

def update_india(capitals):
    if "Indie" in capitals:
        capitals["Indie"] = "Mumbaj"

d = {"Anglia": "Londyn", "Francja": "Paryż", "Indie": "Bombaj"}
update_india(d)
print(d)


def get_firstname_surname():
    return "Jan", "Kowalski"  # tak naprawdę zwraca tuplę

t = get_firstname_surname()
firstname, surname = get_firstname_surname()


def policz_potege(a, b):
    c = a ** b
    return c

print(policz_potege(2, 10))
print(policz_potege(b=10, a=2))
# print(a) -- nie powstała zmienna a - to powyżej to tylko nazwanie argumentu
# print(c) -- zmienna c widoczna tylko wewnąrz funkcji policz_potege

def powitaj(imie, powitaine="Witaj", znak_ramki="*"):
    print(znak_ramki * 10)
    print(znak_ramki, powitaine, imie)
    print(znak_ramki * 10)

powitaj("Konrad")
powitaj("Marian", "Hello")
powitaj("Zbyszek", znak_ramki="#")
#powitaj("Marian", powitaine="Hello", "#") wszystkie pozycyjne muszą być przed kluczowymi
