class Bankomat:
    pass  # TODO

user = "Jan Kowlaski"
bankomat = Bankomat()
bankomat.uzupelnij({20: 15, 50: 5, 100: 5})
bankomat.wyplac(user, 170)  # --> {100: 1, 50: 1, 20: 1}
bankomat.wplac(user, {20: 1})
bankomat.summary() # --> str