from flask import g
from psycopg2 import OperationalError
from ..models.ticket import Ticket,TicketStatus
import datetime
class TicketRepository:



    def find_by_id(self, ticket_id):
        try:
            with g.db.cursor() as cursor:
                cursor.execute(
                    "SELECT * FROM ticket WHERE ticket.id = %s;",
                    (ticket_id,)
                )
                result_query = cursor.fetchone()

                if result_query:
                    ticket = Ticket(*result_query)
                    return ticket
        except Exception as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            raise



    def insert_ticket(self, ticket:Ticket):
        try:
            with g.db.cursor() as cursor:



                cursor.execute(
                    "INSERT INTO ticket (title, description, status, date) VALUES (%s, %s, %s, %s) RETURNING "
                    "id,title, description, status;",
                    (ticket.title, ticket.description, ticket.status,ticket.date)
                )
                result_query = cursor.fetchone()
                if result_query:
                    ticket = Ticket(*result_query)
                    return ticket

        except Exception as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            raise

    def update_ticket(self, ticket: Ticket):
        try:
            with g.db.cursor() as cursor:


                # Atualiza os campos desejados (substitua os nomes dos campos e valores pelos reais)
                cursor.execute(
                    'UPDATE ticket SET title = %s, description = %s, status = %s, closed_by_id=%s WHERE id = %s',
                    (ticket.title, ticket.description, ticket.status, ticket.closed_by, ticket.id)
                )

                return f"Atualização bem-sucedida"
        except Exception as e:
            error_message = f"Erro de operação no banco de dados: {str(e)}"
            print(error_message)
            return None

