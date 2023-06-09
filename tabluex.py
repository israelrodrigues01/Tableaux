import os

ramos = []  # Array dos ramos
betas = []  # Array dos betas
pilhaDeRamos = []  # Array das pilhas de ramos betas B2 (Beta 2)
tamAtual = 0  # Posição atual que está no meu array de ramos

# Função de verificar ramos fechados ou abertos


def verificarFechamento():
    for i, valor1 in enumerate(ramos):
        for j, valor2 in enumerate(ramos):
            if valor1[1] == valor2[1] and i != j:
                if len(valor1) == 2 and len(valor2) == 2:
                    if valor1[0] != valor2[0]:
                        return True
                        # if not pilhaDeRamos:
                        #     # Se o ramo for fechado, verificar se ainda exite algum valor na pilha, caso não tenha nenhum valor na pilha e todos foram fechados, logo está formula é satisfativel, se não, caso tenha valor, verificar se é ramo fechado ou aberto;
                        # else:
                        #     return print('Pilha não vázia, mas ramo fechado')
                    else:
                        return False
                        # Se o ramo for aberto, a formula não é satisfativel


def birfucacoes():
    if pilhaDeRamos:
        ultmoRamoPilha = pilhaDeRamos[-1][1]
        del ramos[ultmoRamoPilha+1:]
        ramos[ultmoRamoPilha] = pilhaDeRamos[-1][0]
        pilhaDeRamos.pop()
        satisfatibilidade()


def satisfatibilidade():
    if verificarFechamento() == True:
        if not pilhaDeRamos:
            print('Satisfatível')
        else:
            birfucacoes()
    else:
        print('Insatisfatível')

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

    # Adicionar na pilha de ramos B2 (Beta 2)
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

# Função para tirar espaços em branco da string


def retirarEspaco(string):
    return string.strip()

# Função para criar as formulas


def criarFomula(formula):
    if '|-' in formula:
        # todos os primeiros devem ser verdadeiror, e o segundo devem ser falsos;
        primeiro, segundo = formula.split('|-')

        # Array de todas as formulas das hipoteses
        subformulasPrimeiro = primeiro.split(',')
        # Array de todas as formulas das conclusões
        subformulasSegundo = segundo.split(',')

        if len(subformulasSegundo[0]) > 0:
            for no in subformulasSegundo:  # Caminhando em cada nó do array e atribuindo valor de falso para cada um
                form = 'F' + retirarEspaco(no)
                ramos.append(form)

        if len(subformulasPrimeiro[0]) > 0:
            for no in subformulasPrimeiro:  # Caminhando em cada nó do array e atribuindo valor de falso para cada um
                form = 'T' + retirarEspaco(no)
                ramos.append(form)

        for no in ramos:  # Caminhando em cada nó dos ramos e criando uma formula para cada um
            criarFomula(no)

    elif '->' in formula:
        if formula[0] == 'F':
            alfa(formula[1:], '->')
        else:
            beta(formula[1:], '->')

    elif '^' in formula:
        if formula[0] == 'F':
            beta(formula[1:], '^')
        else:
            alfa(formula[1:], '^')

    elif 'v' in formula:
        if formula[0] == 'F':
            alfa(formula[1:], 'v')
        else:
            beta(formula[1:], 'v')

    elif '-' in formula:
        alfa(formula, '-')


os.system('cls')
formula = input('Digite a fórmula: ')
criarFomula(formula)  # Formula na qual será criada


os.system('cls')
print('Formula: \n' + formula + '\n')
print('Está fórmula é: ')
satisfatibilidade()
