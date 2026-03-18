from etl.extract import extract_data
from etl.transform import clean_data
from etl.load import load_data
from models.imperative import generate_report
from db import get_mysql_engine
from config import config

def main():
    print("Iniciando pipeline ETL...\n")

    df = extract_data()
    total = len(df)

    df_clean, motivos = clean_data(df)
    validos = len(df_clean)
    descartados = total - validos

    load_data(df_clean)

    engine_mysql = get_mysql_engine()
    generate_report(engine_mysql, config.mysql_table, total, validos, descartados, motivos)

    print("\nPipeline finalizado com sucesso!")

if __name__ == "__main__":
    main()