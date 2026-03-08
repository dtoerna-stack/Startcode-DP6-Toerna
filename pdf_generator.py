from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.pdfgen import canvas


def genereer_pdf(recept, plantaardig=False):
    bestandsnaam = recept.naam + ".pdf"
    c = canvas.Canvas(bestandsnaam, pagesize=A4)
    breedte, hoogte = A4
    y = hoogte - 50

    totaal_kcal = sum(
        ingredient.get_ingredient(plantaardig).get_kcal() * recept.aantal_personen
        for ingredient in recept.ingredienten
    )

    # Titel
    c.setFont("Helvetica-Bold", 22)
    c.setFillColor(colors.HexColor("#2e86ab"))
    c.drawString(50, y, recept.naam)
    y -= 30

    # Omschrijving
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.grey)
    c.drawString(50, y, recept.omschrijving)
    y -= 25

    # Streep
    c.setStrokeColor(colors.HexColor("#2e86ab"))
    c.setLineWidth(1.5)
    c.line(50, y, breedte - 50, y)
    y -= 20

    # Personen en kcal
    c.setFont("Helvetica", 11)
    c.setFillColor(colors.black)
    c.drawString(50, y, "Personen: " + str(recept.aantal_personen) + "   |   Totaal kcal: " + str(totaal_kcal))
    y -= 25

    # Ingredienten
    c.setFont("Helvetica-Bold", 14)
    c.setFillColor(colors.black)
    c.drawString(50, y, "Ingredienten")
    y -= 18

    for ingredient in recept.ingredienten:
        gekozen = ingredient.get_ingredient(plantaardig)
        c.setFont("Helvetica", 11)
        c.drawString(60, y, "•  " + str(gekozen))
        y -= 18

    y -= 10

    # Stappen
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Bereidingsstappen")
    y -= 18

    nummer = 1
    for stap in recept.stappen:
        c.setFont("Helvetica", 11)
        c.setFillColor(colors.black)
        c.drawString(60, y, str(nummer) + ".  " + stap.beschrijving)
        y -= 18
        if stap.tip is not None:
            c.setFont("Helvetica", 10)
            c.setFillColor(colors.HexColor("#e07b39"))
            c.drawString(75, y, "Tip: " + stap.tip)
            y -= 18
        nummer += 1

    c.save()
    print("PDF opgeslagen als: " + bestandsnaam)