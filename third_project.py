#Analizador de texto
texto = input("Ingrese un texto de su preferencia: ")
texto = texto.lower()
buscar_python = "python" in texto
dic = {True:"sí", False:"no"}
letras = []
letras.append(input("Ingrese la primera letra de la que se hará conteo: ").lower())
letras.append(input("Ingrese la segunda letra de la que se hará conteo: ").lower())
letras.append(input("Ingrese la tercera letra de la que se hará conteo: ").lower())

print(f"La letra '{letras[0]}' se encuentra {texto.count(letras[0])} veces.\n"
      f"La letra '{letras[1]}' se encuentra {texto.count(letras[1])} veces.\n"
      f"La letra '{letras[2]}' se encuentra {texto.count(letras[2])} veces.\n"
      f"La longitud de tu texto es de {len(texto)} caracteres.\n"
      f"Y tiene un total de {len(texto.split())} palabra(s).\n"
      f"El primer caracter de tu texto es '{texto[0]}', mientras que el último es '{texto[-1]}' \n"
      f"Tu texto original era:\n"
      f" '{texto}'\n\n"
      f"Y tu texto invertido es: \n"
      f"'{texto[::-1]}'\n"
      f"Por último, se hará una comprobación de si hablabas en el texto del lenguaje de programación con el\n"
      f"que está hecho este programa.\n"
      f"Este texto {dic[buscar_python]} parece hablar sobre Python")

