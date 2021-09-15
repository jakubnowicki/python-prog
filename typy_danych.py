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

print("=== int ===")
assert bool(0) == False
assert int("123") == 123

print("=== list ===")
print([1, 2, 3, True, "string", [1, 2]])
print([1, 2] + [3])
print(["a", "b"] * 6)
a = [1, 2, 3, 4, 5, 6]
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
