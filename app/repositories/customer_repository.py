from flask import g
from psycopg2 import  OperationalError
from ..models.customer import Customer

class CustomerRepository:
    def find_by_id(self, customer_id):
        try:
            customer = None
            connection = g.db
            cursor = connection.cursor()
            cursor.execute('SELECT * FROM customer WHERE id=%s;',(customer_id,))
            result_query = cursor.fetchone()

            if result_query:
                customer = Customer(*result_query)
        except Exception as e:
            print(f"Exception during customer insertion: {str(e)}")
            raise e  # Re-levanta a exceção para que o teste possa tratá-la

        finally:
            cursor.close()
        return customer




    def insert_customer(self, cutomer:Customer):
        try:
            with g.db.cursor() as cursor:
                cursor.execute(
                    'INSERT INTO customer (name, email) VALUES (%s, %s) RETURNING id, name, email;',
                    (cutomer.name, cutomer.email)
                )
                result_query = cursor.fetchone()


                customer = Customer(*result_query)
                return customer

        except OperationalError as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            raise  # Propaga a exceção para que o chamador possa lidar com ela




    def delete_customer(self, customer_id):
        try:
            with g.db.cursor() as cursor:
                cursor.execute('DELETE FROM customer WHERE id = %s RETURNING id, name, email;', (customer_id,))
                result_query = cursor.fetchone()

                # Você pode processar os resultados da exclusão, se necessário
                if result_query:
                    deleted_customer = Customer(*result_query)
                    return deleted_customer
                else:
                    return None  # Ou qualquer indicativo de que o cliente não foi encontrado

        except OperationalError as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            raise