#programa que le uma string do teclado e conta a frequencia

def contaCaracteres(texto):
    freqs = {} #dicionário vazio
    for c in texto:
        if c not in freqs: #verifica se c já é chave
            freqs[c] = 1
        else:
            freqs[c] = freqs[c] + 1
    
    return freqs

if __name__ == "__main__":

    texto = input("Digite um texto: ")

    frequencias = contaCaracteres(texto)

    print(frequencias)