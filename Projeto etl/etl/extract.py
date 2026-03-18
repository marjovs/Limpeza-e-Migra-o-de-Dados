import pandas as pd
from db import get_postgres_engine
from config import config

def extract_data():
    engine = get_postgres_engine()
    query = f"SELECT * FROM {config.pg_table}"
    df = pd.read_sql(query, engine)
    print(f"{len(df)} registros extraídos do Supabase")
    return df