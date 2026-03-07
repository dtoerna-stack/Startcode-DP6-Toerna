from ingredient import Ingredient
from stap import Stap


class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.__naam = naam
        self.__omschrijving = omschrijving
        self.__ingredienten: list[Ingredient] = []
        self.__stappen: list[Stap] = []
