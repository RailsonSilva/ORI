nome = "Railson"
nomemin = nome.lower() #minusculo
print(nomemin)

nome = "              jessica   gomes\t\n   "
print(nome)
nome1 = nome.strip() # retorna uma cópia da string sem espaços na frente e atrás
print(nome1)

frase = "quem casa quer casa"
print(frase)
frase1 = frase.replace("casa", "bola") #substitui aparições de "casa" por "bola"
print(frase1)

fraseA = "quem casa quer casa pois é casado" #TOMAR CUIDADO
print(fraseA)
fraseAA = fraseA.replace("casa", "bola")
print(fraseAA)

#podemos usar o método replace para fazer remoção na string
fraseAAA = fraseA.replace("casa ", "")
print(fraseAAA)

#como a remoção dos espaços
fraseA = fraseA.replace(" ", "")
print(fraseA)

#o método split serve para "picotar uma string em uma lista
frase = "quem casa quer casa pois é casado"
frase = frase.split("casa")
print(frase)
print("==================================")

#podendo ser utilizado para separar arquivos csv
#caso não seja passado nenhum padrão, o " " é passado como default
frase = "quem, casa ,quer ,casa, pois, é ,casado"
print(frase)
frase = frase.split(",")
print(frase)
frase = "".join(frase)
print(frase)
frase = frase.split(" ")
print(frase)

print("==================================")














