#Mariana Lobão-#Todo.

#listas com as notas de cada candidato já inseridos no sistema + lista com as notas dos condidados inseridos pelo usuário.
notas_candidato0 = [5, 10, 8, 8]
notas_canditato1 = [6,7,6,3]
notas_canditato2 = [9,6,9,9]
notas_candidato3 = [6,5,7,9]
lista_de_candidatos = [notas_candidato0 , notas_canditato1 , notas_canditato2 , notas_candidato3]

#Variável para perguntar ao usuário quantos candidatos ele gostaria de inserir notas.
#while para realizar o loop até a quantidade de candidatos inseridos pelo usuário.
#As notas dos candidatos inseridos pelo uruário foram colocadas em uma lista e após isso, adicionadas em outra lista para ficarem todas juntas apenas em uma lista.
quantidadedecandidatos = int(input('Quantos candidatos você gostaria de cadastras? '))
contador = 0
while contador < quantidadedecandidatos:
    notae = int(input('Digite a nota para Entrevista: '))
    notatt = int(input('Digite a nota para Teste teórico: '))
    notatp = int(input('Digite a nota para Teste Prático: '))
    notass = int(input('Digite a nota para Soft Skills: '))
    listanotas = [notae , notatt , notatp , notass]
    lista_de_candidatos.append(listanotas)
    contador = contador +1


#Variáveis para perguntar ao usuário a nota requisito para cada etapa do processo seletivo.
nota_requisito_e = int(input('Digite a nota requisito para Entrevista: '))
nota_requisito_tt = int(input('Digite a nota requisito para Teste Teórico: '))
nota_requisito_tp = int(input('Digite a nota requisito para Teste Prático: '))
nota_requisito_ss = int(input('Digite a nota requisito para Soft Skills: '))
lista_requisitos = [nota_requisito_e ,nota_requisito_tt , nota_requisito_tp , nota_requisito_ss]

#função e for para comparar se os índices e valores da lista_requisitos são iguais ou maiores que os índices e valores da lista_de_candidatos.
def candidatos_validados():
    candidatos_ok = []
    for i , lista in enumerate(lista_de_candidatos):
        cont = 0
        for indice , valor in enumerate(lista):
            if lista_requisitos[indice] <= valor:
                cont = cont +1
        if cont == 4:
            candidatos_ok.append(lista_de_candidatos[i])
    
    
    for i, valor2 in enumerate(candidatos_ok):
        print('e{}_t{}_p{}_s{}'.format(valor2[0],valor2[1],valor2[2],valor2[3]))

candidatos_validados()




