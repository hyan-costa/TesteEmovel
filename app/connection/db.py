import psycopg2
from flask import g,current_app
from dotenv import load_dotenv
import os

load_dotenv()

def get_db():
    if 'db' not in g:


        g.db = psycopg2.connect(
            dbname=os.environ['POSTGRES_DB'],
            user=os.environ['POSTGRES_USER'],
            password=os.environ['POSTGRES_PASSWORD'],
            host=os.environ['POSTGRES_HOST'],
            port=os.environ['POSTGRES_PORT']
        )
        if current_app.config.get("TESTING"):
            g.db.autocommit = False
        else:
            g.db.autocommit = True

    return g.db

# def close_db():
#         db = g.pop('db', None)
#
#         if db is not None:
#             db.close()
