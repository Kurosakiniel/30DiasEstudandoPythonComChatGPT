"""

📌 Exercícios pra você:

Classificação de nota

Peça uma nota (0 a 100).

Mostre:

A (nota >= 90)

B (nota >= 70)

C (nota >= 50)

Reprovado (nota < 50).

"""

print(f"Digite a nota:")
nota = float(input())

if nota >= 90:
    print(f"Você tirou A")
elif nota >= 70:
    print(f"Você tirou B")
elif nota >= 50:
    print(f"Você tirou C")
else:
    print(f"Está Reprovado")