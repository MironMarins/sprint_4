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
tuplaP = find_all_problemas()
for i in range(len(tuplaP)):
    print("["+str(tuplaP[i][0])+"] "+ str(tuplaP[i][1]))

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
tuplaE = find_all_especificacao()
for i in range(len(tuplaE)):
    print("["+str(tuplaE[i][0])+"] "+ str(tuplaE[i][1]))