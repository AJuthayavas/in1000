#Skriv et program som ber om og leser inn to datoer, angitt med heltall for dag ogmåned#
#(to variable for hver dato). Eksempel ​24 ​og ​12 ​for 24. desember.#
#Her lagde jeg ulike variabler for de forskjellige datoene (måned og dag), deretter lagde jeg print for de forskjellige inputtene#
dag1 = input("Veg dag (1-31): ")
maned1 = input("Velg måned (1-12): ")
dato1 = maned1 + dag1
print("Datoen din ble (dag+måned): " + dag1 + "." + maned1)
print("Nå skal du velge dato nummer 2: ")
dag2 = input("Veg dag (1-31): ")
maned2 = input("Velg måned (1-12): ")
dato2 = maned2 + dag2
print("Datoen din ble (dag+måned): " + dag2 + "." + maned2)
print("Du fikk disse 2 datoene: " + dag1 + "." + maned1 + " og " + dag2 + "." + maned2)


#Skriv en if-test som tester hvilken dato som kommer først i samme år:#
#a.Hvis den første datoen kommer først skal programmet ditt skrive ut ​“Riktigrekkefølge!”#
#b.Hvis den siste datoen som skrives inn er en tidligere dato, skal programmetskrive ut ​“Feil rekkefølge!”#
#c.Om datoene er like skrives ​“Samme dato!”​ ut.#
#Her vises det om den første datoen kommer før den andre eller ikke#
if dato1 < dato2:
    print("Dette er riktig, den første datoen kom først")

elif dato1 > dato2:
    print("Dette er feil, den første datoen skulle komme først")

else:
    print("Du har oppgitt to eksakt like datoer")
