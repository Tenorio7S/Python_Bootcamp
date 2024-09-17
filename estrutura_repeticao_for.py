# texto = input("Informe um texto: ")
texto = ""
VOGAIS = "AEIOU"


# exemplo com iterável
for letra in texto:
        if letra.upper() in VOGAIS:
            print(letra, end="" )
else:
    print()
    print("Executa no final do laço")


# exemplo com bullt in range
for numero in range(0, 100, 2):
    print(numero, end= " ")