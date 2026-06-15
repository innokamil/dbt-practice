from pathlib import Path
import re
from airflow.providers.mysql.hooks.mysql import MySqlHook 
from airflow.providers.standard.operators.trigger_dagrun import TriggerDagRunOperator
from airflow.sdk import dag, task 
import datetime
from config import SAKILA_DATA_FILE_LOCATION, SAKILA_SCHEMA_FILE_LOCATION


@dag(dag_id="database_sakila_fill",
     start_date=datetime.datetime(2026, 5, 28),
     schedule="@once",
     catchup=False)
def database_sakila_fill():
    @task(task_id="run_sql")
    def run_sql(db_conn_id: str, sql_filepath: str | Path):
        with open(sql_filepath, "r", encoding="utf-8") as f:
            content = f.read()
        
        # NOTE: Those steps are NECESSARY, because connector is picky about the
        # syntax.
        # DELIMITER causes syntax error - this regex grabs any DELIMITER and removes it 
        content = re.sub(r'(?i)^\s*DELIMITER\s+\S+.*$', '', content, flags=re.MULTILINE)

        # We replace any tokens that are leftovers of DELIMITER
        content = content.replace(';;', ';')
        content = content.replace('$$', ';')
        content = content.replace('//', ';')
        hook = MySqlHook(mysql_conn_id=db_conn_id)
        hook.run(
            sql=content, 
            autocommit=True, 
            split_statements=False
        )

    _trigger_download_sqls = TriggerDagRunOperator(task_id="download_sqls", 
                                                   trigger_dag_id="database_sakila_download_sqls")


    (_trigger_download_sqls >> 
        run_sql("sakila_default", SAKILA_SCHEMA_FILE_LOCATION) >>
        run_sql("sakila_default", SAKILA_DATA_FILE_LOCATION)
     )

database_sakila_fill()
