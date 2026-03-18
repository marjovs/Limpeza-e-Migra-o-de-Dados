from db import get_mysql_engine
from config import config

def load_data(df):
    engine = get_mysql_engine()
    df.to_sql(config.mysql_table, con=engine, if_exists="replace", index=False)
    print(f"Dados carregados na tabela {config.mysql_table} do MySQL")