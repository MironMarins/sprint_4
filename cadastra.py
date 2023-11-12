import datetime as dt


def cadastraV(id,data):
    
    V = {}
    
    V['CodigoCliente'] = id
    
    placa = str(input('Por favor nos Informe numero da placa de seu veiculo: '))
    V['placa'] = placa

    aux = str(input("Qual marca de seu veiculo: "))
    V['marca'] = aux

    aux = float(input("Quanto seu veiculo pesa em toneladas (0.0): "))
    V['peso'] = aux

    aux = float(input("Quanto seu veiculo mede em comprimento em metros(0.0): "))
    V['comprimento'] = aux

    aux = float(input("Qual a largura de seu veiculo em metros (0.0): "))
    V['largura'] = aux

    aux = float(input("Qual a altura de seu veiculo em metros (0.0): "))
    V['altura'] = aux

    aux = int(input("por ultimo, quantos eixos seu veiculo possui: "))
    V['eixos'] = aux
    
    V['data'] = data

    return V
def seuVeiculo(idveiculo,id,placa,marca,peso,comprimento,largura,altura,eixos,data):
    V = {}
    V['idveiculo'] = idveiculo
    V['id'] = id
    V['placa'] = placa
    V['marca'] = marca
    V['peso'] = peso
    V['comprimento'] = comprimento
    V['largura'] = largura
    V['altura'] = altura
    V['eixos'] = eixos
    V['data'] = data
    return V


def cadastraCliente(data,id):
    
    cliente = {}
    cliente['id'] = id
    
    aux = str(input("informe seu nome completo: "))
    cliente['nome'] = aux

    aux = str(input("informe seu CPF: "))
    cliente['cpf'] = aux

    cliente['data'] = data

    
    #veiculos.append(cadastraV())
    #cliente['veiculos'] = veiculos
    #idCliente = cliente['id']
    #listaIdCliente.append(idCliente)
    return cliente

def seuCadastro(id,nome,cpf,data):
    cli = {}
    cli['CodigoCliente'] = id
    cli['nome'] = nome
    cli['cpf'] = cpf
    cli['data'] = data
    return cli

def carga(placa,data):
      
    Carga = {} 
    
    Carga['placa'] = placa

    aux = float(input("Quanto sua carga pesa em toneladas (0.0): "))
    Carga['peso'] = aux

    aux = float(input("Quanto sua carga mede em comprimento em metros(0.0): "))
    Carga['comprimento'] = aux

    aux = float(input("Qual a altura de sua carga em metros (0.0): "))
    Carga['altura'] = aux

    aux = float(input("Qual a largura de sua carga em metros (0.0): "))
    Carga['largura'] = aux

    aux = int(input("quantos eixos sua carga possui: "))
    Carga['eixos'] = aux

    aux = str(input("por ultimo, qual o tipo de carga externa que seu veiculo esta carregando: "))
    Carga['CargaTipo'] = aux
    
    Carga['data'] = data
       
    return Carga

def suaCarga(placa,peso,comprimento,largura,altura,eixos,tipo,data):
    V = {}
    V['placa'] = placa
    V['peso'] = peso
    V['comprimento'] = comprimento
    V['altura'] = altura
    V['largura'] = largura
    V['eixos'] = eixos
    V['CargaTipo'] = tipo
    V['data'] = data
    return V




