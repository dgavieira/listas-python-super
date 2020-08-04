dado_alunos = dado_notas = ""

#ler dados do arquivo alunos
with open("L9_q_5_alunos.txt") as alunos:
    dado_alunos = alunos.read()
    alunos.close()

#ler dados do arquivo notas
with open("L9_q5_notas.txt") as notas:
    dado_notas = notas.read()
    alunos.close()

#unindo os arquivos
with open('alunos_e_notas.txt','w') as diario:
    diario.write(dado_alunos + "\t" + dado_notas)
    diario.close()