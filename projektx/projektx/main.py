#!/usr/bin/env python
import powitania
import geografia.stolice
#from geografia import stolice
#from geografia.stolice import get_capitol
import geografia.odleglosci

def main():
    powitania.powitaj("User")
    print("Stolicą Anglii jest", geografia.stolice.get_capitol("Anglia"))
    print("Pomiedzy stolica Anglii i Francji jest",
          geografia.odleglosci.distance_between_capitals("Anglia", "Francja")
          )

if __name__ == '__main__':
    main()