from recept import Recept
from ingredient import Ingredient
from stap import Stap


def main():
    # Recept 1
    r1 = Recept("Spaghetti met Kip", "Romige spaghetti met kipstukjes en tomatensaus.")
    r1.voeg_ingredient_toe(Ingredient("spaghetti", "100", "gram", 350))
    r1.voeg_ingredient_toe(Ingredient("kipfilet", "150", "gram", 165))
    r1.voeg_ingredient_toe(Ingredient("tomatensaus", "150", "ml", 50))
    r1.voeg_ingredient_toe(Ingredient("knoflook", "2", "teentjes", 10))
    r1.voeg_ingredient_toe(Ingredient("geraspte kaas", "2", "el", 80))
    r1.voeg_ingredient_toe(Ingredient("olijfolie", "1", "el", 120))
    r1.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes", 0))
    r1.voeg_stap_toe(Stap("Kook de spaghetti gaar in gezouten water."))
    r1.voeg_stap_toe(Stap("Snijd de kip in blokjes en kruid met zout en peper."))
    r1.voeg_stap_toe(Stap("Bak de kip in olijfolie gaar op middelhoog vuur.", "Zorg dat de pan goed heet is voor een mooie kleur."))
    r1.voeg_stap_toe(Stap("Voeg de knoflook toe en bak 1 minuut mee."))
    r1.voeg_stap_toe(Stap("Voeg de tomatensaus toe en laat 5 minuten sudderen."))
    r1.voeg_stap_toe(Stap("Schep de spaghetti door de saus en serveer met kaas."))

    # Plantaardig alternatief voor kip
    tofu = Ingredient("tofu", "150", "gram", 120)
    r1.get_ingredienten()[1].set_plantaardig_alternatief(tofu)

    # Recept 2
    r2 = Recept("Lasagna", "Klassieke ovenschotel met gehakt, tomatensaus en bechamelsaus.")
    r2.voeg_ingredient_toe(Ingredient("lasagnebladen", "4", "stuks", 140))
    r2.voeg_ingredient_toe(Ingredient("gehakt", "150", "gram", 300))
    r2.voeg_ingredient_toe(Ingredient("tomatensaus", "150", "ml", 50))
    r2.voeg_ingredient_toe(Ingredient("melk", "200", "ml", 100))
    r2.voeg_ingredient_toe(Ingredient("bloem", "1", "el", 30))
    r2.voeg_ingredient_toe(Ingredient("boter", "1", "el", 90))
    r2.voeg_ingredient_toe(Ingredient("geraspte kaas", "50", "gram", 180))
    r2.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes", 0))
    r2.voeg_stap_toe(Stap("Verwarm de oven voor op 200 graden."))
    r2.voeg_stap_toe(Stap("Bak het gehakt rul en voeg de tomatensaus toe."))
    r2.voeg_stap_toe(Stap("Maak de bechamelsaus: smelt boter, voeg bloem toe en roer melk erdoor tot een gladde saus.", "Blijf constant roeren zodat er geen klontjes ontstaan."))
    r2.voeg_stap_toe(Stap("Laag een ovenschaal in: lasagnebladen, gehaktsaus, bechamelsaus. Herhaal."))
    r2.voeg_stap_toe(Stap("Eindig met bechamelsaus en strooi de kaas erover."))
    r2.voeg_stap_toe(Stap("Bak 30 minuten in de oven tot de bovenkant goudbruin is."))

    # Plantaardig alternatief voor gehakt
    linzen = Ingredient("linzen", "150", "gram", 180)
    r2.get_ingredienten()[1].set_plantaardig_alternatief(linzen)

    # Recept 3
    r3 = Recept("Stampot met Rookworst", "Hollandse klassieker met aardappel, boerenkool en rookworst.")
    r3.voeg_ingredient_toe(Ingredient("aardappelen", "300", "gram", 250))
    r3.voeg_ingredient_toe(Ingredient("boerenkool", "100", "gram", 35))
    r3.voeg_ingredient_toe(Ingredient("rookworst", "1", "stuks", 290))
    r3.voeg_ingredient_toe(Ingredient("melk", "3", "el", 20))
    r3.voeg_ingredient_toe(Ingredient("boter", "1", "el", 90))
    r3.voeg_ingredient_toe(Ingredient("zout en peper", "2", "snufjes", 0))
    r3.voeg_stap_toe(Stap("Schil de aardappelen en kook ze gaar in gezouten water."))
    r3.voeg_stap_toe(Stap("Voeg de boerenkool de laatste 5 minuten mee toe aan het kookwater."))
    r3.voeg_stap_toe(Stap("Verwarm de rookworst in warm water volgens de verpakking.", "Laat het water niet koken, anders barst de worst."))
    r3.voeg_stap_toe(Stap("Giet de aardappelen en boerenkool af en stamp ze fijn."))
    r3.voeg_stap_toe(Stap("Voeg melk en boter toe en stamp tot een smeuige stampot."))
    r3.voeg_stap_toe(Stap("Breng op smaak met zout en peper en serveer met de rookworst."))

    # Plantaardig alternatief voor rookworst
    vegaworst = Ingredient("vegetarische rookworst", "1", "stuks", 180)
    r3.get_ingredienten()[2].set_plantaardig_alternatief(vegaworst)

    # Lijst tonen
    recepten = [r1, r2, r3]

    print("Welkom in het receptenboek!")
    print("==========================")
    nummer = 1
    for recept in recepten:
        print(str(nummer) + ". " + recept.get_naam())
        nummer += 1

    # Recept kiezen
    keuze = 0
    while keuze == 0:
        try:
            keuze = int(input("\nKies een recept: "))
            if keuze < 1 or keuze > len(recepten):
                print("Recept niet gevonden.")
                keuze = 0
        except ValueError:
            print("Foutieve invoer.")

    gekozen_recept = recepten[keuze - 1]

    # Aantal personen vragen
    personen = 0
    while personen == 0:
        try:
            personen = int(input("Voor hoeveel personen? "))
            if personen < 1:
                print("Foutieve invoer.")
                personen = 0
        except ValueError:
            print("Foutieve invoer.")

    gekozen_recept.set_aantal_personen(personen)

    # Plantaardig vragen
    plantaardig = False
    while True:
        antwoord = input("Plantaardig? (ja/nee): ").lower()
        if antwoord == "ja":
            plantaardig = True
            break
        elif antwoord == "nee":
            break
        else:
            print("Foutieve invoer.")

    gekozen_recept.get_plantaardig_recept(plantaardig)


if __name__ == "__main__":
    main()