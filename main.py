import datetime as dt
import menu
import cadastra
import altera
import auxilio
import codigo
import ressources.cliente_resource as cliente_resource
import ressources.veiculo_resource as veiculo_resource
escolha = 0
print("Seja bem vindo ao S.O.SPorto")
print("Em que podemos ajuda-lo?")
opcao = 0
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')

while escolha != 7 or opcao == "inicio":
    
    
    escolha = menu.menu() # chama a função menu criado na pasta menu.py
    
    if escolha == 1: #referente a opção "gostaria de realizar meu cadatro"
        print("=-"*10)
        print("por favor preencha as informações solicitadas: ")
        id = codigo.ids()
        cli = cadastra.cadastraCliente(data=dataHora,id=id) # chama a função cadastraV na pasta cadastraV 
        cliente_resource.create(cli) # adicionará os dados do cliente no banco de dados
        print("=-"*10)
        print("Agora preencha as informações do seu primeiro veiculo: ")
        idcliente = cliente_resource.find_one_by_id(id=id)
        idcliente=idcliente[0]
        
        veiculo = cadastra.cadastraV(id=idcliente,data=dataHora)
        veiculo_resource.create(veiculo)
        print(cli)
        print("=-"*10)
        print("por favor anote o numero de seu  cadastro")
        print(id) # o id dado pelo programa é muito inportante para a ulização das funcionalidades do programa 
        print("obrigado por se cadastrar!!!")
        print("=-"*10)
        
        
        opcao = "inicio"
    elif escolha == 2: # referente a opção "gostaria de cadastrar um veiculo a minha conta"
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        opcao = "checar"
        while opcao == "checar":
            listadados =cliente_resource.find_all()
            print(listadados)
            id = input("seu ID de cadastro: ")
                                            
            print("=-"*10)
            idcliente = cliente_resource.find_one_by_id(id=id)# realizará uma busca pelo id apenas se o id estiver na lista "listaIdCliente"
            if idcliente == None: # o cliente poderá decidir se quer voltar para o inicio ou tentar repetir a operação de inserir seu codigo
                print('esse codigo não consta em nosso banco de dados')
                print('gostaria de tentar mais uma vez?')
                print('[1] Sim')
                print('[2] Não')
                opcao = int(input())        
            
                if opcao == 2:
                        input("aperte [enter] para ser enviado para o inicio")
                        opcao = "inicio"
                elif opcao == 1:
                        opcao = "checar"
            
            else: 
                 idcliente=idcliente[0]
                 veiculo = cadastra.cadastraV(id=idcliente,data=dataHora) # cliente poderá colocar as informações do novo veiculo que quiser adicionar
                 veiculo_resource.create(veiculo)
                 print("veiculo adicionado com sucesso!")
                 print(veiculo_resource.find_one_by_placa(veiculo['placa']))
                 print("=-"*10)
                 opcao = "inicio"
            
                
                
    elif escolha == 3: # referente a opção "gostaria de alterar uma informação"
        print("por favor preencha as informações a seguir: ")
        print("=-"*10)
        opcao = "altera"
        while opcao == "altera": #valor qualquer para entrar no looping while
            listadados =cliente_resource.find_all()
            print(listadados)
            id = str(input("seu ID de cadastro: ")) 
            print("=-"*10)
            idcliente = cliente_resource.find_one_by_id(id=id)# realizará uma busca pelo id apenas se o id estiver na lista "listaIdCliente"
            if idcliente == None: # o cliente poderá decidir se quer voltar para o inicio ou tentar repetir a operação de inserir seu codigo
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
            else:
                 opcao = "alteraVeiculo" #valor qualquer para entrar no looping while
                 while opcao == "alteraVeiculo":
                       placa = str(input("por favor incira a placa do veiculo que gostaria de alterar: "))
                       veiculo = veiculo_resource.find_one_by_placa(str(placa))
                       if veiculo == None: # realizará uma busca pela placa, apenas se o numero da placa estiver na lista "listaPlacas"
                            print('essa placa não consta em nosso banco de dados')
                            print('gostaria de tentar mais uma vez?')
                            print('[1] Sim')
                            print('[2] Não')
                            opcao = int(input())
                            if opcao == 2:
                                input("aperte [enter] para ser enviado para o inicio")
                                opcao = "inicio"
                            elif opcao == 1:
                                 opcao = "alteraVeiculo"
                            
                       else:
                              
                            menu.seuVeiculo(veiculo=veiculo)
                            print(veiculo)   
                            print("=-"*10)
                            veiculo = veiculo_resource.find_one_by_placa(placa=placa)
                            idveiculo = veiculo[0]
                            id = veiculo[1]
                            peso = veiculo[2]
                            comprimento = veiculo[3]
                            largura = veiculo[4]
                            altura = veiculo[5]
                            eixos = veiculo[6]
                            placa = veiculo[7]
                            marca = veiculo[8]
                            data = veiculo[9]

                            print(menu.seuVeiculo(veiculo))
                            escolha = int(input("qual informação deseja alterar?"))
                            if escolha ==1:
                                    peso = float(input("qual o novo peso?"))
                            elif escolha ==2:
                                    comprimento = float(input("qual o novo comprimento?"))
                            elif escolha ==3:
                                        largura = float(input("qual a nova largura?"))
                            elif escolha ==4:
                                    altura = float(input("qual a nova altura?"))
                            elif escolha ==5:
                                    eixos = int(input("quantos eixos?"))
                            elif escolha ==6:
                                    placa = str(input("qual a nova plana?"))
                            elif escolha ==7:
                                    marca = str(input("qual a nova marca?"))
                            vei = cadastra.seuVeiculo(idveiculo=idveiculo,id=id,peso=peso,comprimento=peso,largura=largura,altura=altura,eixos=eixos,placa=placa,marca=marca,data=data)
                            veiculo_resource.update(vei,placa)                                        
                            print(veiculo)
                            print("informação alterada com sucesso!!")
                            print("=-"*10)
                            opcao = "inicio"
                 
    elif escolha == 4: #consulta referente a opção "gostaria de consultar meus dados" da função "menu" em "menu.py" 
        opcao = 'consulta'
        while opcao =='consulta':
              id = str(input("por favor digite seu codigo de usuario"))
              tuplacliente = cliente_resource.find_one_by_id(id=id)# realizará uma busca pelo id apenas se o id estiver na lista "listaIdCliente"
              if tuplacliente == None: # o cliente poderá decidir se quer voltar para o inicio ou tentar repetir a operação de inserir seu codigo
                 print('esse codigo não consta em nosso banco de dados')
                 print('gostaria de tentar mais uma vez?')
                 print('[1] Sim')
                 print('[2] Não')
                 opcao = int(input())        
            
                 if opcao == 2:
                    input("aperte [enter] para ser enviado para o inicio")
                    opcao = "sair"# valor qualquer para sair do looping while
              
                 elif opcao == 1:
                    opcao = "consulta"
              else:
                   print("suas informções de cadastro são:")
                   print('id:', tuplacliente[0])
                   print('nome:', tuplacliente[1])
                   print('cpf:', tuplacliente[2])
                   print('data de cadastro:', tuplacliente[3])
                   print('codigo de cliente:', tuplacliente[4])
                   print("=-"*10)
                   print("gostaria de ver as informações de um veiculo especifico?")
                   print("[1] sim")
                   print("[2] não")
                   opcao = int(input())
        if opcao == 1:
             placa = str(input("for favor nos informe a placa desse veiculo: "))
             veiculo_consulta=veiculo_resource.find_one_by_placa(placa=placa)
             print("suas informções de cadastro são:")
             print('id_veiculo:', veiculo_consulta[0])
             print('id_cliente:', veiculo_consulta[1])
             print('peso:', veiculo_consulta[2])
             print('comprimento:', veiculo_consulta[3])
             print('largura:', veiculo_consulta[4])
             print('altura:', veiculo_consulta[5])
             print('eixos:', veiculo_consulta[6])
             print('placa:', veiculo_consulta[7])
             print('marca:', veiculo_consulta[8])
             print('data de cadastro do veiculo:', veiculo_consulta[9])
##############################################################################################################################################################################################
        elif opcao == 2:     
             opcao == "inicio"
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
            opcao = 'deletar'
            while opcao == 'deletar':
                idCliente = str(input('Por favor informe seu id de cadastro: ')) 
                cliente=cliente_resource.find_one_by_id(id=idCliente)
                print(cliente)
                if cliente == None:
                    print("seu codigo não foi encontrado gostaria de tentar de novo?")
                    print("[1] sim")
                    print("[2] não")
                    opcao = int(input())
                    if opcao == 1:
                        opcao = 'deletar'
                    else:
                         opcao = "inicio"
                else:
                    cliente_resource.delete(id=idCliente)
                    print("aperte [enter] para ser enviado para o menu inicial")
                    opcao = input ("seu cadastro foi apagado com sucesso")
                    opcao = "inicio"
                    print("=-"*10)
        elif opcao == 2:
             opcao = 'deletarCarro'
             while opcao == 'deletarCarro':
                   placa = str(input('Por favor o numero de sua placa do carro que deseja deletar de sua conta: '))
                   meuCarro = veiculo_resource.find_one_by_placa(placa=placa)
                   print(meuCarro)
                   if meuCarro == None: # o id é encontrado 
                      print("a placa de seu carro não foi encontrada em nosso banco de dados")
                      print("gostaria de tentar realizar essa operação novamente?")
                      print("[1] sim")
                      print("[2] não")
                      opcao = int(input())
                      if opcao == 1:
                         opcao = 'deletarCarro'
                      else:
                          opcao = "inicio"
                   else:
                        
                        veiculo_resource.delete(placa=placa)
                        print("seu cadastro foi apagado com sucesso")
                        opcao = input ("aperte [enter] para ser enviado para o menu inicial")
                        opcao = "inicio"
                        print("=-"*10)
                        
       
    elif escolha == 7:
         print("Obrigado por utilizar nosso aplicativo")
    else:
        print("Escolha invalida!!")
    
    

    



