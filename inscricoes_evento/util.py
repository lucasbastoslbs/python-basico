def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0])
        leitor.close()
    except:
        pass

def inscricao(lista):
    matricula = input('Informe matrícula: ')
    if matricula in lista:
        print('Esta matrícula já foi inscrita no evento')
    else:
        lista.append(matricula)
        nome = input('Nome: ')
        nome = nome.upper()
        email = input('Email: ')
        email = email.lower()
        escritor = open('inscricoes.dat','a')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')
        escritor.close()

def listagem():
    try:
        leitor = open('inscricoes.dat','r',encoding='utf8')
        for linha in leitor:
            vetor_linha = linha.split(';')
            print('Nome:',vetor_linha[1],'Matrícula:',vetor_linha[0])
        leitor.close()
    except:
        print('Sem inscrições até o momento')

def entrada_saida(lista,matricula,saida):
    lista.append(matricula)
    nome = input('Nome: ')
    nome = nome.upper()
    email = input('Email: ')
    email = email.lower()
    escritor = open('inscricoes.dat','a')
    escritor.write(matricula + ';' + nome + ';' + email + '\n')
    escritor.close()
    escritor = open('entrada.dat','a')
    escritor.write(matricula + '\n')
    escritor.close()
    if saida:
        escritor = open('saida.dat','a')
        escritor.write(matricula + '\n')
        escritor.close()
        print('Entrada e saída registrada com sucesso!')
        return
    print('Entrada registrada com sucesso!')

def entrada(lista):
    matricula = input('Informe matrícula: ')
    if matricula not in lista:
        print('Esta matrícula não está cadastrada.')
        op = input('Deseja realizar inscrição? (S/N)\n').lower()
        if op == 's':
            entrada_saida(lista,matricula,False)
        else:
            pass
    else:
        escritor = open('entrada.dat','a')
        escritor.write(matricula + '\n')
        escritor.close()
        print('Entrada registrada com sucesso!')

def saida(lista):
    matricula = input('Informe matrícula: ')
    if matricula not in lista:
        print('Esta matrícula não está cadastrada.')
        op = input('Deseja realizar inscrição? (S/N)\n').lower()
        if op == 's':
            entrada_saida(lista,matricula,True)
        else:
            pass
    else:
        escritor = open('saida.dat','a')
        escritor.write(matricula + '\n')
        escritor.close()
        print('Saída registrada com sucesso!')