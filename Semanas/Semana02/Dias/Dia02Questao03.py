"""

📌 Somatório

Peça vários números ao usuário.

O programa deve parar quando o usuário digitar 0.

No final, mostre a soma de todos os números digitados.

"""

contador = 1
somaNumero = 0
while contador > 0:
    print("Digite um número:")
    numerosDigitados = int(input())
    if numerosDigitados == 0:
        somaNumero == numerosDigitados
        somaNumero += numerosDigitados
        break
    else:
        somaNumero == numerosDigitados
        somaNumero += numerosDigitados
    contador += 1

print(somaNumero)