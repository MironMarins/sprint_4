import menu
import cadastra
import altera
import auxilio

escolha = 0
print("Seja bem vindo ao S.O.SPorto")
print("Em que podemos ajuda-lo?")
opcao = 0
usuario = []

while escolha != 7 or opcao == "inicio":
    
    
    escolha = menu.menu() # chama a função menu criado na pasta menu.py
    
    if escolha == 1: #referente a opção "gostaria de realizar meu cadatro"
        print("=-"*10)
        print("por favor preencha as informações solicitadas: ")
        cli = cadastra.cadastraCliente() # chama a função cadastraV na pasta cadastraV 
        print("=-"*10)
        print(cli)
        usuario.append(cli) # adicionará o dicionario cli para a lista usuario
        print("=-"*10)
        print("por favor anote seu codigo de cadastro")
        print(cli["id"]) # o id dado pelo programa é muito inportante para a ulização das funcionalidades do programa 
        print("obrigado por se cadastrar!!!")
        print("=-"*10)
        
        
        opcao = "inicio"
    elif escolha == 2: # referente a opção "gostaria de cadastrar um veiculo a minha conta"
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        opcao = "checar"
        while opcao == "checar":
            id = str(input("seu ID de cadastro: "))
        
            if id in cadastra.listaIdCliente:# realizará uma busca pelo id apenas se o id estiver na lista "listaIdCliente"         
                        
                for info in usuario: # cliente poderá colocar as informações do novo veiculo que quiser adicionar
                    if info['id'] == id:
                        idCliente = id
                        print("=-"*10)
                        print(info['veiculos'])
                    
                        cadastraV = cadastra.cadastraV()# chama o dicionario da função cadastraV
                        listaVeiculos = info['veiculos']
                        print(listaVeiculos)
                        listaVeiculos.append(cadastraV)# aciciona o dicionario na lista veiculos do dicionario "cliente"
                        print("veiculo adicionado com sucesso!")
                        print("=-"*10)
                        opcao = "inicio"
            else: # o cliente poderá dicidir se quer voltar para o inicio ou tentar repetir a operação de inserir seu codigo
                print('esse codigo não consta em nosso banco de dados')
                print('gostaria de tentar mais uma vez?')
                print('[1] Sim')
                print('[2] Não')
                opcao = int(input())        
            
                if opcao == 2:
                    input("aperte [enter] para ser enviado para o inicio")
                elif opcao == 1:
                   opcao = "checar"
        
        print(listaVeiculos)
        print(info)
                
    elif escolha == 3: # referente a opção "gostaria de alterar uma informação"
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        opcao = "altera"
        while opcao == "altera": #valor qualquer para entrar no looping while
            id = str(input("seu ID de cadastro: ")) 
            if id in cadastra.listaIdCliente: # realizará uma busca pelo id, apenas se o id estiver na lista "listaIdCliente"
                for info in usuario:
                    if info['id'] == id:
                        idCliente = id
                        print("=-"*10)
                        print(info['veiculos'])
                        listaVeiculos = info['veiculos']
                        print("=-"*10)
                    opcao = "alteraVeiculo" #valor qualquer para entrar no looping while
                    while opcao == "alteraVeiculo":
                        placa = str(input("por favor incira a placa do veiculo que gostaria de alterar: "))
                        if placa in cadastra.listaPlacas: # realizará uma busca pela placa, apenas se o numero da placa estiver na lista "listaPlacas"
                            for veiculo in listaVeiculos:
                                if veiculo['placa'] == placa:
                                    meu_vei = veiculo
                                    for k, v in meu_vei.items():
                                            print(f'{k}={v}')
                            opcao = 'sair' # valor qualquer para sair do looping while   
                            print(veiculo)   
                        else:
                             print('essa placa não consta em nosso banco de dados')
                             print('gostaria de tentar mais uma vez?')
                             print('[1] Sim')
                             print('[2] Não')
                             opcao = int(input())
                             if opcao == 2:
                                input("aperte [enter] para ser enviado para o inicio")
                             elif opcao == 1:
                                  opcao = "alteraVeiculo"
                    print("=-"*10)                                        
                    alteracao = str(input("escreva qual informação gostaria de alterar?")) # pede o nome da chave que quer alterar
                    valor = input("Qual o novo valor dessa alteração?") # pede o novo valor da alteraração
                    valor = altera.alteraV(alteracao=alteracao,valor=valor) # coloca chave e valor na função "alteraV" 
                    veiculo[alteracao] = valor
                    print(veiculo)
                    print("informação alterada com sucesso!!")
                    print("=-"*10)
                    print(info)
                    print(usuario)
                    opcao = "inicio"
        
            else:
                print('esse codigo não consta em nosso banco de dados')
                print('gostaria de tentar mais uma vez?')
                print('[1] Sim')
                print('[2] Não')
                opcao = int(input())        
            
                if opcao == 2:
                    input("aperte [enter] para ser enviado para o inicio")
                    opcao = "sair"# valor qualquer para sair do looping while
                elif opcao == 1:
                   opcao = "altera"   
    elif escolha == 4: #consulta referente a opção "gostaria de consultar meus dados" da função "menu" em "menu.py" 
        desc = input('Informe seu id de usuario: ')
        for info in usuario: #mostra as informações do usuario em forma de coluna
            if info['id'] == desc:
                print("suas informções de cadastro são:")
                for k, v in info.items():
                    print(f'{k}={v}')
        
                
        listaVeiculos = info['veiculos']
        veiculo = 0
        for vei in listaVeiculos: #mostra a lista de veiculos em forma de colunas
            veiculo = veiculo + 1
            print("-=-=-=-=-=-==-=-=-=- veiculo", veiculo,"=-=-=-=-=-=-=-=-=-=-=-=-=-=-") # separa um veiculo de outro
            for k, v in vei.items():
                print(f'{k}={v}')
        print("gostaria de ver o resumo de suas chamadas?" )
        print("[1] Sim")
        print("[2] Não")        
        opcao = int(input())
        if opcao == 2:
             input("aperte [enter] para ser enviado para o meu incial")
        elif opcao == 1:
             print("entrando no banco de dados de chamadas")
             opcao = "chamadas" # valor generico para entra no looping while
             while opcao == "chamadas": 
                    idChamada = str(input("por favor informe o id da chamada que gostaria de verificar: "))
                    listaChamadas = auxilio.chamada
                    
                    if idChamada in auxilio.listaIdChamadas:
                        for info in listaChamadas:# mostrará o resumo da chamas em forma de coluna
                            if info['idChamada'] == idChamada:
                                print("suas informções de cadastro são:")
                                for k, v in info.items():
                                    print(f'{k}={v}')
                        opcao = "sair"        
                           
                    else:
                        print('esse codigo não consta em nosso banco de dados')
                        print('gostaria de tentar mais uma vez?')
                        print('[1] Sim')
                        print('[2] Não')
                        opcao = int(input())
                    if opcao == 2:
                        input("aperte [enter] para ser enviado para o inicio")
                        opcao = "sair" #valor generico para sair do looping while
                    elif opcao == 1:
                        opcao = "chamadas"    
                                           
                    
                    
    elif escolha == 5:
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        id = str(input("seu ID de cadastro: "))
        for info in usuario: # assim que o usuario colocar seu id corretamente 
            if info['id'] == id:
                idCliente = id
                print("=-"*10)
                print(info['veiculos'])
                listaVeiculos = info['veiculos']
                veiculo = 0
                for vei in listaVeiculos: # sua lista de veiculos aparerá em forma de coluna
                    veiculo = veiculo + 1
                    print("-=-=-=-=-=-=-=-=-=-= veiculo", veiculo,"-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                    
                    for k, v in vei.items():
                        print(f'{k}={v}')
                print("=-"*10)
                while opcao !=0:
                    placa = str(input("placa de seu veiculo: ")) # o usuario deve inserir corretamente a placa de seu veiculo   
                    print("=-"*10)
                    opcao = 1
                    for vei in listaVeiculos:
                        if vei['placa'] == placa:
                            placa = vei['placa']
                            print("esse é seu veiculo?")
                            print("[1] Sim") # as opções aparecerão acima do veiculo referente ao codigo da placa incerida
                            print("[2] Não")
                            print("=-"*10)
                            for k, v in vei.items():
                                print(f'{k}={v}')
                            pesoV = vei['peso'] # as informações do veiculo, pesoV, comprimentoV, alturaV e larguraV serão ulizadas para futuramente auxiliarem na escolha de um modal 
                            comprimentoV = vei['comprimento']
                            alturaV = vei['altura']
                            larguraV = vei['largura']
                            
                    opcao = int(input())
                    if opcao == 2:
                        print("por favor, informe a placa de seu veiculo novamente")
                    elif opcao == 1:
                        
                        opcao = 0 
            
        
        print("=-"*10)
        print("nesse momento, seu veiculo esta comportando uma carga externa?") 
        print("[1] Sim")
        print("[2] Não")
        opcao = int(input()) # o usuario deve informar se o veiculo esta comportando alguma carga externa (carreta)
        
        if opcao == 1:
            entradacarga = 1
            print("por favor preencha a descrição da carga conforme e for solicitado")
            print("=-"*10)
            print("verifique se as informações estão corretas: " )
            while entradacarga == 1:
                                
                  carga = cadastra.carga(placa) # função carga será "chamada" em casdatra.py, a placa da carga será a mesma do veiculo
                                                # o usuario deve inserir as informações de sua carga 
                  print("=-"*10)
                  for k, v in carga.items(): # as informações da carga serão checadas e confirmadas pelo usuario
                                print(f'{k}={v}')
                
                  print("[1] correto") 
                  print("[2] incorreto")
                  print("=-"*10)
                  opcao = int(input())
                  if opcao == 2:
                     print("por favor incira as informações novamente")
                     entradacarga = 1
                  elif opcao == 1:# assim que confirmadas as imformações pesoC, comprimentoC, alturaC, larguraC serão guardadas para serem usulizads na escolha de um modal correto
                       pesoC = carga['peso'] 
                       print(pesoC)
                       comprimentoC = carga['comprimento']
                       print(comprimentoC)
                       alturaC = carga['altura']
                       print(alturaC)
                       larguraC = carga['largura']
                       print(larguraC)
                       opcao == 1
                       entradacarga = 0
            veiculoTotal = auxilio.veiculoTotal(pesoV=pesoV,pesoC=pesoC,comprimentoV=comprimentoV,comprimentoC=comprimentoC,alturaV=alturaV,alturaC=alturaC,larguraV=larguraV,larguraC=larguraC)
            opcao = "modal" # pesoV e comprimentoC serão somados com o pesoV e comprimentoV e devolvidos como pesoTotal e comprimentoTotal
                            # a maior altura e largura dentre veiculo e carga serão a alturaTotal e larguraTotal
            print("vt1",veiculoTotal)
        elif opcao == 2:# Caso o veiculo não tenha carga externa o pesoC, alturaC, comprimentoC e larguraC serão todos iguais a 0
                veiculoTotal = auxilio.veiculoTotal(pesoV=pesoV,pesoC=0,comprimentoV=comprimentoV,comprimentoC=0,alturaV=alturaV,alturaC=0,larguraV=larguraV,larguraC=0)
                print("vt2",veiculoTotal) # os atributos de veiculoTotal serão guadados em pesoTotal, ComprimentoTotal, larguraTotal e alturatotal
        pesoTotal = veiculoTotal['pesoTotal']
        print(pesoTotal)
        comprimentoTotal = veiculoTotal['comprimentoTotal']
        print(comprimentoTotal)
        alturaTotal = veiculoTotal['alturaTotal']
        print(alturaTotal)
        larguraTotal = veiculoTotal['larguraTotal']
        print(larguraTotal)
        dic_auxilio = auxilio.auxilio() # o dicionario "auxilio" será chamado da função "auxilio"  em auxilio.py e quardado em dic_auxilio 
        dic_modal = dic_auxilio['modal'] # o dicionario da chave modal no dicionario dic_auxilio será quardado em dic_modal

        modalT = auxilio.escolhaModal(pesoTotal=pesoTotal,dic_modal=dic_modal) # o valor de pesoTotal será usado para escolher o modal correto no dicionario dic_modal
                                                                                #esse modal será guardado em modalT 
        print(modalT)
        print("=-"*10)
        print("por favor digite o numero correspondente ao seu problema")
        problemas = auxilio.problema() # o dicionario "problema" será chamado em auxilio.py
        for k, v in problemas.items(): # o apresentado em forma de coluna, sendo as chaves são numeros de 1 a 6, menu de opções é automaticamente criado
            print(f'{k}={v}')
        opcao = int(input())
        problema = problemas[str(opcao)]
        print(problema)
        
        print("=-"*10)
                        
        especificacao = auxilio.expecificacao() # o dicionario de expecificações será chamado de da função "expecificacao" em auxilio.py 
        
        if opcao == 1: # referente a opção ' O veiculo simplesmente parou no meio da estrada e não anda mais', do dicionario "problema"
                gasolina_dic = especificacao[str(opcao)]
                for k, v in gasolina_dic.items():
                    print(f'{k}={v}')
                opcao = int(input()) # o usuario deve escolher uma opção referente ao dicionario guardado na chave do dicionario especificacao
                
                
                especificacao = gasolina_dic[str(opcao)]
                print(especificacao)
                
                if opcao == 1: #referente a opção ' há gasolina no tanque' do dicionaro "gasolina" na funcao especificacao
                    solucao = modalT #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                    print("entamos enviando um modal", modalT, "para a sua localização" )
                                        
                    
                elif opcao == 2: #referente a opção ' o tanque esta vazio' do dicionaro "gasolina" na funcao especificacao
                    
                    moto = dic_auxilio['moto']
                    solucao = moto #quarda valor moto em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                    print("estamos enviando um", moto, "com gasolina para a sua localização")
        elif opcao == 2: # referente a opção ' O veiculo estava estacionado e não quer ligar', do dicionario "problema"
                eletrico = especificacao['2'] 
                print("o painel esta ascendendo?")
                for k, v in eletrico.items():
                    print(f'{k}={v}')
                opcao = int(input()) # o usuario deve escolher uma opção referente ao dicionario guardado na chave do dicionario especificacao   
                especificacao = eletrico[str(opcao)]
                print(especificacao)    
                if opcao == 1: #referente a opção ' O painel esta ligando' do dicionaro "esletrico" na funcao especificacao
                    solucao = modalT #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                    print("entamos enviando um modal", modalT, "para a sua localização" )
                elif opcao == 2: #referente a opção ' O painel não liga' do dicionaro "esletrico" na funcao especificacao
                    
                     moto = dic_auxilio['moto']
                     solucao = moto #quarda valor moto em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                     print("estamos enviando um", moto, "com material carregar sua bateria, para a sua localização")
        elif opcao == 3:# referente a opção ' Meu pneu furou/extourou, não tenho step/macaco', do dicionario "problema"
                pneu = especificacao['3']
                especificacao = pneu
                print(especificacao)
                tecnico = dic_auxilio['tecnico']
                solucao = tecnico #quarda valor tecnico em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                print("estamos enviando um", tecnico, "com step para a sua localização")

        elif opcao == 4:# referente a opção ' Ouvi um barulho e agora meu veiculo esta se comportando de maneira estranha', do dicionario "problema"
                print("Consegue identificar de onde esta vindo o barulho? ")
                barulho = especificacao['4']
                for k, v in barulho.items():
                    print(f'{k}={v}')
                opcao = str(input()) # como barulho estranho é um problema de dificio averiguação colocamos modal como unica opção de solução
                especificacao = barulho[str(opcao)]
                solucao = modalT #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                print("entamos enviando um modal", modalT, "para a sua localização" )
        elif opcao == 5:# referente a opção ' Um cheiro estranho', do dicionario "problema"
                print("que tipo de cheiro esta sentindo?")
                cheiro = especificacao['5']
                for k, v in cheiro.items():
                    print(f'{k}={v}')
                opcao = str(input()) # # como cheiro de queimado ou gasolina podem estar ambos ligados a um problem serio colocamos modal como unica opção de solução   
                especificacao = cheiro[str(opcao)]
                solucao = modalT #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                print("por precausão, é melhor estacionar o carro")
                print("entamos enviando um modal", modalT, "para a sua localização" )
                print("por precausão, é melhor estacionar o carro")
                
        elif opcao == 6:# referente a opção ' Vejo fumaça saindo do meu veiculo', do dicionario "problema"
                fumaça = especificacao['6']
                especificacao = fumaça 
                solucao = modalT #quarda valor modal em solucao para ser adicionado no dicionario da fuunção "resumoChamadas" em auxilio.py
                print("por precausão, é melhor estacionar o carro") #como a visão de fumaça pode ser um problema seriu no veiculo colocamos o modal como 
                                                                    #solução para esse caso
                print("entamos enviando um modal", modalT, "para a sua localização" )
        resumoChamada = auxilio.resumoChamada(idCliente=idCliente,placa=placa,pesoTotal=pesoTotal,comprimentoTotal=comprimentoTotal,alturaTotal=alturaTotal,larguraTotal=larguraTotal,problemaChamada=problema,especificacao=especificacao,solucao=solucao)
        print("=-"*10) #todsas os valores pertinentes a chamada serão adicionados a função resomuChamad em aucilio.py e serão guardadas no valor variavel resumoChamada
        print('por favor anote o id dessa chamada')
        print(resumoChamada['idChamada']) # mostrará o id da chamada para o usuario
        print("=-"*10)
        print("gostaria de ver o resumo de sua chamada?")
        print("[1] Sim")
        print("[2] Não")
        opcao = int(input())
        if opcao == 1: # mostra dicionario do resumo da chamada em forma de colunas
            print(auxilio.chamada)
            for k, v in resumoChamada.items():
                    print(f'{k}={v}')

            input("aperte [Enter] para ser eviado para o inicio")
            print("-="*10)
            opcao = "inicio"       
        elif opcao == 2:# mostra dicionario do resumo da chamada em forma de colunas leva o usuario para o inicio do programa
            input("aperte enter para ser enviado para o inicio")          
            opcao ="inicio"
    elif escolha == 6: # apaga referente a opção "gostaria de deletar minhas informações" da função "menu" em menu.py
        print("Oque gostaria de deletar?")
        print("[1] Minha Conta")
        print("[2] um veiculo de minha conta")
        opcao = int(input())# o cliente poderá escolher se quer apagar a propria conta por completo ou apenas um um veiculo de sua conta
        if opcao == 1:
            idCliente = str(input('Por favor informe seu id de cadastro: ')) 
            i = 0
            for i in range(len(usuario)):
                cli = usuario[i]
                if cli['id'] == idCliente:
                    usuario.pop(i) # assim que o valor id for encontrado em um dicionario "cliente" da lista "usuario" ele sera apagado
                    break
            print(usuario)
            print("seu cadastro foi apagado com sucesso")
            print("=-"*10)
        elif opcao == 2:
            id = str(input("Por favor informe seu id de cadastro: "))
        for info in usuario: # o id do usuario é buscado
            if info['id'] == id: # o id é encontrado 
                idCliente = id
                print("=-"*10)
                print(info['veiculos'])
                listaVeiculos = info['veiculos']
                veiculo = 0
                for vei in listaVeiculos: # uma lista de veiculos é aberta na forma de colunas
                    veiculo = veiculo + 1 
                    print("=-=-=-=-=-=-=-=-=-=-=-==veiculo", veiculo,"-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=") #separando os veiculos para a melhor visulização
                    
                    for k, v in vei.items():
                        print(f'{k}={v}')
                print("=-"*10)
                while opcao !=0:
                    placa = str(input("placa do seu veiculo que quer deletar: "))#ao que colocar o codigo correto da placa de carro
                    print("=-"*10)
                    opcao = 1
                    N_vei = 0
                    for vei in listaVeiculos:
                        N_vei = N_vei + 1
                        if vei['placa'] == placa: #assim que o veiculo for encontrado
                            meu_vei = N_vei
                            placa = vei['placa']
                            print("esse é seu veiculo?")# uma opção aparecerar confirmando se esse fo o veiculo correto
                            print("[1] Sim")
                            print("[2] Não")
                            print("=-"*10)
                            for k, v in vei.items():
                                print(f'{k}={v}')
                    opcao = int(input())
                    if opcao == 2:
                        print("por favor, informe a placa de seu veiculo novamente") # caso não seja o usuario podera colocar o codigo da placa novamente
                    elif opcao == 1: # assim que a placa do veiculo for confimada pelo usuario o veiculo será apagado da "veiculos", da chave "veiculo", do dicionario cliente
                        # da lista "usuario"
                        
                        print(listaVeiculos)

                        listaVeiculos.pop(meu_vei-1)
                        print("seu veiculo foi deletado com sucesso")
                        print("=-"*10)
                        print(listaVeiculos)
                        opcao = 0 
       
    elif escolha == 7:
         print("Obrigado por utilizar nosso aplicativo")
    else:
        print("Escolha invalida!!")
    
    

    



