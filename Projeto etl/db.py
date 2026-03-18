from sqlalchemy import create_engine
from sqlalchemy.exc import SQLAlchemyError
from config import config

def get_postgres_engine():
    try:
        engine = create_engine(config.postgres_url)
        print("Conexão com PostgreSQL criada com sucesso!")
        return engine
    except SQLAlchemyError as e:
        print("Erro ao se conectar com PostgreSQL:", e)
        raise

def get_mysql_engine():
    try:
        engine = create_engine(config.mysql_url)
        print("Conexão com MySQL criada com sucesso!")
        return engine
    except SQLAlchemyError as e:
        print("Erro ao se conectar com MySQL:", e)
        raise