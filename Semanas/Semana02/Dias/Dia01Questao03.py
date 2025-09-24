"""

📌 Calculadora simples

Peça dois números.

Pergunte a operação (+, -, *, /).

Mostre o resultado conforme a escolha.

"""

print(f"Bem-vindo a calculadora simples de 2 números")
print(f"Me diz seu primeiro número")
primeiroNumero = float(input())
print(f"Me diz seu segundo número:")
segundoNumero = float(input())
print(f"Qual operação você fazer?")
print(f"1 - Soma")
print(f"2 - Subtração")
print(f"3 - Multiplicação")
print(f"4 - Divisão")
escolha = int(input())
if escolha == 1:
    print(f"Resultado: {primeiroNumero + segundoNumero}")
elif escolha == 2:
    print(f"Resultado: {primeiroNumero - segundoNumero}")
elif escolha == 3:
    print(f"Resultado: {primeiroNumero * segundoNumero}")
elif escolha == 4:
    print(f"Resultado: {primeiroNumero / segundoNumero}")
else:
    print(f"Não existe operação com esse valor")