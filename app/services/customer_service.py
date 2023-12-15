from ..repositories.customer_repository import CustomerRepository
from ..repositories.ticket_repository import TicketRepository, TicketStatus
from ..models.customer import Customer

ticket_repository = TicketRepository()
class CustomerService:
    def __init__(self, customer_repository:CustomerRepository):
        self.customer_repository = customer_repository

    def create_customer(self, name, email):
        try:
            if name and email:
                custumer_insert = Customer(name=name,email=email)
                customer = self.customer_repository.insert_customer(custumer_insert)
                return {"message": "Criado com sucesso!!","customer":customer.__dict__}, 201
            else:
                return {"message": "Erro ao tentar criar cliente"}, 400
        except Exception as e:
            return {"message": "Erro interno ao processar a solicitação"}, 500

    def get_customer(self, customer_id):
        try:
            if customer_id:
                customer = self.customer_repository.find_by_id(customer_id)
                if customer:
                    return {"customer": customer.__dict__}, 200
                else:
                    return {"message": "Cliente não encontrado"}, 404
        except Exception as e:
            print(f"Exception during customer creation: {str(e)}")
            return {"message": "Erro interno ao processar a solicitação"}, 500


    def approve_ticket(self, customer_id, ticket_id):
        if customer_id and ticket_id:

            ticket = ticket_repository.find_by_id(ticket_id)
            customer = self.customer_repository.find_by_id(customer_id)
            if customer:
                if  ticket.status == TicketStatus.REVIEW.value:
                    ticket.status = TicketStatus.SOLVED.value
                    ticket_repository.update_ticket(ticket)
                    return {"message": f'cliente {customer.name} aprovou ticket'}, 200
                else:
                    return {"message": "ticket não está em enálise"},404
            else:
                return {"message": " cliente nao existe"},404
        else:
            return {"message": "Erro ao tentar aprovar ticket"},400


    def close_ticket(self, customer_id, ticket_id):

        ticket = ticket_repository.find_by_id(ticket_id)
        customer = self.customer_repository.find_by_id(customer_id)
        if customer:
            ticket.status = TicketStatus.CLOSED.value
            ticket.closed_by = customer_id
            ticket_repository.update_ticket(ticket)
            return {"message": f'cliente {customer.name} fechou ticket'}, 200
        else:
            return {"message": "cliente não existe"}, 404