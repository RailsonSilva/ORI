nome = input("Digite um nome: ")
nomeMin = nome.lower()

vogais = 0
consoantes = 0

for c in nomeMin: 
    if c in ('a', 'e', 'i', 'o', 'u') and c.isalpha():
        vogais += 1
    elif c.isalpha():
        consoantes += 1

print("Numero de vogais: ", vogais)
print("Numero de consoantes: ", consoantes)