import os

tamatual = 2

ramo = []
# Criando as formulas


# Função para criar ramos betas
def beta(formula):
  print('beta')


# Função para criar ramos alfas
def alfa(formula, conectivo):
  primeiro, segundo = formula.split(conectivo, 1)
  # Implicação - falso
  if conectivo == '->':
    primeiro = 'T' + retirarEspaco(primeiro)
    segundo = 'F' + retirarEspaco(segundo)
    ramo.append(primeiro)
    ramo.append(segundo)

  # e - verdadeiro
  elif conectivo == '^':
    primeiro = 'T' + retirarEspaco(primeiro)
    segundo = 'T' + retirarEspaco(segundo)
    ramo.append(primeiro)
    ramo.append(segundo)

  # ou - falso
  elif conectivo == 'v':
    primeiro = 'F' + retirarEspaco(primeiro)
    segundo = 'F' + retirarEspaco(segundo)
    ramo.append(primeiro)
    ramo.append(segundo)

  # negação - verdadeiro/falso
  elif conectivo == '-':
    if formula[0] == 'F':
      segundo = 'T' + retirarEspaco(segundo)
    
    else: 
      segundo = 'F' + retirarEspaco(segundo)

    ramo.append(segundo)
  
  criarFomula(primeiro)
  criarFomula(segundo)

def retirarEspaco(string):
  return string.strip()

def criarFomula(formula):
  if '|-' in formula:  
    primeiro, segundo = formula.split('|-') # todos os primeiros devem ser verdadeiror, e o segundo devem ser falsos;
    segundo = 'F'+ retirarEspaco(segundo)
    ramo.append(segundo)
    criarFomula(segundo)
    
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
    


criarFomula('|- -r v -c v c')

os.system('cls')
print(ramo)




# texto = "Olá, Mundo, Python"
# palavras = texto.split(",", 1)
# primeira_palavra = palavras[0]

# print(primeira_palavra)  # Saída: Olá
