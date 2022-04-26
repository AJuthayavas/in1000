#Her lager jeg en ordbok og fyller den inn med informasjon oppgaven har gitt meg#
ordbok = {
"Melk": 14.90,
"Brød": 24.90,
"Yoghurt": 12.90,
"Pizza": 39.90
}

print(ordbok)

print("..................................")

#Oppretter fire inputfelt. To av dem skal representere varenavn, og de to siste skal være prisen på varene.#
produkt1 = input("Tast inn den første varen din: ")
prislapp1 = float(input("Tast inn prisen på den varen: "))

print("..................................")

produkt2 = input("Tast inn den andre varen din: ")
prislapp2 = float(input("Tast inn prisen på den varen: "))


#Setter de 4 inputtene inni orboken. Deretter printer jeg ut den oppdaterte ordboken.#
ordbok[produkt1] = prislapp1
ordbok[produkt2] = prislapp2
print("..................................")

print(ordbok)
