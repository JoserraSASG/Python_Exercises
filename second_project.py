#Los vendedores reciben un 13% de las ventas totales
#El programa debe de saber el nombre del usuario y las ventas para calcular el total de las comisiones
#Le saltará una frase que diga OK, NOMBRE TU COMISIÓN ESTE MES SUPONE TANTO Y GANASTE TANTO
#No tener mas de dos decimales
nombre = input("¿Cuál es tu nombre?")
ventas = float(input("¿Cuáles han sido tus ventas este mes?"))
comision_perc = 0.13
salario = float(input("¿Cuál es tu salario neto mensual?"))
comision = ventas * comision_perc
print(f"¡Enhorabuena! {nombre}, debido a tus ventas por valor de {ventas} este mes percibirás un total de: {round(salario + comision, 2)}€ como salario neto")