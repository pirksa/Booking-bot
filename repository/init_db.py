from pathlib import Path

import psycopg2

from settings import load_config

config = load_config()
sql_script = Path(__file__).parent / 'schema.sql'


def create_schema():
    con = psycopg2.connect(database=config['db']['database'], user=config['db']['user'],
                           password=config['db']['password'], host=config['db']['host'])
    cur = con.cursor()
    cur.execute(open(sql_script, 'r').read())
    con.commit()
    cur.close()
    con.close()
