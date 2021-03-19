
texto=input("Ingrese el texto: ")
buscar=input("Que frecuencia hay en el texto de la palabra: ")
# texto = """este es un texto el cual deben contar el numero
# de palabras que tiene, deben tener en cuenta,
# que algunas palabras se separa por un punto, y una
# coma, tambien hay que tener en cuenta, que las palabras
# escritas EN MAYUSCULAS y minusculas cuenta como una este. Texto"""

no_valido = ",;:."
for caracter in no_valido:
     texto = texto.replace(caracter,"")

texto = texto.lower()

palabras = texto.split(" ")

texto="Contando cuantas letras tiene este texto"
re=palabras.count(buscar)
tex="La frecuencia de la palabra ("
r=") es: "
print(tex+buscar+r)
print(re)