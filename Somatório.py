print(40 * "-")
print("SOMÁTORIO:")
print("Este programa tem como objetivo:\n- Solicitar 2 valores, informar os\nnumeros pares dentre eles e o seu somátorio.\n")


i = int(input("Informe o menor valor"))
s = int(input("Informe o maior valor"))

soma = 0

print("\nNumeros Pares:")
for i in range(i + 1, s):
    if i % 2 == 0:
        print(i)
        soma += 1
    
print("\Somátorio:", soma)
print(40 * "-")