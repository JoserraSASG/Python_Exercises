#va a preguntar el nombre y despues le dira que ha pensado un numero entre el 1 y 100 y que va a
#intentar adivinarlo en 8 intentos, pueden pasar 4 cosas:
# si es menor 1 a superior a 100 dira que no esta permitido
#si dice que que es menor o mayor
#si ha acertado
#si no acierta volvera a pedir otro numero y asi 8 intentos hasta que gane o falle

from random import randint
numero = randint(1,100)
respuesta = int(input("Intenta adivinar un número entero entre el 1 y el 100.\nTienes 8 intentos:"))


for n in respuesta:
    if n < 1 or n > 100:
        print(f"El número no puede ser inferior a 1 o superior a 100. Te quedan {8 - len(respuesta)} intentos")
    elif n == numero:
         print(f"¡Enhorabuena! El número elegido es correcto. Lo has conseguido en {8 - len(respuesta)} intentos")
    elif n < numero:
        print(f"Has fallado. {n} es inferior al número misterioso.Te quedan {8 - len(respuesta)} intentos")
    elif n > numero:
        print(f"Has fallado. {n} es superior al número misterioso. Te quedan {8 - len(respuesta)} intentos")
    elif len(respuesta) == 8:
        print(f"Lo siento. Te has quedado sin intentos, el número correcto era: {numero}")

