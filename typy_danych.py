print("=== str ===")
print("A" + "B")  # konkatenacja
print("*" * 5)
print(str(True), str(-123), str([1, 2, 3]))
print(repr("Cześć"), repr("True"))
print("Cześć"[1], "Cześć"[-1])
print("Cześć"[1:4])
print("Cześć"[1:40])  # nie rzuci błędu
print("Cześć, witajcie w Pythonie"[1:20:2])  # co druga litera
print("Cześć"[5:0:-1])
print("Cześć"[::-1])  # puste miejsca - całość
# str - niemutowalny
s = "Cześć"
s += "!"  # tworzymy nowy str, nie modyfikujemy poprzedniego
assert s == "Cześć!"
for litera in "Cześć":  # po str można iterować
    print(litera, end="")
print()
assert bool("") == False

assert "Cześć" == 'Cześć'
assert "litera 'a'." == 'litera \'a\'.' == """litera 'a'.""" == '''litera 'a'.'''

multiline = """linia 1
linia 2"""
multiline2 = '''linia 1
linia 2'''
multiline3 = "linia 1\nlinia 2"
if True:
    multiline4 = """linia 1
linia 2"""

assert multiline == multiline2 == multiline3 == multiline4

assert "Warszawa".startswith("War")
assert "Warszawa".endswith("awa")
assert "sza" in "Warszawa"
assert "zsa" not in "Warszawa"
assert "Warszawa".isalpha()
assert not "Warszawa123".isalpha()
assert "12312321".isdigit()

print(" <--> ".join(["ala", "kot", "pies"]))
#print(" <--> ".join(["ala", 123, True]))  - muszą być str

#Dygresja - funkcja map:

def mapuj(f, col):
    col2 = []
    for x in col:
        col2.append(f(x))
    return col2

mapuj(str, ["ala", 123, True])
print(" <--> ".join(mapuj(str, ["ala", 123, True])))
print(" <--> ".join(map(str, ["ala", 123, True])))  # już zaimplementowane i efektywne pamięciowo

# reversed - przydatne zwłaszcza dla list, tuple
print(reversed("Adam Małysz"))
for x in reversed("Adam Małysz"):
    print(x, end="")
print()
print(list(reversed("Adam Małysz")))  # przydatne żeby szybko zobaczyć zwracane elementy

assert " Litwo,   ojczyzno moja\t\t! ".split() == ["Litwo,", "ojczyzno", "moja", "!"]
assert "Litwo!! Ojczyzno moja!".split("!") == ['Litwo', '', ' Ojczyzno moja', '']
# .split(', ', 1)
# .rsplit('-', 1)

print("Cześć".encode('utf-8'))
assert "Hej".encode('utf-8') == b"Hej"
assert "Cześć".encode('utf-8').decode('utf-8') == "Cześć"


imie = "Konrad"
a = "100"
pi = 3.14159265359
print("Witaj w %s, %s po raz %d" % ("domu", "Konrad", 100))  # jeśli damy %s zamiast %d - będzie rzutowanie
print("Dostałem wartość: %r" % (a))
print("Liczba pi: %.2f" % (pi))

print("Witaj w {}, {} po raz {}".format("domu", "Konrad", 100))
print("Witaj w {1}, {0} po raz {2}".format("Konrad", "domu", 100))
print("Witaj w {miejsce}, {imie} po raz {licznik}".format(imie="Konrad", miejsce="domu", licznik=100))
print("Dostałem wartość: {!r}".format(a))
print("Liczba pi: {:.2f}".format(pi))

# f-string, od pythona 3.6
print(f"Hej, {imie.upper()}! Dostałem {a}, obliczyłem {1+1}")
print(f"Dostałem wartość: {a!r}")
print(f"Liczba pi: {pi:.2f}")

assert "WaWa".lower() == "wawa"

wawa = "Warszawa"
print(wawa.replace('a', '-!-'), wawa.replace('a', '-!-', 1), wawa.replace('rsza', ''))
assert wawa == "Warszawa"

print("=== int ===")
assert bool(0) == False
assert int("123") == 123
assert int() == 0

print("=== list ===")
print([1, 2, 3, True, "string", [1, 2]])
print([1, 2] + [3])
assert list() == []
print(["a", "b"] * 6)
a = [1, 2, 3, 4, 5, 6, ]  # na końcu opcjonalnie można dać przecinek
print(a[0], a[0:4], a[0:4:2], a[-1])  # jak w str
a = [1, 2]
a.append(3)  # jest mutowalne, możemy zmieniać zawartość
a[0] = "pierwszy"
a[1:3] = ["drugi", "trzeci"]
print(a)
assert list(range(4)) == [0, 1, 2, 3]
assert list("Hej") == ["H", "e", "j"]
assert bool([]) == False
for element in [1, 2, 3]:
    print(element, end=" ")
print()

a = [1, 2, 3]
a.pop(1)
assert a == [1, 3]

for indeks, element in enumerate([1, 2, 3]):
    print(indeks, element)

lista = [1, 2, 3]
for indeks, element in enumerate(lista[:]):  # [:] jako skrót dla .copy()
    if element % 2 == 0:
        lista.pop(indeks)
    print(element)

lista = [1, 2, 3]
lista.extend([4, 5])
assert lista == [1, 2, 3, 4, 5]
assert 1 in lista
assert 100 not in lista

lista = [1, 2, 3]
lista.insert(1, 1.5)
assert lista == [1, 1.5, 2, 3]

lista = [1, 2, 3]
lista.reverse()  # w miejscu!
assert lista == [3, 2, 1]

lista = [2, 1, 3]
lista.sort()  # w miejscu
assert lista == [1, 2, 3]


lista = ["Dom", "Samochód", "Piesek"]
lista.sort(key=len)  # w miejscu
assert lista == ["Dom", "Piesek", "Samochód"]

lista = [2, 1, 3]
for x in sorted(lista):
    print(x, end=" ")
print()
assert lista == [2, 1, 3]

print("=== tuple ===")
t = (1, 2, 3)
print(t)
t = (1,)
print(t)
assert () == tuple() == tuple([])
print(tuple("Cześć"), tuple([1, 2, 3]))
t = (1, 2, [])
lista = t[2]
t[2].append("niespodzianka!")
print(t, lista)

print("===packing, unpacking===")
t = 1, 2, 3  # packing
print(type(t), t)
a, b, c = t  # unpacking
print(a, b, c)
a, b, c = [1, 2, 3]
print(a, b, c)
a = "cośtam"
b = "coś innego"
a, b = b, a  # prosta zamiana wartość

def funkcja_3argumentowa(x, y, z):
    return x * y + z ** 2
funkcja_3argumentowa(*t)  # odpakowanie tupli do poszczególnych argumentów

d = {'promien': 2, 'wysokosc': 1.5}
def pole_figury(promien, wysokosc):
    return 3.14 * promien ** 2 * wysokosc / 3
pole_figury(**d)

print("===dict===")
d = {"Anglia": "Londyn", "Francja": "Paryż", "Indie": "Bombaj"}
assert d["Anglia"] == "Londyn"
d["Indie"] = "Mumbaj"
assert d["Indie"] == "Mumbaj"
d["Polska"] = "Warszawa"
print(d)
assert {} == dict()
print(dict([("Anglia", "Londyn"), ]))
for key in d:
    print(key, "-->", d[key])
for k, v in d.items():
    print(k, "-->", v)
#są jeszcze: d.keys(), d.values()
crazy_dict = {
    1: "asdasd",
    "asdsa": True,
    True: (1, 2, 3),
    (1, 2, 3): [1, 2, 3],
    #(1, 2, []): [1, 2, 3],
    #[1, 2, 3]: 1,
    2: {"a": 1},
    #{"a": 3}: 3,
    int: 4,
    5: str,
}

assert d["Anglia"] == d.get("Anglia")
assert d.get("Anglija", "Lądek Zdrój") == "Lądek Zdrój"

import collections
dd = collections.defaultdict(int)
print(dd["cokolwiek"])
dd["coś innego"] += 1
print(dd)

print("===None===")
a = None
print(a)
assert None is [].append(1)  # funkcja która "nic nie zwraca" zwraca None
assert bool(None) == False

print("===set===")
s = {1, 2, 3}
print(s)
assert set() != {}  # to drugie to dict
assert {"a", "b", "c"} == set(["a", "b", "c"]) == set("abc")
s.add(1)
s.add(4)
print(s)  # dodanie 1 nic nie zmieniło

s2 = {3, 4, 5, "x", "z"}
print(s | s2, s - s2, s & s2, s ^ s2)


print(" === długości ===")
assert len("Ala") == 3
assert len([]) == 0