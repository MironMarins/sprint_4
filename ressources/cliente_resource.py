#import cadastra
import oracledb
import datetime as dt
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')
#print(dataHora)
#cli = cadastra.cadastraCliente(str(dataHora),'1235')


def create(cliente):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_cliente (id_cliente, nm_cliente, nr_cpf, dt_cadastro, cd_cliente)
                VALUES (seq_id.nextval, :nome, :cpf, to_date(:data, 'DD/MM/YYYY HH24:MI'), :id)
                """
                cur.execute(sql, cliente)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao realizar seu cadastro.")
        raise error

#create(cli)


def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_cliente'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao seu cadastro")
        raise error

#print(find_all())


def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_cliente WHERE cd_cliente = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao seu cadastro")
        raise error

#print(find_one_by_id(34))


def update(cliente, id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
                                         
            with con.cursor() as cur:
                sql = """UPDATE t_porto_cliente SET nm_cliente=:nome, nr_cpf=:cpf,dt_cadastro=:data WHERE cd_cliente = :CodigoCliente"""
                cur.execute(sql, { **cliente, 'CodigoCliente': id })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar seu cadastro.")
        raise erro

#iden = int(input("qual id quer alterar?"))

#cliente = find_one_by_id('1235')
#print(cliente)
#nome = cliente[1]
#cpf = cliente[2]
#data= cliente[3]
#print()
#print("[1] nome: ",nome)
#print("[2] cpf: ", cpf)

#escolha = int(input("qual informação quer alterar"))
#if escolha ==1:
    #nome = str(input("qual o novo nome?"))
#else:
    #cpf = int(input("qual o novo nome?"))
#cli = cadastra.seuCadastro(id='1235',nome=nome,cpf=cpf,data=data)
#print(cli)
#update(cli,'1235')

def delete(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_cliente WHERE cd_cliente = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar seu cadastro.")
        raise erro

#delete('1235')

