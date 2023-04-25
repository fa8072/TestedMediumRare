import psycopg

from .Database_config import host, user, password, db_name

try:
    # Подключение к существующей базе
    connection = psycopg.connect(f"host={host} user={user} password={password} dbname={db_name}")

except Exception as _ex:
    print("[INFO] Error while working with PostgreSQL", _ex)


