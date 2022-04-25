# import random

# print("Lista de 100 numeros aleatorios")
# l = [random.randint(1,100) for x in range(1,101)]
# print(l)


# print("Lista sem repetidos")
# l = list(set(l)) # retira repetidos ao passar para set e depois volta a list
# print(l)


# # gera uma lista de 20 tuplos com numeros aleatorios 
# l2 = []
# for i in range(1,20) : 
#     x = random.randint(0,20)
#     tuple = (x,2*x)
#     l2.append(tuple)
# print(l2)



# listTuples = [(x,2*x) for x in range(1,11)]
# print(listTuples)
# # Tuplos , sequencias imutáveis 

# meudici = {
#     "nome" : "Pl" ,
#     "curso" : "LEI"
# }


# EXERCICIO 2

import csv

with open('/Users/ruimoreira/Desktop/MIEI/3º ano/alunos.csv', mode ='r')as file:
    csvFile = csv.reader(file)
       
    def countlines(csvFile) :
      res = 0
      for lines in csvFile:
          res = res + 1
      return res


    #print(countlines(csvFile))

    # for lines in csvFile:
    #     print(lines)

    dicionario = { }
    for lines in csvFile:
        # linhas[lines[0]] = lista[1:]
        idaluno,nome,curso,*notas = lines
        # print(notas)
        aluno = { "nome" : nome,
                  "curso" : curso,
                  "notas" : notas}
        alunoAux = {idaluno : aluno}
        
        dicionario.update(alunoAux)
        #print(alunoAux)

del dicionario["id_aluno"]
#print(dicionario)


# parte que ve que alunos tem a melhor media 
melhores_alunos = []
melhor_media = 0
for key , value in dicionario.items() :
    notas = value["notas"]
    media = (int(notas[0]) + int(notas[1]) + int(notas[2]) + int(notas[3])) / 4
    if media == melhor_media :
        melhores_alunos.append(key)
    else :
         if media > melhor_media :
            melhores_alunos = [key]
            melhor_media = media 

print(melhores_alunos)



# parte que conta quantos alunos tem media superior a 15
n_alunos = 0
for key , value in dicionario.items() :
    notas = value["notas"]
    media = (int(notas[0]) + int(notas[1]) + int(notas[2]) + int(notas[3])) / 4
    if media > 15
        n_alunos = n_alunos + 1

print(n_alunos)



