import datetime as dt
import oracledb
user='rm551801'
password='040591'
dsn='oracle.fiap.com.br/orcl'

def find_all_problemas():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_problema'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro")
        raise error
#tuplaP = find_all_problemas()
#for i in range(len(tuplaP)):
    #print("["+str(tuplaP[i][0])+"] "+ str(tuplaP[i][1]))

def find_one_by_id_problema(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_problema WHERE id_problema = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao tipo de erro")
        raise error


def find_all_especificacao():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_especificacao'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro")
        raise error
#tuplaE = find_all_especificacao()
#for i in range(len(tuplaE)):
    #print("["+str(tuplaE[i][0])+"] "+ str(tuplaE[i][1]))

def find_one_by_id_especificacao(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_especificacao WHERE id_especicacao = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao tipo de especificacao")
        raise error



def find_all_auxilio():
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_auxilio'
                cur.execute(sql)
                return cur.fetchall()
            
    except Exception as error:
        print("Ocorreu um erro")
        raise error
#tuplaE = find_all_especificacao()
#for i in range(len(tuplaE)):
    #print("["+str(tuplaE[i][0])+"] "+ str(tuplaE[i][1]))

def find_one_by_id_auxilio(id):
    try:
        with oracledb.connect(user=user, password=password, dsn=dsn) as con:
            with con.cursor() as cur:
                sql = 'SELECT * FROM t_porto_auxilio WHERE id_auxilio = :id'
                cur.execute(sql, { 'id': id })
                resp = cur.fetchall()

                if len(resp) == 0:
                    return None
                else:
                    return resp[0]
            
    except Exception as error:
        print("Ocorreu um erro na consulta ao tipo de especificacao")
        raise error