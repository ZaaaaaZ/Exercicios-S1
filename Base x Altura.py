## Criar um modelo que calcula automaticamente a Area de um Retangulo
# Adicionar o calculo de Triangulos

##  Area (A) = Base (B) * Altura (H) 
# Area (A) = Base (B) * Altura (H) / 2

## Criando variaveis A, B, H
print(40 * "-")
print("INPUTS".center(40))
print("Este Programa tem o intuito de:\n- Calcular automáticamente a Area do Retângulo e Triângulo.")

b = float(input("\nDigite o valor da BASE: "))
h = float(input("Digite o valor da ALTURA: "))
print(40 * "-")
## Calculo da Area do retangulo e Triangulo:
AR = b * h
AT = AR / 2

## Retorno

print(40 * "-")
print("AREA".center(40))
print(f"Area do Retnâgulo: {AR:.2f}m².")
print(f"Area do Triângulo: {AT:.2f}m².")
print(40 * "-")

