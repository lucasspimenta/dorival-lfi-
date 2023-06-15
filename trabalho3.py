vetorPossibilidade = [True, False]

linhas1 = 0
verdade1 = 0
mentira1 = 0

linhas2 = 0
verdade2 = 0
mentira2 = 0

listaFormula1 = []
listaFormula2 = []

quant = int(input('Digite se a quantidade de variáveis é 2 ou 3: '))

formula1 = input('Digite a fórmula 1: ')
formula2 = input('Digite a fórmula 2: ')

if quant == 2:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            if eval (formula1):
                resultadoF = True
                verdade1+=1
                listaFormula1.append(True)
            else: 
                resultadoF = False
                mentira1 +=1
                listaFormula1.append(False)
        
            print(f'A = {a} \t B = {b} \t H = {resultadoF}')
            linhas1+=1
        

    print(f'Total de linhas com resultado VERDADEIRO: {verdade1}')
    print(f'Total de linhas com resultado FALSO: {mentira1}')
    print(f'Total de linhas da tabela: {linhas1}')

    if mentira1 == 0:
        print('Essa fórmula é TAUTOLÓGICA.')
    elif verdade1 == 0:
        print('Essa fórmula é CONTRADITÓRIA.')
    else:
        print('Essa fórmula é SATISFATÓRIA.')

if quant == 3:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            for c in vetorPossibilidade:
                if eval (formula1):
                    resultadoF = True
                    verdade1+=1
                    listaFormula1.append(True)
                else: 
                    resultadoF = False
                    mentira1 +=1
                    listaFormula1.append(False)
            
                print(f'A = {a} \t B = {b} \t C = {c} \t H = {resultadoF}')
                linhas1+=1
            

        print(f'Total de linhas com resultado VERDADEIRO: {verdade1}')
        print(f'Total de linhas com resultado FALSO: {mentira1}')
        print(f'Total de linhas da tabela: {linhas1}')

        if mentira1 == 0:
            print('Essa fórmula é TAUTOLÓGICA.')
        elif verdade1 == 0:
            print('Essa fórmula é CONTRADITÓRIA.')
        else:
            print('Essa fórmula é SATISFATÓRIA.')

if quant == 2:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            if eval (formula2):
                resultadoF = True
                verdade2+=1
                listaFormula2.append(True)
            else: 
                resultadoF = False
                mentira2 +=1
                listaFormula2.append(False)
        
            print(f'A = {a} \t B = {b} \t H = {resultadoF}')
            linhas2+=1
        

    print(f'Total de linhas com resultado VERDADEIRO: {verdade2}')
    print(f'Total de linhas com resultado FALSO: {mentira2}')
    print(f'Total de linhas da tabela: {linhas2}')

    if mentira2 == 0:
        print('Essa fórmula é TAUTOLÓGICA.')
    elif verdade2 == 0:
        print('Essa fórmula é CONTRADITÓRIA.')
    else:
        print('Essa fórmula é SATISFATÓRIA.')

if quant == 3:
    for a in vetorPossibilidade:
        for b in vetorPossibilidade:
            for c in vetorPossibilidade:
                if eval (formula2):
                    resultadoF = True
                    verdade2+=1
                    listaFormula2.append(True)
                else: 
                    resultadoF = False
                    mentira2 +=1
                    listaFormula2.append(False)
            
                print(f'A = {a} \t B = {b} \t C = {c} \t H = {resultadoF}')
                linhas2+=1
            

        print(f'Total de linhas com resultado VERDADEIRO: {verdade2}')
        print(f'Total de linhas com resultado FALSO: {mentira2}')
        print(f'Total de linhas da tabela: {linhas2}')

        if mentira2 == 0:
            print('Essa fórmula é TAUTOLÓGICA.')
        elif verdade2 == 0:
            print('Essa fórmula é CONTRADITÓRIA.')
        else:
            print('Essa fórmula é SATISFATÓRIA.')


print('FAZENDO ANÁLISE DE EQUIVALÊNCIA ENTRE AS FÓRMULAS: ')

if listaFormula1 == listaFormula2:
    print('As fórmulas são equivalentes.')
else:
    print('As fórmulas não são equivalentes.')