#import stolice  # nie zadziała jeśli uruchamiamy main.py
#from geografia import stolice  # deprecated, ale działa
from . import stolice
#from .sopleczna import dane_statystyczne
#from ..algebra import macierze

def distance_between_capitals(country1, country2):
    cap1 = stolice.get_capitol(country1)
