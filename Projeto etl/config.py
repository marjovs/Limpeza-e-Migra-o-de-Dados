from pydantic_settings import BaseSettings, SettingsConfigDict

class Config(BaseSettings):
    # Supabase
    pg_host: str
    pg_user: str
    pg_password: str
    pg_port: int
    pg_db: str
    pg_table: str = "raw_clients"

    # MySQL
    mysql_host: str
    mysql_user: str
    mysql_password: str
    mysql_port: int
    mysql_db: str
    mysql_table: str = "clients_clean"

    model_config = SettingsConfigDict(env_file=".env")

    @property
    def postgres_url(self):
        return f"postgresql+psycopg2://{self.pg_user}:{self.pg_password}@{self.pg_host}:{self.pg_port}/{self.pg_db}"

    @property
    def mysql_url(self):
        return f"mysql+pymysql://{self.mysql_user}:{self.mysql_password}@{self.mysql_host}:{self.mysql_port}/{self.mysql_db}"

config = Config()