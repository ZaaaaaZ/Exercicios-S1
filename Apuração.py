## Fazer um programa que retorne as % de votos, separadas por: 
# - Em Branco;
# - Nulos;
# - Validos;
# - total.

## Variaveis para descobrir o total 
print(40 * "-")
print("APURAÇÂO".center(40))
print("Este programa tem o intuito de:\n- Informar a distribuição, em porcentagem(%), dos votos totais simulados.\n")
v_branco = int(input("Informe o total de Votos Em Branco: "))
v_nulos = int(input("Informe o total de Votos Nulos: "))
v_validados = int(input("Informe o total de Votos Validados: "))

## Total de votos
totais_votos = v_branco + v_nulos + v_validados

## distruibuindo em porcentagem
p_vb = v_branco / totais_votos * 100
p_vn = v_nulos / totais_votos * 100
p_vv = v_validados / totais_votos * 100

print(40 * "-")
print(f"O total de Votos foram {totais_votos:.0f}\n")
print(f"Os Votos em Branco correspondem a {p_vb:.0f}%")
print(f"Os Votos Nulos correspondem a {p_vn:.0f}%")
print(f"Os Votos Validados correspondem a {p_vv:.0f}%")
print(40 * "-")
