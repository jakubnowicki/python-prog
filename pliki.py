import pathlib

p = pathlib.Path("C:/Windows")
#p = pathlib.Path("C:\\Windows")
#p = pathlib.Path(r"C:\Windows")
#p = pathlib.Path(r"C:\Windows\") - backslash na końcu nie zadziała w r-string
print(p, repr(p))

print("C:/" / pathlib.Path("Windows"))

p2 = p / "system32"
print(p2, repr(p2), p2.exists(), p2.is_dir())

# print(list(map(str, p2.iterdir())))
# for path in p2.iterdir():
#     print(path)

for path in pathlib.Path('.').iterdir():
    print("  ", path)

p = pathlib.Path("C:/Users/kurs/NTUSER.DAT")
assert p.exists()
assert p.is_file()
assert not p.is_dir()
print("Rozmiar pliku:", p.stat().st_size)
print(p.parent, p.name, "==>", p.stem, p.suffix)

#Path.unlink() --> kasowanie pliku

import shutil

p = pathlib.Path("C:/Users/kurs/test.txt")

shutil.copy(p, "C:/Users/kurs/test_copy.txt")  # można Path albo str
#shutil.rmtree(...) -- usuwa cały katalog


#---------------

f = open("C:/Users/kurs/test.txt")
text = f.read()
f.close()

# to samo, ale z wbudowanym try-except

with open("C:/Users/kurs/test.txt") as f:
    text = f.read()

print("Zawartość pliku:", repr(text))

with open("C:/Users/kurs/test.txt") as f:
    for line in f:
        print("#", line.rstrip())
