def numeros_perfumeria():
    for n in range(1,1000000):
        yield f"P - {n}"


def numeros_farmacia():
    for n in range(1,1000000):
        yield f"F - {n}"

def numeros_cosmetica():
    for n in range(1,1000000):
        yield f"C - {n}"

p = numeros_perfumeria()
f = numeros_farmacia()
c = numeros_cosmetica()

def decorador(opcion):
    print("\n" + "*" * 23)
    print("Su numero es: ")
    if opcion == "P":
        print(next(p))
    elif opcion == "F":
        print(next(f))
    elif opcion == "C":
        print(next(c))
    print("Espere a ser atendido")
    print("*" * 23 + "\n")