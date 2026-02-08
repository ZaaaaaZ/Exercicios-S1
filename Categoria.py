## Escreva um prgorama que separ por categoria de atelta

## Categorias
## Infantil - 5 a 7 anos;
## Inicado - 8 a 10 anos;
## Juvenil - 11 a 13 anos;
## Junior - 14 a 17 anos;
## Sénior - Maiores de 18 anos.

  
print(40 * "-")
print("INSCRIÇÔES".center(40))
print("Este programa tem como intuito:\n- Classificar atletas, em relação a sua idade.\n")
participantes = int(input("Numero de participantes:"))
atletas = []

def categoria(idade):
    if 5 <= idade <= 7:
        return "Infantil."
    elif 8 <= idade <= 10:
        return "Iniciado."
    elif 11 <= idade <= 13:
        return "Juvenil."
    elif 14 <= idade <= 17:
        return "Junior."
    elif idade >= 18:
        return "Sénior."
    else:
        return "idade fora das categorias."

def Atleta():

    nome = str(input("Nome:"))
    idade = int(input("Idade:")) 
    classificação = categoria(idade)
    return nome, idade, classificação

for i in range(participantes):

    print(f"\nAtleta {i + 1}")
    atletas.append(Atleta())
  
print(40 * "-")
print("CLASSIFICAÇÔES".center(40))
for nome, idade, classificação in atletas:

    print(f"\nCompetidor(a): {nome}\nIdade: {idade} anos | Categoria: {classificação}")

print(40 * "-")