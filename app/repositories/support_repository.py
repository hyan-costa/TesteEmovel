from flask import g
from psycopg2 import OperationalError
from ..models.support import Support
class SupportRepository:
    def find_by_id(self, support_id):
        try:
            with g.db.cursor() as cursor:
                cursor.execute('SELECT * FROM support WHERE id=%s;',(support_id,))
                result_query = cursor.fetchone()

                if result_query:
                    support = Support(*result_query)
                return support
        except OperationalError as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            raise

    def insert_support(self, support:Support):
        try:
            with g.db.cursor() as cursor:
                print(support.ranking)
                cursor.execute(
                    'INSERT INTO support (name, email, ranking) VALUES (%s, %s, %s)'
                    'RETURNING id, name, email, ranking',(support.name, support.email, support.ranking)
                )
                result_query = cursor.fetchone()

                support = Support(*result_query)
                return support
        except OperationalError as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            raise

    def update_support(self, support:Support):
        try:
            with g.db.cursor() as cursor:
                cursor.execute(
                    'UPDATE support SET name = %s, email = %s, ranking = %s, ticket = %s WHERE id = %s '
                    ' RETURNING id, name,email, ranking, ticket',
                    (support.name, support.email, support.ranking,support.ticket, support.id)
                )
                result_query = cursor.fetchone()

                support = Support(*result_query)
                return support
        except OperationalError as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            return None
