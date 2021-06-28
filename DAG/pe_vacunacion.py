import pandas as pd
import urllib
import sqlite3
from sqlalchemy.orm import sessionmaker
import sqlalchemy
import os
import requests


def run_vaccination_etl():
    database_location = 'sqlite:///pe_vaccination.sqlite'

    engine = sqlalchemy.create_engine(database_location)
    con = sqlite3.connect('pe_vaccination.sqlite')
    cur = con.cursor()

    url = 'https://www.datosabiertos.gob.pe/sites/default/files/_Muestra.xlsx'
    urllib.request.urlretrieve(url, 'vac_data.xlsx')
    vacc_df = pd.read_excel('vac_data.xlsx')
    ids = []
    for i in range(len(vacc_df.index)):
        ids.append(i)
    vacc_df['ID'] = ids
    

    sql_query = """
    CREATE TABLE IF NOT EXISTS pe_vaccination(
        GRUPO_RIESGO VARCHAR(200),
        EDAD VARCHAR(200),
        SEXO VARCHAR(200),
        FECHA_VACUNACION VARCHAR(200),
        DOSIS VARCHAR(200),
        FABRICANTE VARCHAR(200),
        DIRESA VARCHAR(200),
        DEPARTAMENTO VARCHAR(200),
        PROVINCIA VARCHAR(200),
        DISTRITO VARCHAR(200),
        ID VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (ID)
    )
    """


    cur.execute(sql_query)
    print("Opened database successfully")
    try:
        vacc_df.to_sql("pe_vaccination", engine, index=False, if_exists='append')
    except:
        print("Data already exists in db")
    con.close()
    print('Closed database')
    os.remove("vac_data.xlsx")

if __name__ == '__main__':
    run_vaccination_etl()
