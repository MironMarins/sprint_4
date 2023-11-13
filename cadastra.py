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



def cadastraCliente(data,id):
    
    cliente = {}
    cliente['id'] = id
    
    aux = str(input("informe seu nome completo: "))
    cliente['nome'] = aux

    aux = str(input("informe seu CPF: "))
    cliente['cpf'] = aux

    cliente['data'] = data

    return cliente



def carga(placa,data,codigo):
      
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
    Carga['codigo'] = codigo   
    return Carga






