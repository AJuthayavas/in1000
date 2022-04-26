#Oppretter en prosedyre. Her skal man taste inn alderen, og ved hjelp av en if-elif test skal brukeren#
#få beskjed om pris på billetten utifra alderen de selv putter inn i input-feltet nedenfor.#
def print_ticket ():
    alder = int(input("Tast inn alderen på eieren av billetten: "))
    billettpris = 0

    if alder <= 17:
        billettpris = 30

    elif 17 < alder < 63:
        billettpris = 50

    elif alder >= 63:
        billettpris = 35

    print("Siden du er", alder, "år gammel, må du betale", billettpris, "kr.")

#Prosedyre - tester for alder 15, 31 og 63#
print_ticket()
print("..................................")
print_ticket()
print("..................................")
print_ticket()
print("..................................")



"""
Nei, på starten fungerte ikke koden. Fordi da jeg tastet inn 63 som alder, så printet
den ut at prisen ble 50kr. Det var veldig rart, men jeg fant heldigvis ut feilen, og
det skyldes at jeg skrev:

elif alder > 17:
    billettpris = 50

elif alder >= 63:
    billettpris = 35


Feilen var at jeg skulle ha puttet den slik:


elif 17 < alder < 63:
    billettpris = 50

elif alder >= 63:
    billettpris = 35

Problemet var at programmet mitt ikke skjønte at grensen for 50kr per billett, skulle
stoppe etter 62 år. Den fortsettet bare med 50kr, selv om alderen gikk forbi 63.

Håper det her ga mening?!
"""
