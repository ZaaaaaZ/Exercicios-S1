pessoas = []

print(40 * "-")
print("COMPARADOR".center(40))
print("Este programa tem como objetivo:\n- Comparar altura e peso de 2 pessoas\ne informar o maior e o mais pesado.")


for i in range(2):
    print(f"\nPessoa {i + 1}")
    nome = input("Nome: ")
    altura = float(input("Altura (em metros): "))
    peso = float(input("Peso (em kg): "))
    pessoas.append({"nome": nome, "altura": altura, "peso": peso})

# Encontrar a mais pesada
ms_pesada = max(pessoas, key=lambda p: p["peso"])
# Encontrar a mais alta
ms_alta = max(pessoas, key=lambda p: p["altura"])

print(f"\nA pessoa mais pesada é: {ms_pesada['nome']} com {ms_pesada['peso']} kg.")
print(f"A pessoa mais alta é: {ms_alta['nome']} com {ms_alta['altura']} m.")

print(40 * "-")
