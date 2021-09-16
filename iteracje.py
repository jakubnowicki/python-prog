def range5():
    return [1, 2, 3, 4, 5]

for x in range5():
    print(x)

def range5():
    print("Podaję 1")
    yield 1
    print("Podaję 2")
    yield 2
    print("Podaję 3")
    yield 3
    yield 4
    yield 5

for x in range5():
    print("Pobrałem", x)

def infinity():
    i = 0
    while True:
        yield i
        i += 1

for x in infinity():
    print(x, end=" ")
    if x > 1000:
        break
print()

def moj_range(n):
    i = 0
    while i < n:
        yield i
        i += 1

def squared(numbers):
    for x in numbers:
        yield x ** 2

for x in squared(moj_range(5)):
    print("Squared:", x)

def censored(messages):
    """
    Example:
        From sequence "cześć", "czołem", "kurcze pieczone!", "oto sekret ...", "asdasd"
        generates: "cześć", "czołem", "*** pieczone!", "asdasd"
    """
    for msg in messages:
        if not isinstance(msg, str):  # sprawdza czy obiekt jest instancją danej klasy
            yield msg

        if "sekret" in msg:
            pass
        elif "kurcze" in msg:
            yield msg.replace("kurcze", "***")
        else:
            yield msg


msgs = ["cześć", "czołem", "kurcze pieczone!", "oto sekret ...", "asdasd"]
for x in censored(msgs):
    print("Msg: %s" % x)

# List comprehensions

g = (x**2 for x in range(5))  # to jest generator
print(g)

l = [x**2 for x in range(5)]
print(l)

t = tuple(x**2 for x in range(5))
print(t)

d = dict((x, x**2) for x in range(5))
d2 = {x: x**2 for x in range(5)}
assert d == d2
print(d)

print([x for x in range(100) if x % 7 == 0])
print(" - ".join("Hop!" for _ in range(5)))

# inne jednolinijkowce

imie = "Wacław"
print("Witaj", imie if imie else "Nieznajomy")  # Nieznajomy dla None lub ""
print("Witaj", imie or "Nieznajomy")
print("Dzień dobry", "pani" if imie.endswith("a") else "panu")  # z przeprosinami dla Kuby

def square(x):
    return x**2

square = lambda x: x**2
get_pi = lambda: 3.1415926
vector_len = lambda x, y: (x**2 + y**2)**0.5

for x in sorted(["Abb", "aaa", "Acc"], key=lambda s: s.lower()):
    print(x)

for x in range(5):
    if x == 3: continue
    pass # tu coś mądrego, co nie lubi 3

# dygresja: dekoratory

def logowana(f):  # to nie jest w pełni poprawnie zrobiony dekorator
    def wrapper(*args, **kwargs):
        print("Start działania funkcji", f.__name__)
        temp = f(*args, **kwargs)
        print("Koniec działania funkcji", f.__name__)
        return temp
    return wrapper

@logowana
def policz_cos():
    result = 0
    for x in range(1, 10000):
        result *= x
        result += 1
        result /= x
    return result
#użycie dekoratora odpowiada:
#policz_cos = logowana(policz_cos)

wazny_wynik = policz_cos()
print(wazny_wynik)