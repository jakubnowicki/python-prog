# import pathlib  # pathlib.Path('.')
from pathlib import Path  # Path('.')

"""
Example output:
- .
  - [katalog1]
    - [podkatalog]
      - plik
    - plik1
    - plik2
  - [katalog2]
  - plik1
  - plik2
"""

# zadanie dodatkowe 1:
#  [katalog]
#   |- plik
#   |- plik

# zadanie dodatkowe 2:
#  [katalog]
#   |- plik
#   '- plik

SEP = "  "


def print_tree(path, depth=0):
    for p in path.iterdir():
        if p.is_dir():
            print(SEP * depth + "-", f"[{p.name}]")
            print_tree(p, depth + 1)
        else:
            print(SEP * depth + "-", p.name)


def main():
    print_tree(Path("."))


if __name__ == "__main__":
    main()
