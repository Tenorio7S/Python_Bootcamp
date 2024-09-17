# saldo = 2000
# saque = float(input("Informe o valor do saque:"))

# if saldo >= saque:
   # print("Realizando saque!")

# if saldo < saque:
    # print("Saldo insuficiente!")

MAIOR_IDADE = 18
IDADE_ESPECIAL = 14

idade = int(input("Informe sua idade: "))

if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar a CNH")

if idade < MAIOR_IDADE:
    print("Ainda não pode tirar CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
else:
    print("Ainda não pode tirar CNH")


if idade >= MAIOR_IDADE:
    print("Maior de idade, pode tirar CNH")
elif idade == IDADE_ESPECIAL:
    print("Pode fazer aulas teoricas, mas não pode fazer as práticas.")
else:
    print("Ainda não pode tirar CNH")


