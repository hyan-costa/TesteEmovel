import pytest
from flask import Flask, g
from ..models import customer
from ..services.support_service import SupportService
from ..repositories.support_repository import SupportRepository
from ..repositories.ticket_repository import TicketRepository
from ..models.support import Support,  SupportRank
from ..models.ticket import Ticket,TicketStatus
support_repository = SupportRepository()
ticket_repository = TicketRepository()
class TestSupportService:
    @pytest.fixture
    def support_aux(self):

        support_insert = Support(name="aaaaa",email="gmail.com",ranking='A')
        print(support_insert.ranking)
        support = support_repository.insert_support(support_insert)

        return support

    @pytest.fixture
    def ticket_aux(self):
        ticket_insert = Ticket(title="teste ticket",description="descricaoo")
        ticket = ticket_repository.insert_ticket(ticket_insert)
        return ticket

    def test_create_suuport(self, client, db):
        data = {
            "name":"juliana",
            "email":"july@gmail.com",
            "ranking":3
        }
        response = client.post("/supports", data=data)
        assert response.status_code == 201

    def test_find_by_support(self, client, db):
        support_id = 1
        response = client.get(f'/supports/{support_id}')
        assert response.status_code == 200

    def test_accept_ticket_success(self, client, db, support_aux, ticket_aux):

        response = client.post(f'/supports/{support_aux.id}/accept_ticket/{ticket_aux.id}')
        assert response.status_code == 200
        assert response.json["message"] == "ticket aceito"

        support = support_repository.find_by_id(support_aux.id)
        assert support.ticket == ticket_aux.id

    def test_accept_ticket_lock(self, client, db, support_aux, ticket_aux):

        client.post(f'/supports/{support_aux.id}/accept_ticket/{ticket_aux.id}')
        response = client.post(f'/supports/{support_aux.id}/accept_ticket/{ticket_aux.id}')

        assert response.status_code == 200
        assert response.json["message"] == "ticket já foi aceito"

    def test_close_ticket_success(self, client, db, support_aux, ticket_aux):

        support_aux.ticket = ticket_aux.id
        support_repository.update_support(support_aux)
        support = support_repository.find_by_id(support_aux.id)
        ticket_aux.status = TicketStatus.SOLVED.value
        ticket_repository.update_ticket(ticket_aux)
        ticket = ticket_repository.find_by_id(ticket_aux.id)

        response = client.post(f"/supports/{support.id}/close_ticket/{ticket.id}")

        assert  response.status_code == 200

    def test_close_ticket_not_bont_support(self, client, db, support_aux, ticket_aux):

        ticket_aux.status = TicketStatus.SOLVED.value
        ticket_repository.update_ticket(ticket_aux)
        ticket = ticket_repository.find_by_id(ticket_aux.id)

        response = client.post(f"/supports/{support_aux.id}/close_ticket/{ticket.id}")

        assert  response.status_code == 404


    def test_close_ticket_not_solved_or_closed(self, client, db, support_aux, ticket_aux):
        support_aux.ticket = ticket_aux.id
        support_repository.update_support(support_aux)
        support = support_repository.find_by_id(support_aux.id)

        response = client.post(f"/supports/{support.id}/close_ticket/{ticket_aux.id}")

        assert  response.status_code == 404