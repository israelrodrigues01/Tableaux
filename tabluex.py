tamatual = 2

ramo = []
# Criando as formulas


# Função para criar ramos betas
def beta(formula):
  print('beta')


# Função para criar ramos alfas
def alfa(formula):
  print('implica - falso')
  print('e - verdadeiro')
  print('ou - falso')
  print('negação - verdadeiro/falso')

def retirarEspaco(string):
  return string.strip()

def criarFomula(formula):
  if '|-' in formula:  
    primeiro, segundo = formula.split('|-') # todos os primeiros devem ser verdadeiror, e o segundo devem ser falsos;
    
    segundo = 'F'+ retirarEspaco(segundo)
    ramo.append(segundo)
    criarFomula(segundo)
    

  elif '->' in formula:  
    primeiro,segundo = formula.split('->')
      
    ramo.append(segundo)

  elif '^' in formula:  
    primeiro,segundo = formula.split('^')
    ramo.append(segundo)

  elif 'v' in formula:  
    primeiro,segundo = formula.split('v')
    ramo.append(segundo)

  elif '-' in formula:  
    primeiro, segundo = formula.split('-')
    ramo.append(segundo)


criarFomula('|- r -> c')

print(ramo)




# texto = "Olá, Mundo, Python"
# palavras = texto.split(",", 1)
# primeira_palavra = palavras[0]

# print(primeira_palavra)  # Saída: Olá
