## criar um boletim com base am assinuiddade, nota.

## conição
## assinuidade > 75%  = reprovado
## assinuidade > 75% e 100% nota até 5 = reprovado
## assinuidade > 75% e 100% nota de 5 até 9,5 = exame
## assinuidade > 75% e 100% nota e nota de 10 a 20 = aprovado

# presença
# nota
# Aluno

print(40 * "-")
print("BOLETIM".center(40))
print("Este programa tem como objetivo:\n- Calcular assinuidade e nota do aluno, para Reprovar,Exame e Aprovado.")

ano_letivo = int(input("\nDias Letivos: "))
qnt_alunos = int(input("Quantos alunos serão cadastrados? "))

assinuidade = ano_letivo * 0.75
aluno = []
print(40 * "-")

def aprovação(presença,nota):
    if presença < assinuidade:
        return "Reprovado."
    elif nota <= 5:
        return "Reprovado."
    elif 5 <= nota <= 9.5:
        return "Exame."
    elif nota > 9.5:
        return "Aprovado."

def c_aluno():

    nome = str(input("Nome do(a) Aluno(a): "))
    nota = float(input("Nota do(a) Aluno(a): "))
    faltas = int(input("Quantidade de faltas: "))
    
    presença = ano_letivo - faltas
    sta = aprovação(presença, nota)
    return nome, nota, presença, sta

for i in range(qnt_alunos):
    print(f"\n{i + 1} Aluno(a)")
    aluno.append(c_aluno())

print(40 * "-")
print("BOLETIM".center(40))
for nome, nota, presença, sta in aluno:

    print(f"Nome: {nome}.\nNota: {nota}.\nDias Ausentes: {presença}.\nStatus: {sta}")

print(40 * "-")