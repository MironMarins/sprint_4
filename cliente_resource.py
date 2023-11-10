import oracledb
import cadastra
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'

#cli = cadastra.cadastraCliente()


def create(cliente):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = """
                INSERT INTO t_porto_cliente (id_cliente, nm_cliente, nr_cpf)
                VALUES (:id, :nome, :cpf)
                """
                cur.execute(sql, cliente)
            
            con.commit()

    except Exception as error:
        print("Ocorreu um erro ao cadastrar o livro.")
        raise error




def find_all():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_cliente'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro ao consultar os livros")
        raise error




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
        print("Ocorreu um erro ao consultar os livros")
        raise error




def update(cliente, id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
                                         
            with con.cursor() as cur:
                sql = """UPDATE t_porto_cliente SET nm_cliente=:nome, nr_cpf=:cpf WHERE id_cliente = :id"""
                cur.execute(sql, { **cliente, 'id': id })
            
            con.commit()

    except Exception as erro:
        print("Ocorreu um erro ao atualizar o livro.")
        raise erro

#iden = int(input("qual id quer alterar?"))

#cliente = find_one_by_id(iden)
#nome = cliente[1]
#cpf = cliente[2]
#print("[1] nome: ",nome)
#print("[2] cpf: ", cpf)

#escolha = int(input("qual informação quer alterar"))
#if escolha ==1:
    #nome = str(input("qual o novo nome?"))
#else:
    #cpf = int(input("qual o novo nome?"))

#update(cli,2)

def delete(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:

            with con.cursor() as cur:
                sql = 'DELETE FROM t_porto_cliente WHERE id_cliente = :id'
                cur.execute(sql, { 'id': id })
                affected_rows = cur.rowcount
            con.commit()
            return  affected_rows

    except Exception as erro:
        print("Ocorreu um erro ao deletar o livro.")
        raise erro

delete(2)

