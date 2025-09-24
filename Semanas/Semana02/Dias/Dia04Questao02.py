"""

📌 Contar vogais

Peça uma frase ao usuário.

Conte quantas vogais (a, e, i, o, u) aparecem.

Ignore maiúsculas/minúsculas (dica: use .lower()).

"""

print(f"Digite uma frase:")
frase = input()
quantidadeVogais = 0


for frase in frase:
    if frase == frase.lower():
        if frase == 'a':
            quantidadeVogais += 1
        if frase == 'e':
            quantidadeVogais += 1
        if frase == 'i':
            quantidadeVogais += 1
        if frase == 'o':
            quantidadeVogais += 1
        if frase == 'u':
            quantidadeVogais += 1

print(quantidadeVogais)