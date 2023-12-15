
from flask import  Blueprint, jsonify, request
from  ..services.ticket_service import TicketService
from ..repositories.ticket_repository import TicketRepository


app_ticket = Blueprint("ticket",__name__)

ticket_repository = TicketRepository()
ticket_service = TicketService(ticket_repository)



# @app_ticket.route("/tickets", methods=['POST'])
# def create():
#     name = request.form.get("name")
#     email = request.form.get("email")
#     ranking = request.form.get("ranking")
#     result, status_code = ticket_service.create_support(name, email, ranking)
#     return jsonify(result), status_code

@app_ticket.route("/tickets/<int:ticket_id>")
def get_ticket(ticket_id):
    support, status_code = ticket_service.get_ticket(ticket_id)
    return jsonify(support), status_code

@app_ticket.route("/tickets", methods=['POST'])
def create():
    tile = request.form.get("title")
    description = request.form.get("description")
    support, status_code = ticket_service.create_ticket(tile,description)
    return jsonify(support), status_code


