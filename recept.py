from ingredient import Ingredient
from stap import Stap


class Recept:
    def __init__(self, naam: str, omschrijving: str):
        self.naam = naam
        self.omschrijving = omschrijving
        self.ingredienten = []
        self.stappen = []

    def voeg_ingredient_toe(self, ingredient):
        self.ingredienten.append(ingredient)

    def voeg_stap_toe(self, stap):
        self.stappen.append(stap)

    def toon_details(self):
        print("Naam: " + self.naam)
        print("Omschrijving: " + self.omschrijving)

        print("\nIngredienten:")
        for ingredient in self.ingredienten:
            print("  - " + ingredient.hoeveelheid + " " + ingredient.eenheid + " " + ingredient.naam)

        print("\nStappen:")
        nummer = 1
        for stap in self.stappen:
            print("  " + str(nummer) + ". " + stap.beschrijving)
            nummer += 1