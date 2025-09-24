"""

📌 Tabuada com for

Peça um número ao usuário.

Mostre a tabuada desse número de 1 a 10 (usando for).

"""
print(f"Digite um número")
numeroDigitado = int(input())
for i in range(10):
    print(f"{numeroDigitado} * {i+1} = {(numeroDigitado * (i+1))}")
