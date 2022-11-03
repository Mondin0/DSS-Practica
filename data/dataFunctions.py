import sqlite3
import pandas as pd
def conectar():
    con = sqlite3.connect("data/Db.db")
    return con
def juntarDf(con):
    df = pd.read_sql_query("Select * From Vehiculos", con)
    df1 = pd.read_sql_query("Select * From Precios", con)

    dataframe1 = df.merge(df1, left_on='Version', right_on='Version')
    return dataframe1
def desconectar(con):
    con.close()