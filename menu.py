def menu():
   
    print("1 - gostaria de realizar meu cadastro")
    print("2 - gostaria de cadastrar um veiculo em minha conta")
    print("3 - gostaria de alterar uma informação")
    print("4 - gostaria de consultar meus dados")
    print("5 - solicitação de modal")
    print("6 - gostaria de deletar minhas informações")
    print("7 - sair")
    return int(input('escolha: '))

def seuVeiculo(veiculo):
    print("Qual informação gostaria de alterar? ")
    print("[1] peso: ",veiculo[2])
    print("[2] comprimento: ",veiculo[3])
    print("[3] largura: ",veiculo[4])
    print("[4] altura: ",veiculo[5])
    print("[5] eixos: ",veiculo[6])
    print("[6] placa: ",veiculo[7])
    print("[7] marca: ",veiculo[8])