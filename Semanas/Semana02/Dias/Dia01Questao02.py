"""
📌 Categoria de idade

Pergunte a idade do usuário.

Classifique:

Criança (0–12)

Adolescente (13–17)

Adulto (18–59)

Idoso (60+).

"""

print(f"Qual sua idade?")
idade = int(input())

if idade >= 0 and idade <= 12:
    print(f"Criança")
elif idade >= 13 and idade <= 17:
    print(f"Adolescente")
elif idade >= 18 and idade <= 59:
    print(f"Adulto")
else:
    print(f"Idoso")