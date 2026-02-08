## OBJ criar um programa que diga o Numero anterior, dentro de uma lista.

## kkkk Eu acabei confundindo e fiz em letras, mas vou fazer o de numeros abaixo.

## Lista de Numeros e Teclas:
numeros = [1,2,3,4,5,6,7,8,9,10]
teclado = "QWERTYUIOPASDFGHJKLÇZXCVBNM"

## Criando um cabeçalho e looping para que o forçe uma resposta correta.
while True:

    print(40 * "-")
    print("VERIFICAÇÂO DE LETRAS.".center(40))
    print("Este programa tem o intuito de:\n- Te informar o valor anterior do que for inserido.")
    letra = input("\nDigite uma Letra: ").upper()

    ##Verificação se há o caractere na lista
    if letra in teclado:
        
        ## essa variavel verifica a posição da letra, em relação a letra.
        index = teclado.index(letra)

    #Se sim, impre a letra e seu antecessor, para por fim quebrar o looping e passars para o proximo
        if index > 0:
            
            ## Aqui, a gente diz a letra escolhida e -1 posição, através do valor informado, assim retornando a anterior.
            print(f"A Letra escolhida foi a(o): {letra};\nJá a antecessora, na ordem do teclado, seria a(o): {teclado[index-1]}.")
            print(40 * "-")
            break
            
    ## Se não, volta o looping do inico.
        else:

            print("\nLetra inexistente na escala. Tente novamente.")    
            print(40 * "-")

    else:

        print("\nLetra inexistente na escala. Tente novamente.")    
        print(40 * "-")

while True:

    ## Cabeçalho Numerico
    print(40 * "-")
    print("CONTADOR DE NUMEROS.".center(40))
    Numb = int(input("Digite um numero entre 1 a 10:"))
    Valor = Numb
   
  
    ##Verificação se o numeros está dentro da lista
    if Numb in numeros:

        index = numeros.index(Numb)

        #Se sim, printa e quebra o looping
        if index > 0:

            print(f"O seu Numero é o: {Valor};\nJá o antecessor é o: {numeros[index - 1]}.")
            print(40 * "-")
            break

    ## Se não, volta o looping do inico.
        else: 
                    
            print("\nNúmero inexistente na escala. Tente novamente.")
            print(40 * "-")
    else:

        print("\nNúmeo inexistente na escala. Tente novamente.")    
        print(40 * "-")
