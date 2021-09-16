ALLOWED_NOTES = (20, 50, 100, 200, 500)

class Bankomat:
    def __init__(self):
        self._notes = {}

    def uzupelnij(self, notes):
        for note, amount in notes.items():
            #opcjonalnie: spr. nominał
            if note in self._notes:
                self._notes[note] += amount
            else:
                self._notes[note] = amount

    def wplac(self, user, notes):
        return self.uzupelnij(notes)

    def wyplac(self, user, requested):
        notes_draft = self._notes.copy()
        notes_to_withdraw = {}
        left_to_withdraw = requested
        while left_to_withdraw > 0:
            found_note = False
            for note, amount in sorted(notes_draft.items(), reverse=True):
                # print("Sprawdzam", note)
                if amount <= 0:
                    continue
                would_be_left = left_to_withdraw - note
                if would_be_left >= 20 or would_be_left == 0:
                    # print("Pasuje", note)
                    notes_to_withdraw[note] = notes_to_withdraw.get(note, 0) + 1
                    notes_draft[note] -= 1
                    left_to_withdraw -= note
                    found_note = True
                    break
            if not found_note:
                break

        if left_to_withdraw:
            raise Exception("Nie jesteśmy w stanie wypłacić takiej kwoty")
        else:
            # tu można odpytać bank
            self._notes = notes_draft
            return notes_to_withdraw

    def summary(self):
        return "Stan bankomatu:\n" + "\n".join(f"  {n} zł x {a}" for n, a in self._notes.items())

user = "Jan Kowlaski"
bankomat = Bankomat()
bankomat.uzupelnij({20: 15, 50: 5, 100: 5})
bankomat.wyplac(user, 100)

print(bankomat.summary())
wyplata = bankomat.wyplac(user, 170)  # --> {100: 1, 50: 1, 20: 1}
print("Wypłacono", wyplata)
assert sum(k * v for k, v in wyplata.items()) == 170
print(bankomat.summary())

bankomat.wplac(user, {20: 1})


# challange - poprawić algorytm który działa dobrze dla
# bankomat = Bankomat()
# bankomat.uzupelnij({20: 4, 50: 1})
# bankomat.wyplac(user, 60)
# bankomat.wyplac(user, 80)
