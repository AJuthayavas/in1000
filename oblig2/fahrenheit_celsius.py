#Her oppretter jeg en variabel for fahrenheit, og deretter printes det ut en meldng til brukeren om hva slags fahrenheit jeg har angitt til oppgaven#
fahrenheit = 21
print("Admin har satt fahrenheit til:", fahrenheit, "°F")

#Her oppretter jeg en variabel som omgjør fahrenheit til celsius. Deretter printes det ut en melding til brukerne#
celsius = ((fahrenheit) - 32) * 5/9
print("Gjør vi om dette til Celsius, blir svaret:", celsius, "°C")

print("............................")

print("Hittil har kun admin tilgang til inputfeltet, nå skal brukeren få velge temperatur selv")

print("............................")

#Nå opprettes det et input felt, og her skal brukren taste inn en fahrenheit de vil omgjøre til celsius.#
fahrenheit2 = int(input("Tast inn en temperatur som du ønsker å omgjøre: "))
celsius2 = ((fahrenheit2) - 32) * 5/9
print("Gjør vi om dette til Celsius, blir svaret:", celsius2, "°C")
