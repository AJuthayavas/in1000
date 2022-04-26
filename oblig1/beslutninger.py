#Oppagve 2.1 = Skriv et program som ber brukeren om å svare “ja” eller “nei” på om de kunne tenkeseg en brus. Lagre svaret i en variabel.#
#Her opprettet jeg et spørsmål#
spm = input("Kunne du ha tenkt deg en brus? (Ja/Nei): ")


#Oppgave 2.2 = Skriv en if-sjekk som tester hva brukeren har skrevet inn:
#a.Hvis brukeren har svart ​“ja”​ skal programmet skrive ut ​“Her har du en brus!”#
#b.Hvis brukeren har svart ​“nei”​ skal setningen​ “Den er grei.”​ skrives ut.#
#c.Hvis brukeren har svart noe helt annet skal programmet skrive ut ​“Det forstodjeg ikke helt.”#
#Her lagde jeg 3 ulike svarmetoder#
if spm == "Ja":
    print("Ja, jeg vil gjerne ha en brus")

elif spm == "Nei":
    print("Nei takk, jeg vil ikke ha brus")

else:
    print("Kompis, du skal enten svare Ja eller Nei")
