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


     # Recept 2
    r2 = Recept("Lasagna", "Klassieke ovenschotel met gehakt, tomatensaus en bechamelsaus.")
    r2.voeg_ingredient_toe(Ingredient("lasagnebladen", "4", "stuks"))
    r2.voeg_ingredient_toe(Ingredient("gehakt", "150", "gram"))
    r2.voeg_ingredient_toe(Ingredient("tomatensaus", "150", "ml"))
    r2.voeg_ingredient_toe(Ingredient("melk", "200", "ml"))
    r2.voeg_ingredient_toe(Ingredient("bloem", "1", "el"))
    r2.voeg_ingredient_toe(Ingredient("boter", "1", "el"))
    r2.voeg_ingredient_toe(Ingredient("geraspte kaas", "50", "gram"))
    r2.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes"))
    r2.voeg_stap_toe(Stap("Verwarm de oven voor op 200 graden."))
    r2.voeg_stap_toe(Stap("Bak het gehakt rul en voeg de tomatensaus toe."))
    r2.voeg_stap_toe(Stap("Maak de bechamelsaus: smelt boter, voeg bloem toe en roer melk erdoor tot een gladde saus."))
    r2.voeg_stap_toe(Stap("Laag een ovenschaal in: lasagnebladen, gehaktsaus, bechamelsaus. Herhaal."))
    r2.voeg_stap_toe(Stap("Eindig met bechamelsaus en strooi de kaas erover."))
    r2.voeg_stap_toe(Stap("Bak 30 minuten in de oven tot de bovenkant goudbruin is."))

    # Recept 3
    r3 = Recept("Stampot met Rookworst", "Hollandse klassieker met aardappel, boerenkool en rookworst.")
    r3.voeg_ingredient_toe(Ingredient("aardappelen", "300", "gram"))
    r3.voeg_ingredient_toe(Ingredient("boerenkool", "100", "gram"))
    r3.voeg_ingredient_toe(Ingredient("rookworst", "1/2", "stuks"))
    r3.voeg_ingredient_toe(Ingredient("melk", "3", "el"))
    r3.voeg_ingredient_toe(Ingredient("boter", "1", "el"))
    r3.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes"))
    r3.voeg_stap_toe(Stap("Schil de aardappelen en kook ze gaar in gezouten water."))
    r3.voeg_stap_toe(Stap("Voeg de boerenkool de laatste 5 minuten mee toe aan het kookwater."))
    r3.voeg_stap_toe(Stap("Verwarm de rookworst in warm water volgens de verpakking."))
    r3.voeg_stap_toe(Stap("Giet de aardappelen en boerenkool af en stamp ze fijn."))
    r3.voeg_stap_toe(Stap("Voeg melk en boter toe en stamp tot een smeuige stampot."))
    r3.voeg_stap_toe(Stap("Breng op smaak met zout en peper en serveer met de rookworst."))

# Lijst tonen
    recepten = [r1, r2, r3]

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



