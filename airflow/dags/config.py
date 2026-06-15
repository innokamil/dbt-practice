import os 
from pathlib import Path

SQL_PAGILA_FILES_LOCATION: Path = Path(os.getenv("SQL_PAGILA_FILES", ""))
PAGILA_SCHEMA_FILE_URL = "https://raw.githubusercontent.com/devrimgunduz/pagila/refs/heads/master/pagila-schema.sql"
PAGILA_DATA_FILE_URL = "https://raw.githubusercontent.com/devrimgunduz/pagila/refs/heads/master/pagila-insert-data.sql"
PAGILA_SCHEMA_FILE_LOCATION = SQL_PAGILA_FILES_LOCATION.joinpath("pagila-schema.sql")
PAGILA_DATA_FILE_LOCATION = SQL_PAGILA_FILES_LOCATION.joinpath("pagila-data.sql")

SQL_SAKILA_FILES_LOCATION: Path = Path(os.getenv("SQL_SAKILA_FILES", ""))
SAKILA_SCHEMA_FILE_URL = "https://raw.githubusercontent.com/jOOQ/sakila/refs/heads/main/mysql-sakila-db/mysql-sakila-schema.sql"
SAKILA_DATA_FILE_URL = "https://raw.githubusercontent.com/jOOQ/sakila/refs/heads/main/mysql-sakila-db/mysql-sakila-insert-data.sql"
SAKILA_SCHEMA_FILE_LOCATION = SQL_SAKILA_FILES_LOCATION.joinpath("sakila-schema.sql")
SAKILA_DATA_FILE_LOCATION = SQL_SAKILA_FILES_LOCATION.joinpath("sakila-data.sql")

SQL_SCHEMA_EXISTS_QUERY: str = """SELECT NOT EXISTS (
SELECT 1 FROM information_schema.tables 
WHERE table_schema = 'public');
"""
