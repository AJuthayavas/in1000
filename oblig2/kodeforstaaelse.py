a = input("Tast inn et heltall! ")
b = int(a)

if b < 10:
    print(b + "Hei!")

#1. Dette er en lovlig kode, men den funker ikke med alle tall. Den takler ikke negative tall (f.eks: -100)#

#2. Den takler ikke bare negative tall, men også "+" tegnet. Programmet forstår ikke dette. Om det hadde#
#vært komma istedenfor pluss så ville den ha forstått det. Dermed er det ikke mulig å taste inn et tall lavere enn 10.#
