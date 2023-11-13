
import oracledb
import datetime as dt

user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'
hoje = dt.datetime.now()
dataHora = hoje.strftime('%d/%m/%Y %H:%M')

# função responçavel por receber um as informações de uma 
# dicionario e usar essas informações para montar uma linha na tabela
#  t_porto_cliente

def create(cliente):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_cliente (id_cliente, nm_cliente, nr_cpf, dt_cadastro, cd_cliente)
                VALUES (seq_cliente.nextval, :nome, :cpf, to_date(:data, 'DD/MM/YYYY HH24:MI'), :id)
                """
                cur.execute(sql, cliente)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao realizar seu cadastro.")
        raise error

#função que trará uma lista de tuplas referente a tabela t_porto_cliente

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


#função que trará uma tupla referente a uma linha da tabela t_porto_cliente, ulizando
# o codigo de cliente providenciado por essa aplicação, que será correspondente 
# a "cd_cliente"

def find_one_by_codigo(id):
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
#função que trará uma tupla referente a uma linha da tabela t_porto_cliente, ulizando
# o id de cliente que será correspondente a "id_cliente"
def find_one_by_id(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_cliente WHERE id_cliente = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao seu cadastro")
        raise error

print(find_one_by_id(4))

#função responsavel por alterar informações na tabela t_porto_cliente
#ela recebera o codigo correspondente a cd_cliente e um dicionario com novas informações 
#que substituiram as informações correspondentes a mesma linha da informação cd_cliente
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

#função reponsalvel por deletar uma linha da tabela t_porto_cliente correspondente ao 
# codigo de um cliente "correspondente a "cd_cliente"

def delete(codigo):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_cliente WHERE cd_cliente = :codigo'
                cur.execute(sql, { 'codigo': codigo })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar seu cadastro.")
        raise erro



