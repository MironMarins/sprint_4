import datetime as dt
import oracledb
#import cadastra
#import auxilio
#import codigo
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')
#cham = auxilio.resumoChamada(idProblema=1,idAuxilio=1,idCliente=1,idCarga=1,idEspecificacao=1,idVeiculo=1,data=dataHora, idCodigo=codigo.ids())


def create(chamada):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_chamada (id_chamada, id_problema, id_cliente, id_auxilio, id_veiculo, id_especificacao, id_carga, dt_chamada, cd_chamada)
                VALUES (seq_id2.nextval, :idProblema, :idCliente, :idAuxilio, :idVeiculo, :idEspecificacao, :idCarga, to_date(:dtChamada, 'DD/MM/YYYY HH24:MI'), :idCodigo) """
                cur.execute(sql, chamada)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao realizar sua chamada.")
        raise error

#create(cham)



def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_chamada'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error



def find_one_by_codigo(chamada):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_chamada WHERE cd_chamada = :chamada'
                cur.execute(sql, { 'chamada': chamada })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error

def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_chamada WHERE id_chamada = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error


def update(veiculo, placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
                                         
            with con.cursor() as cur:
                sql = """UPDATE t_porto_veiculo_cliente SET id_veiculo=:idveiculo, id_cliente=:id, nr_peso=:peso, nr_comprimento=:comprimento,
                  nr_largura=:largura, nr_altura=:altura, nr_eixos=:eixos, ds_marca=:marca,dt_cadastro=:data WHERE cd_placa = :placa"""
                cur.execute(sql, { **veiculo, 'placa': placa })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar seu veiculo.")
        raise erro

#placa = str(input("digite o a placa do veiculo que cujas informação deseja alterar?"))

#veiculo = find_one_by_id('456-fsdf')
#idveiculo = veiculo[0]
#id = veiculo[1]
#peso = veiculo[2]
#comprimento = veiculo[3]
#largura = veiculo[4]
#altura = veiculo[5]
#eixos = veiculo[6]
#placa = veiculo[7]
#marca = veiculo[8]
#data = dataHora

def seuVeiculo(veiculo):
    print("Qual informação gostaria de alterar? ")
    print("[1] peso: ",veiculo[2])
    print("[2] comprimento: ",veiculo[3])
    print("[3] largura: ",veiculo[4])
    print("[4] altura: ",veiculo[5])
    print("[5] eixos: ",veiculo[6])
    print("[6] placa: ",veiculo[7])
    print("[7] marca: ",veiculo[8])

#print(seuVeiculo(veiculo))

#escolha = int(input("qual informação quer alterar"))
#if escolha ==1:
    #peso = float(input("qual o novo peos?"))
#elif escolha ==2:
    #comprimento = float(input("qual o novo comprimento?"))
#elif escolha ==3:
    #largura = float(input("qual a nova largura?"))
#elif escolha ==4:
    #altura = float(input("qual a nova altura?"))
#elif escolha ==5:
    #eixos = int(input("quantos eixos?"))
#elif escolha ==6:
    #placa = str(input("qual a nova plana?"))
#elif escolha ==7:
    #marca = str(input("qual o nova marca?"))
#vei = cadastra.seuVeiculo(idveiculo=idveiculo,id=id,peso=peso,comprimento=peso,largura=largura,altura=altura,eixos=eixos,placa=placa,marca=marca)
#update(vei,placa)

def delete(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_veiculo_cliente WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro

#delete('456-fsdf')

