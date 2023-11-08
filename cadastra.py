import codigo
listaPlacas = []
listaIdCliente =[]
def cadastraV():
    
    V = {}
    placa = str(input('Por favor nos Informe numero da placa de seu veiculo: '))
    V['placa'] = placa

    aux = str(input("Qual marca de seu veiculo: "))
    V['marca'] = aux

    aux = float(input("Quanto seu veiculo pesa em toneladas (0,0): "))
    V['peso'] = aux

    aux = float(input("Quanto seu veiculo mede em comprimento em metros(0,0): "))
    V['comprimento'] = aux

    aux = float(input("Qual a largura de seu veiculo em metros (0,0): "))
    V['largura'] = aux

    aux = float(input("Qual a altura de seu veiculo em metros (0,0): "))
    V['altura'] = aux

    aux = int(input("por ultimo, quantos eixos seu veiculo possui: "))
    V['eixos'] = aux
    listaPlacas.append(placa)
    return V



def cadastraCliente():
    
    veiculos = []
    cliente = {}
    
    cliente['id'] = codigo.ids()
    
    aux = str(input("informe seu nome: "))
    cliente['nome'] = aux

    aux = str(input("informe seu sobrenome: "))
    cliente['sobre_nome'] = aux

    aux = str(input("informe seu CPF: "))
    cliente['cpf'] = aux

    
    veiculos.append(cadastraV())
    cliente['veiculos'] = veiculos
    idCliente = cliente['id']
    listaIdCliente.append(idCliente)
    return cliente

def carga(placa):
      
    Carga = {} 
    
    Carga['placa'] = placa

    aux = str(input("Qual o tipo de carga externa que seu veiculo esta carregando: "))
    Carga['CargaTipo'] = aux

    aux = float(input("Quanto sua carga pesa em toneladas (0,0): "))
    Carga['peso'] = aux

    aux = float(input("Quanto sua carga mede em comprimento em metros(0,0): "))
    Carga['comprimento'] = aux

    aux = float(input("Qual a largura de sua carga em metros (0,0): "))
    Carga['largura'] = aux

    aux = float(input("Qual a altura de sua carga em metros (0,0): "))
    Carga['altura'] = aux

    aux = int(input("por ultimo, quantos eixos sua carga possui: "))
    Carga['eixos'] = aux
    
    return Carga






