import pytest
from app.app import create_app
from ..models.customer import Customer
from ..models.support import Support
from ..models.ticket import Ticket, TicketStatus
from ..repositories.support_repository import SupportRepository
from ..repositories.ticket_repository import TicketRepository
from ..services.customer_service import CustomerService
from ..repositories.customer_repository import CustomerRepository
from ..config import TestConfig
support_repository = SupportRepository()
ticket_repository = TicketRepository()
customer_repository = CustomerRepository()
class TestCustomerService:
    @pytest.fixture
    def customer_aux(self):
        customer_insert = Customer(name="caio silva", email="silva@gmail.com")
        customer = customer_repository.insert_customer(customer_insert)
        return customer
    @pytest.fixture
    def support_aux(self):
        support_insert = Support(name="aaaaa", email="gmail.com", ranking='A')
        print(support_insert.ranking)
        support = support_repository.insert_support(support_insert)

        return support

    @pytest.fixture
    def ticket_aux(self):
        ticket_insert = Ticket(title="teste ticket", description="descricaoo")
        ticket = ticket_repository.insert_ticket(ticket_insert)
        return ticket

    def test_create_customer(self, client):
        data = {
            'name': 'tiao',
            'email': 'john@gmail.com'
        }
        response = client.post('/customers', data=data)

        assert response.status_code == 201

        customer_id = response.json["customer"]["id"]
        customer_repository = CustomerRepository()
        result = customer_repository.find_by_id(customer_id)

        assert result.id == customer_id
        assert result.name == data['name']
        assert result.email == data['email']

    def test_find_by_customer(self, client, db, customer_aux):

        response = client.get(f'/customers/{customer_aux.id}')
        assert response.status_code == 200



    def test_approve_ticket_success(self, client, db, ticket_aux,customer_aux):
        ticket_aux.status =  TicketStatus.REVIEW.value
        ticket_repository.update_ticket(ticket_aux)
        ticket = ticket_repository.find_by_id(ticket_aux.id)
        response = client.post(f"/customers/{customer_aux.id}/approve_ticket/{ticket.id}")

        assert response.status_code == 200


    def test_approve_ticket_not_analyze(self, client, db, ticket_aux,customer_aux):
        response = client.post(f"/customers/{customer_aux.id}/approve_ticket/{ticket_aux.id}")
        assert response.json["message"] == 'ticket não está em enálise'



    def test_approve_ticket_not_customer(self,client, db, ticket_aux,customer_aux):
        customer_repository.delete_customer(customer_aux.id)

        response = client.post(f"/customers/{customer_aux.id}/approve_ticket/{ticket_aux.id}")
        assert response.json["message"] == ' cliente nao existe'


    def test_close_ticket_success(self, client, db, ticket_aux,customer_aux):

        response = client.post(f"/customers/{customer_aux.id}/close_ticket/{ticket_aux.id}")
        assert response.status_code == 200


    def test_close_ticket_not_customer(self, client, db, ticket_aux,customer_aux):
        customer_repository.delete_customer(customer_aux.id)
        response = client.post(f"/customers/{customer_aux.id}/close_ticket/{ticket_aux.id}")
        assert response.status_code == 404