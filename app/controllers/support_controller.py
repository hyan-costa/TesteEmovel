
from flask import  Blueprint, jsonify, request
from  ..services.support_service import SupportService
from ..repositories.support_repository import SupportRepository


app_support = Blueprint("support",__name__)

support_repository = SupportRepository()
support_service = SupportService(support_repository)



@app_support.route("/supports", methods=['POST'])
def create():
    name = request.form.get("name")
    email = request.form.get("email")
    ranking = request.form.get("ranking")
    result, status_code = support_service.create_support(name, email, ranking)
    return jsonify(result), status_code

@app_support.route("/supports/<int:support_id>")
def get_support(support_id):
    support, status_code = support_service.get_support(support_id)
    return jsonify(support), status_code


@app_support.route("/supports/<int:support_id>/accept_ticket/<int:ticket_id>", methods=['POST'])
def accept_ticket(support_id,ticket_id):
    result, status_code = support_service.accept_ticket(support_id,ticket_id)
    return jsonify(result), status_code


@app_support.route("/supports/<int:support_id>/close_ticket/<int:ticket_id>",methods=['POST'])
def close_ticket(support_id, ticket_id):
    result, status_code = support_service.close_ticket(support_id, ticket_id)
    return jsonify(result), status_code
