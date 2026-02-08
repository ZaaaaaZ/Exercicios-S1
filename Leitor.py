

print(40 * "-")
print("CUSTO E LUCRO".center(40))
print("-Este programa tem como objetivo:\n- Criar 10 inputs, para no final apresentar o menor e o maior numero\n")

numeros = []

for i in range(10):
    n = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(n)

maior = max(numeros)
menor = min(numeros)

print(f"O maior número digitado foi: {maior}")
print(f"O menor número digitado foi: {menor}")

print(40 * "-")