nome = "Tenorio"
idade = 22
profissao = "Programador"
linguagem = "Python"
saldo = 100.510

dados = {"nome": "Tenorio", "idade": 22 }



print("nome: %s idade: %d" % (nome, idade))

print("nome: {} idade: {}".format (nome, idade))

print("nome: {1} idade: {0}".format (idade, nome))

print("nome: {1} idade: {0} nome: {1} {1}".format (idade, nome))
print("nome: {name} idade: {age}".format (name=nome, age=idade))
print("nome: {nome} idade: {idade}".format(**dados))


print(f"nome: {nome} idade: {idade}")
print(f"nome: {nome} idade: {idade} saldo:{saldo}")
print(f"nome: {nome} idade: {idade} saldo:{saldo:10.2f}")

