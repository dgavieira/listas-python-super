student_details= [
  {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
  {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
  {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
]
output = []
cont = 0
for d in student_details:
    di = student_details[cont]
    soma = di['V'] + di['VI']
    media = soma/2
    dout = {'id' : cont + 1, 'subject' : 'math', 'V+VI' : media}
    output.append(dout)
    cont = cont + 1

print(output)