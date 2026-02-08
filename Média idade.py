soma = 0
contador = 0

print(40 * "-")
print("MÉDIA:")
print("Este programa tem como objetivo:\n- Criar inputs infinitos, armazenando idades\npara no final dizer a média.\n")


while True:
    idade = int(input("Digite a idade (0 para sair): "))
    if idade == 0:
        break
    if idade < 0:
        print("Idade inválida, digite um valor positivo.")
        continue
    soma += idade
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"\nA média das idades digitadas é: {media:.2f}")
else:
    print("Nenhuma idade válida foi digitada.")

print(40 * "-")
