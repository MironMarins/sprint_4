import datetime as dt
import oracledb
import cadastra
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'

hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')
#print(dataHora)
#vei = cadastra.carga(placa='4678',data=dataHora)


def create(carga):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_veiculo_carga (cd_placa, nr_peso, nr_comprimento, nr_altura, nr_largura, nr_eixos, ds_tipo, dt_cadastro, id_carga, cd_carga)
                VALUES (:placa, :peso, :comprimento, :altura, :largura, :eixos, :CargaTipo, to_date(:data, 'DD/MM/YYYY HH24:MI'),seq_cargavei.nextval,:codigo) """
                cur.execute(sql, carga)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao cadastrar sua carga.")
        raise error




def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error



def find_one_by_placa(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error

#print(find_one_by_id('1234-rm'))
def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga WHERE id_carga = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error
def find_one_by_codigo(codigo):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_veiculo_carga WHERE cd_carga = :codigo'
                cur.execute(sql, { 'codigo': codigo })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro ao consultar sua carga")
        raise error

def update(carga, placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
                                         
            with con.cursor() as cur:   
                sql = """UPDATE t_porto_veiculo_carga SET nr_peso=:peso, nr_comprimento=:comprimento, nr_altura=:altura, nr_largura=:largura,
                  nr_eixos=:eixos, ds_tipo=:CargaTipo,dt_cadastro=:data WHERE cd_placa = :placa"""
                cur.execute(sql, { **carga, 'placa': placa })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar sua carga.")
        raise erro

#placa = str(input("digite o a placa do veiculo que cujas informação deseja alterar?"))
#placa = '1234-rm'
#carga = find_one_by_id('1234-rm')
#peso = carga[1]
#comprimento = carga[2]
#largura = carga[4]
#altura = carga[3]
#eixos = carga[5]
#tipo = carga[6]
#data = dataHora


def suaCarga(carga):
    print("Qual informação gostaria de alterar? ")
    print("[1] peso: ",carga[1])
    print("[2] comprimento: ",carga[2])
    print("[3] altura: ",carga[3])
    print("[4] largura: ",carga[4])
    print("[5] eixos: ",carga[5])
    print("[6] cargaTipo: ",carga[6])
    
    

#print(suaCarga(carga))

#escolha = int(input("qual informação quer alterar"))
#if escolha ==1:
    #peso = float(input("qual o novo peos?"))
#elif escolha ==2:
    #comprimento = float(input("qual o novo comprimento?"))
#elif escolha ==4:
    #largura = float(input("qual a nova largura?"))
#elif escolha ==3:
    #altura = float(input("qual a nova altura?"))
#elif escolha ==5:
    #eixos = int(input("quantos eixos?"))
#elif escolha ==6:
    #tipo = str(input("qual o novo tipo?"))
#carg = cadastra.suaCarga(peso=peso,comprimento=comprimento,largura=largura,altura=altura,eixos=eixos,placa=placa,tipo=tipo,data=dataHora)
#update(carg,placa)

def delete(placa):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_veiculo_carga WHERE cd_placa = :placa'
                cur.execute(sql, { 'placa': placa })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar sua carga.")
        raise erro

#delete(placa)

