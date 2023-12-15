import pytest

from ..models.ticket import TicketStatus, Ticket
from ..repositories.ticket_repository import TicketRepository

ticket_repository = TicketRepository()

class TestTicketService:

    @pytest.fixture
    def ticket_aux(self):
        ticket_insert = Ticket(title="teste ticket",description="descricaoo")
        ticket = ticket_repository.insert_ticket(ticket_insert)
        return ticket

    def test_create_ticket(self, client):
        data ={
            "title":"titulo",
            "description":"teste"
        }
        response = client.post("/tickets",data=data)

        status = response.json["ticket"]["status"]
        assert response.status_code == 201
        assert status == TicketStatus.PENDING.value


    def test_find_by_ticket(self, client,db, ticket_aux):

        response = client.get(f'/tickets/{ticket_aux.id}')
        assert response.status_code == 200

