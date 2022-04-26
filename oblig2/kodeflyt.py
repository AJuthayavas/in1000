def print_prosa():
    print("Melding til alle gaardseiere:")
    print("Antall dyr på gaarden: ")


antall_dyr = 4
print_prosa()
print(antall_dyr)
antall_nye_dyr = int(input("Hvor mange nye dyr kommer til gaarden: "))
antall_dyr = antall_dyr + antall_nye_dyr
print_prosa()
print(antall_dyr)


if antall_dyr > 12:
    print("Det er mer enn ett dusin dyr på gaarden!")

elif antall_dyr == 12:
    print("Det er ett dusin dyr på gaarden!")

else:
    print("Det er mindre enn ett dusin dyr på gaarden!")
