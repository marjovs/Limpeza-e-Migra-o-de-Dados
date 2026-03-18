from sqlalchemy import text

def generate_report(engine, table_name, total, validos, descartados, motivos):
    with engine.connect() as conn:
        result = conn.execute(text(f"SELECT COUNT(*) FROM {table_name}"))
        count_in_db = result.scalar()

    print("\nRELATÓRIO FINAL DO ETL")
    print(f"Registros extraídos: {total}")
    print(f"Registros válidos processados: {validos}")
    print(f"Registros carregados no banco: {count_in_db}")
    print(f"Registros descartados: {descartados}\n")

    print("Motivos de descarte:")
    for k, v in motivos.items():
        print(f"- {k}: {v}")