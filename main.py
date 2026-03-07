from recept import Recept 
from ingredient import Ingredient
from stap import Stap

def main():

    # Recept 1
    r1 = Recept("Spaghetti met Kip", "Romige spaghetti met kipstukjes en tomatensaus.")
    r1.voeg_ingredient_toe(Ingredient("spaghetti", "100", "gram"))
    r1.voeg_ingredient_toe(Ingredient("kipfilet", "150", "gram"))
    r1.voeg_ingredient_toe(Ingredient("tomatensaus", "150", "ml"))
    r1.voeg_ingredient_toe(Ingredient("knoflook", "2", "teentjes"))
    r1.voeg_ingredient_toe(Ingredient("geraspte kaas", "2", "el"))
    r1.voeg_ingredient_toe(Ingredient("olijfolie", "1", "el"))
    r1.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes"))
    r1.voeg_stap_toe(Stap("Kook de spaghetti gaar in gezouten water."))
    r1.voeg_stap_toe(Stap("Snijd de kip in blokjes en kruid met zout en peper."))
    r1.voeg_stap_toe(Stap("Bak de kip in olijfolie gaar op middelhoog vuur."))
    r1.voeg_stap_toe(Stap("Voeg de knoflook toe en bak 1 minuut mee."))
    r1.voeg_stap_toe(Stap("Voeg de tomatensaus toe en laat 5 minuten sudderen."))
    r1.voeg_stap_toe(Stap("Schep de spaghetti door de saus en serveer met kaas."))


    recept2 = Recept("Gehakt quiche met paprika", "Een heerlijke quiche met gehakt en paprika.")

# Lijst tonen
    recepten = [r1]

    print("Welkom in het receptenboek!")
    print("==========================")
    nummer = 1
    for recept in recepten:
        print(str(nummer) + ". " + recept.naam)
        nummer += 1

    keuze = int(input("\nKies een recept: "))
    recepten[keuze - 1].toon_details()

if __name__ == "__main__":
    main()



