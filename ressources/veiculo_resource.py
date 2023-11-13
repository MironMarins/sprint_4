import datetime as dt
import oracledb
#import cadastra
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')
#vei = cadastra.cadastraV(1)


def create(veiculo):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_veiculo_cliente (id_veiculo, id_cliente, nr_peso, nr_comprimento, nr_largura, nr_altura, nr_eixos, cd_placa, ds_marca,dt_cadastro)
                VALUES (seq_veiculocli.nextval, :CodigoCliente, :peso, :comprimento, :largura, :altura, :eixos, :placa, :marca, to_date(:data, 'DD/MM/YYYY HH24:MI')) """
                cur.execute(sql, veiculo)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao cadastrar seu veiculo .")
        raise error

#create(vei)



def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_cliente'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error



def find_one_by_placa(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_cliente WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar seu veiculo")
        raise error

def find_one_by_idVeiculo(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_cliente WHERE id_veiculo = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao seu veiculo")
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



#print(seuVeiculo(veiculo))

#escolha = int(input("qual informação quer alterar"))
#if escolha ==1:
    #peso = float(input("qual o novo peso?"))
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
    #marca = str(input("qual a nova marca?"))
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

