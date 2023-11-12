import codigo


def auxilio():
        ajuda = {}
        reboque = {}
        
        reboque['modal1'] = 'Modal leve'
        reboque['modal2'] = 'Modal medio'
        reboque['modal3'] = 'Modal pesado'

        ajuda['moto'] = 'motoboy'
        ajuda['tecnico'] = 'mecanico'
        ajuda['modal'] = reboque
        return ajuda

#teste = auxilio()
#dici = teste['tecnico']
#print(dici)


def problema():
        problema ={}

        problema['1'] = ' O veiculo simplesmente parou no meio da estrada e não anda mais'
        problema['2'] = ' O veiculo estava estacionado e não quer ligar'
        problema['3'] = ' Meu pneu furou/extourou, não tenho step/macaco'
        problema['4'] = ' Ouvi um barulho e agora meu veiculo esta se comportando de maneira estranha'
        problema['5'] = ' Um cheiro estranho'
        problema['6'] = ' Vejo fumaça saindo do meu veiculo'
        return problema

def expecificacao():
        expecificacao = {}
        gasolina = {}
        eletrico = {}
        cheiro = {}
        barulho = {}
        

        gasolina['1'] = ' há gasolina no tanque'
        gasolina['2'] = ' o tanque esta vazio'

        eletrico['1'] = ' O painel esta ligando'
        eletrico['2'] = ' O painel não liga'

        cheiro['1'] = ' cheiro de queimado'
        cheiro['2'] = ' cheiro de gasolina'
               
        barulho['1'] = ' barulho vindo da frente do veiculo'
        barulho['2'] = ' barulho vindo de traz do veiculo'
        barulho['3'] = ' barulho vindo do lado direito'
        barulho['4'] = ' barulho vindo do lado esquerdo'
        barulho['5'] = ' barulho vindo de embaixo do veiculo'
        barulho['6'] = ' barulho vindo de dentro do veiculo'
        
        expecificacao['1'] = gasolina
        expecificacao['2'] = eletrico
        expecificacao['3'] = ' pneu furado'
        expecificacao['4'] = barulho
        expecificacao['5'] = cheiro
        expecificacao['6'] = ' fumaça saindo do meu veiculo'

        return expecificacao

def veiculoTotal(pesoV,pesoC,comprimentoV,comprimentoC,alturaV,alturaC,larguraV,larguraC):
        veiculoTotal = {}
        
        pesoTotal = pesoV + pesoC
        comprimentoTotal = comprimentoC + comprimentoV

        if alturaC < alturaV:
            alturaTotal = alturaV
        else:
            alturaTotal = alturaC
        if larguraC < larguraV:
            larguraTotal = larguraV
        else:
            larguraTotal = larguraC
        veiculoTotal['pesoTotal'] = pesoTotal
        veiculoTotal['comprimentoTotal'] = comprimentoTotal
        veiculoTotal['alturaTotal'] = alturaTotal
        veiculoTotal['larguraTotal'] = larguraTotal

        return veiculoTotal
def escolhaModal(pesoTotal,dic_modal):
    
    
    if pesoTotal < 5.0:
          modalT = dic_modal['modal1'] 
    elif pesoTotal >= 5.0 and pesoTotal <15.0:
          modalT = dic_modal['modal2']
    else:
         modalT = dic_modal['modal3']
    return modalT
          
                
def resumoChamada(idProblema,idCliente,idAuxilio,idVeiculo,idEspecificacao,idCarga,data,idCodigo):
    resumoChamada = {}
        
    resumoChamada['idProblema'] = idProblema
    resumoChamada['idCliente'] = idCliente
    resumoChamada['idAuxilio'] = idAuxilio
    resumoChamada['idVeiculo'] = idVeiculo
    resumoChamada['idEspecificacao'] = idEspecificacao
    resumoChamada['idCarga'] = idCarga
    resumoChamada['dtChamada'] = data
    resumoChamada['idCodigo'] = idCodigo   
    return resumoChamada 



    





                
