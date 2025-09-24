"""
📌 Tabuada com while

Peça um número ao usuário.

Mostre a tabuada desse número de 1 a 10.
"""

contador = 1

print(f"Diga um número")
numeroTabuada = int(input())

while contador < 11:
    print(f"Tabuada:  {numeroTabuada * contador}")
    contador += 1