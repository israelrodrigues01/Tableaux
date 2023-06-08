import os

tamatual = 2

ramos = []
betas = []
pilhaDeRamos =[]
tamAtual = 0
# Criando as formulas

# def verificarFechamento():
#   for valor1 in ramos:
#     for valor2 in ramos:
#       if valor1[1] == valor2[1]:
#         if valor1[0] != valor2[0]:
#           return print('ramo fechado')


# Função para criar ramos betas
def beta(formula, conectivo):
  tamAtual = len(ramos)
  betas.append('x')
  primeiro, segundo = formula.split(conectivo, 1)

  # Implicação - verdadeiro
  if conectivo == '->':
    primeiro = 'F' + retirarEspaco(primeiro)
    segundo = 'T' + retirarEspaco(segundo)
    ramos.append(primeiro)

  # e - falso
  elif conectivo == '^':
    primeiro = 'F' + retirarEspaco(primeiro)
    segundo = 'F' + retirarEspaco(segundo)
    ramos.append(primeiro)

    
  # ou - Verdeiro
  elif conectivo == 'v':
    primeiro = 'T' + retirarEspaco(primeiro)
    segundo = 'T' + retirarEspaco(segundo)
    ramos.append(primeiro)

  # verificarFechamento()
  pilhaDeRamos.append([segundo, tamAtual, betas])

# Função para criar ramos alfas
def alfa(formula, conectivo):
  primeiro, segundo = formula.split(conectivo, 1)
  # Implicação - falso
  if conectivo == '->':
    primeiro = 'T' + retirarEspaco(primeiro)
    segundo = 'F' + retirarEspaco(segundo)
    ramos.append(primeiro)
    ramos.append(segundo)

  # e - verdadeiro
  elif conectivo == '^':
    primeiro = 'T' + retirarEspaco(primeiro)
    segundo = 'T' + retirarEspaco(segundo)
    ramos.append(primeiro)
    ramos.append(segundo)

  # ou - falso
  elif conectivo == 'v':
    primeiro = 'F' + retirarEspaco(primeiro)
    segundo = 'F' + retirarEspaco(segundo)
    ramos.append(primeiro)
    ramos.append(segundo)

  # negação - verdadeiro/falso
  elif conectivo == '-':
    if formula[0] == 'F':
      segundo = 'T' + retirarEspaco(segundo)
    
    else: 
      segundo = 'F' + retirarEspaco(segundo)

    ramos.append(segundo)
  
  criarFomula(primeiro)
  criarFomula(segundo)

def retirarEspaco(string):
  return string.strip()

def criarFomula(formula):
  if '|-' in formula:  
    primeiro, segundo = formula.split('|-') # todos os primeiros devem ser verdadeiror, e o segundo devem ser falsos;

    subformulasSegundo = segundo.split(',')

    for no in subformulasSegundo: # Caminhando em cada nó do array e atribuindo valor de falso para cada um
      form = 'F'+ retirarEspaco(no)
      ramos.append(form)

    for no in ramos: # Caminhando em cada nó dos ramos e criando uma formula para cada um
      criarFomula(no)


  elif '->' in formula:
    if formula[0] == 'F':
      alfa(formula[1:], '->')
    else:
      beta(formula[1:],'->')
  
    

  elif '^' in formula:  
    if formula[0] == 'F':
      beta(formula[1:],'^')
    else:
      alfa(formula[1:], '^')

    

  elif 'v' in formula:  
    if formula[0] == 'F':
      alfa(formula[1:], 'v')
    else:
      beta(formula[1:],'v')

    

  elif '-' in formula: 
    alfa(formula, '-')


criarFomula('|- q -> r, r -> q, c->t, b^c')






os.system('cls')
print(ramos)
# print(betas)
# print(pilhaDeRamos)
# print(verificarFechamento())




# texto = "Olá, Mundo, Python"
# palavras = texto.split(",", 1)
# primeira_palavra = palavras[0]

# print(primeira_palavra)  # Saída: Olá
