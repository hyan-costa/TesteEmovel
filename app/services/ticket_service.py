from ..repositories.ticket_repository import TicketRepository
from ..models.ticket import Ticket,TicketStatus
import datetime
class TicketService:
    def __init__(self, ticket_repository:TicketRepository):
        self.ticket_repository = ticket_repository


    def get_ticket(self, ticket_id):
        try:
            if ticket_id:
                ticket = self.ticket_repository.find_by_id(ticket_id)
                if ticket:
                    return {"ticket": ticket.__dict__}, 200
                else:
                    return {"message": "Cliente não encontrado"}, 404
        except Exception as e:

            return {"message": "Erro interno ao processar a solicitação"}, 500


    def create_ticket(self,title, description):
        try:
            if title and description:
                status = TicketStatus.PENDING.value
                ticket = Ticket(title=title, description=description, status=status)

                result = self.ticket_repository.insert_ticket(ticket)
                return {"ticket":result.__dict__}, 201
            else:
                return {"message": "Erro ao tentar criar ticket"}, 400
        except Exception as e:
            return {"message": "Erro interno ao processar a solicitação"}, 500

