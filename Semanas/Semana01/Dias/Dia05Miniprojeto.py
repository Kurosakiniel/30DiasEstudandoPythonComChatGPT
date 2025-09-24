"""
Mini-projeto: Calculadora de Idade

📌 Regras:

O programa deve pedir:

Nome do usuário

Ano de nascimento

Ano atual

Ele deve calcular a idade aproximada (ano_atual - ano_nascimento).

Mostrar a mensagem final com f-string:
"Olá [nome], você tem aproximadamente [idade] anos."

🔥 Desafio Extra (opcional):

Perguntar também o mês de nascimento e o mês atual, e melhorar o cálculo da idade:

Se o usuário já fez aniversário, usa ano_atual - ano_nascimento.

Se ainda não fez, usa (ano_atual - ano_nascimento) - 1.

"""

print(f"Qual seu nome?")
nomeUser = input()
print(f"Qual o ano do seu nascimento?")
anoNascimento = int(input())
print(f"Qual ano atual?")
anoAtual = int(input())
idade = anoAtual - anoNascimento
fezAniversario = bool
print("Você já fez aniversário?")
print("1: Sim")
print("2: Não")
escolha = int(input())
if(escolha == 1):
    print(f"Olá {nomeUser}, você tem aproximadamente {idade} anos.")
else:
    print(f"Olá {nomeUser}, você tem {(anoAtual - anoNascimento - 1)}")