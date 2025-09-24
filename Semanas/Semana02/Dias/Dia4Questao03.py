"""

📌 Inverter string

Peça uma palavra.

Mostre ela invertida (exemplo: Python → nohtyP).

(Dica: pode usar for ou fatiamento [::-1]).

"""

print(f"Digite uma palavra")
palavraDigitada = input()

for palavraDigitada in palavraDigitada:
    for i in palavraDigitada:
        print()