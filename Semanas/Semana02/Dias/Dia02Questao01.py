"""

📌 Contagem regressiva

Peça um número ao usuário.

Mostre a contagem regressiva até 0.

"""
print(f"Diga um número")
contador = int(input())

while contador >= 0:
    print(f"{contador}")
    contador -= 1