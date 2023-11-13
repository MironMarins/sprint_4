import datetime as dt
import oracledb

user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')



def create(chamada):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_chamada (id_chamada, id_problema, id_cliente, id_auxilio, id_veiculo, id_especificacao, id_carga, dt_chamada, cd_chamada)
                VALUES (seq_cham.nextval, :idProblema, :idCliente, :idAuxilio, :idVeiculo, :idEspecificacao, :idCarga, to_date(:dtChamada, 'DD/MM/YYYY HH24:MI'), :idCodigo) """
                cur.execute(sql, chamada)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao realizar sua chamada.")
        raise error




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



def deletePorIdVeiculo(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_chamada WHERE id_veiculo = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro

def deletePorIdCliente(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_chamada WHERE id_cliente = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro
#delete('456-fsdf')

