
STOLICE = {"Anglia": "Londyn", "Francja": "Paryż", "Indie": "Bombaj"}

def get_capitol(country):
    if country in STOLICE:
        return STOLICE[country]
    raise Exception("Nie ma takiego panstwa jak " + country)