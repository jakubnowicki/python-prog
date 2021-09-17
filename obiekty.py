import random

ULICE = ["Marszałkowska", "Długa", "Krótka", "Krakowska", "Piłsudzkiego", "Bracka"]

class MojaKlasa:
    def __init__(self):
        print("Działa init!")

    def info(self):
        print(f"Jestem obiektem {self} o ID {id(self)}")

moj_obiekt = MojaKlasa()
moj_obiekt.info()

class Budynek:
    def __init__(self, nazwa, adres, wysokosc=1):
        if not isinstance(nazwa, str):
            raise ValueError("nazwa should be string")
        self.nazwa = nazwa
        self.adres = adres
        self._wysokosc = wysokosc
        self._update_typ_budynku()

    @staticmethod
    def wylosuj_adres():
        return f"{random.choice(ULICE)} {random.randint(1, 125)}"

    @classmethod
    def NowaZabka(cls):
        adres = cls.wylosuj_adres()
        return cls("Zabka", adres, 1)

    def _update_typ_budynku(self):
        if self._wysokosc > 6:
            self.typ_budynku = 'wieżowiec'
        elif self._wysokosc < 2:
            self.typ_budynku = 'bungalow'
        else:
            self.typ_budynku = 'kamienica'

    def __str__(self):
        return f"Budynek '{self.nazwa}'"

    def __repr__(self):
        if self._wysokosc:
            return f"Budynek({self.nazwa!r}, {self.adres!r}, wysokosc={self._wysokosc!r})"
        else:
            return f"Budynek({self.nazwa!r}, {self.adres!r})"

    def pokaz_na_mapie(self, service='google'):
        if service == 'google':
            base_url = "https://maps.google.com/show?address="
        elif service == 'bing':
            base_url = "https://maps.bing.com/show?address="
        else:
            raise Exception(f"Mapping service {service} not supported")
        return base_url + self.adres

    def dobuduj_pietro(self):
        self._wysokosc += 1
        self._update_typ_budynku()

    def get_wysokosc(self):
        return self._wysokosc


biuro = Budynek("Rondo Tower", "Rondo ONZ 1, Warszawa")
print(repr(biuro))
print(f"{biuro}: nazwa: {biuro.nazwa}, adres {biuro.adres!r}")
biuro.nazwa = "Rondo 2000"
print(f"{biuro}: nazwa: {biuro.nazwa}, adres {biuro.adres!r}")
#biuro._wysokosc = 4  # nie powinno się tak robić
biuro.dobuduj_pietro()
biuro.dobuduj_pietro()
biuro.dobuduj_pietro()
biuro.dobuduj_pietro()
biuro.dobuduj_pietro()
biuro.dobuduj_pietro()
print(f"{biuro}: wysokość {biuro.get_wysokosc()}, {biuro.typ_budynku}")

print(biuro.__dir__())
print(biuro.__dict__)

zabki = [Budynek.NowaZabka() for _ in range(5)]
for zabka in zabki:
    print(zabka, zabka.adres)


### dziedziczenie

class Restauracja(Budynek):
    def __init__(self, *args, menu=None, **kwargs):
        print(f"args: {args}, kwargs: {kwargs}")
        super().__init__(*args, **kwargs)
        self._menu = menu

    def get_menu(self):
        return self._menu or "Menu w budowie"

    def __str__(self):
        return "Restauracja-" + super().__str__()

restauracja = Restauracja("Kuźnia Smaku", "Pierogowa 12", menu="Pierogi, schabowy i rosół")
print(restauracja, restauracja.get_menu())


### wielodziedziczenie

class A:
    def __init__(self):
        print("init A")

class B(A):
    def __init__(self):
        print("init B")
        super().__init__()
        print("koniec initu B")

class C(A):
    def __init__(self):
        print("init C")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("init D")
        super().__init__()

d = D()
print(D.__mro__)  # przydatna ściągawka!

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

v1 = Vector(2, 3)
v2 = Vector(5, 1)
print("Dodajemy", v1, v2)
print("Dostajemy", v1 + v2)
v1 += v2  # v1 = v1 + v2
print("I to samo w zmiennej v1", v1)