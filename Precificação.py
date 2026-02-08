## Criar um programa que precifica para o vendedor

## Valor da Compra / Valor da venda
## valor < 10 / 70%  lucro
## 10 <= valor <= 30 / 50% lucro
## 30 <= valor <= 50 / 40% lucro
## valor >= 50 / 30% lucro

print(40 * "-")
print("CUSTO E LUCRO".center(40))
print("Este programa tem como objetivo:\n- Calcular automaticamente um preço de venda,\nbaseado no custo da compra")
qnt_produto = int(input("\nQuantidade de Produtos a ser calculado:"))
produto = []

def precificação(valor_c):
    if valor_c < 10:
        set_porcento = valor_c * 0.7
        lucro = valor_c + set_porcento
        return lucro
    elif 10 <= valor_c <= 30:
        cin_porcento = valor_c * 0.5
        lucro = valor_c + cin_porcento
        return lucro
    elif 30 <= valor_c <= 50:
        qua_porcento = valor_c * 0.4
        lucro = qua_porcento + valor_c
        return lucro
    elif valor_c >= 50:
        tri_porcento = valor_c * 0.3
        lucro = tri_porcento + valor_c
        return lucro
    else:
        print("numero fora da escala.")


def Produto():

    n_produto = str(input("Nome do Produto:"))
    valor_c = float(input("Custo de Compra:"))
    calculo = precificação(valor_c)
    return n_produto, valor_c, calculo

for i in range(qnt_produto):

    print(f"\nProduto {i + 1}")
    produto.append(Produto())

print(40 * "-")
print("CUSTO E LUCRO".center(40))
for n_produto, valor_c, calculo in produto:

    print(f"\n{n_produto.upper()}\nValor de custo: {valor_c} | {calculo} a se cobrar")

print(40 * "-")
