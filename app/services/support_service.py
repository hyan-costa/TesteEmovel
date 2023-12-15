

from ..repositories.support_repository import SupportRepository
from  ..services.ticket_service import TicketService, TicketStatus
from ..models.support import Support
from ..repositories.ticket_repository import TicketRepository


ticket_repository = TicketRepository()
class SupportService:
    def __init__(self, support_repository:SupportRepository):
        self.support_repository = support_repository

    def create_support(self, name, email, ranking):
        try:
            if name and email and ranking:
                support_insert = Support(name=name,email=email,ranking=ranking)
                support = self.support_repository.insert_support(support_insert)
                return {"message":"Criado com sucesso!!", "support": support.__dict__}, 201
            else:
                return {"message": "Criado com sucesso!!"}, 400
        except Exception as e:
            return {"message": f"Erro interno ao processar a solicitação {str(e)}"}, 500

    def accept_ticket(self, support_id, ticket_id):

        try:
            ticket = ticket_repository.find_by_id(ticket_id)
            support = self.support_repository.find_by_id(support_id)

            if not (ticket and support):
                return {"message": "Erro ao aceitar ticket"}, 400

            if ticket.status == TicketStatus.PENDING.value:
                support.ticket = ticket.id
                ticket.status = TicketStatus.REVIEW.value

                result_support = self.support_repository.update_support(support)
                result_ticket = ticket_repository.update_ticket(ticket)

                if result_support and result_ticket:
                    return {"message": "ticket aceito"}, 200
                else:
                    return {"message": "Erro ao aceitar ticket"}, 500
            else:
                return {"message": "ticket já foi aceito"}, 200
        except Exception as e:
            return {"message": f"Erro interno: {str(e)}"}, 500

    def get_support(self, support_id):
        try:
            if not support_id:
                return {"message": "ID do suporte inválido"}, 400

            support = self.support_repository.find_by_id(support_id)

            if support:
                return {"support": support.__dict__}, 200
            else:
                return {"message": "Suporte não encontrado"}, 404
        except Exception as e:
            return {"message": f"Erro interno: {str(e)}"}, 500

    def close_ticket(self, support_id, ticket_id):
        support = self.support_repository.find_by_id(support_id)
        ticket = ticket_repository.find_by_id(ticket_id)
        try:
            if support.ticket == ticket.id:
                if ticket.status in [TicketStatus.SOLVED.value, TicketStatus.CLOSED.value]:
                    ticket.status = TicketStatus.CLOSED.value
                    ticket.closed_by = support_id
                    ticket_repository.update_ticket(ticket)
                    return {"message": "Ticket fechado!"}, 200
                else:
                    return {"message": "Ticket não pode ser fechado"}, 404
            else:
                return {"message": "Ticket não pertence a esse suporte"}, 404
        except:
            return {"message": "Ticket não existe"}, 404