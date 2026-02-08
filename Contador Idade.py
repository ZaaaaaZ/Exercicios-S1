## Criar um contador de anos, meeses e dias. De acordo com o Input do usuario

## imporando uma biblioteca
from datetime import datetime, date, timedelta

## input de entrada
data_nascimento = input("Digite a sua data de nascimento(dd/mm/aaaa): ")

## formatação e dia de hoje
nasc = datetime.strptime(data_nascimento, "%d/%m/%Y")
hoje = datetime.today()

idade = hoje.year - nasc.year

if (hoje.month, hoje.day) < (nasc.month, nasc.day):

    idade -= 1

mes = hoje.month - nasc.month

if hoje.day < nasc.day:

    mes -= 1

if mes < 0:

    mes += 12

if hoje.day >= nasc.day:

    dias = hoje.day - nasc.day

else:

    mes_ant = hoje.replace(day=1) - timedelta(days= 1)
    dias = mes_ant.day - nasc.day + hoje.day


print(40 * "-")
print("CONTADDOR".center(40))
print("Este programa tem como intuito:\n- O calculo automático da sua: IDADE, MESES e DIAS de vida.")
print(f"\nAtualmente você tem:\n1 - {idade} anos;\n2 - {mes} meses;\n3 - {dias} dias de vida.")
print(40 * "-")