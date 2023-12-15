from flask import  Blueprint, jsonify, request
from ..services.customer_service import CustomerService
from ..repositories.customer_repository import CustomerRepository


app_customer = Blueprint("controller",__name__)
customer_repository = CustomerRepository()
customer_service = CustomerService(customer_repository)


@app_customer.route("/customers",methods=['POST'])
def create():
    name = request.form.get("name")
    email = request.form.get("email")
    result, status_code = customer_service.create_customer(name, email)
    return jsonify(result), status_code


@app_customer.route("/customers/<int:customer_id>")
def get_customer(customer_id):
    customer, status_code = customer_service.get_customer(customer_id)
    return jsonify(customer), status_code



@app_customer.route("/customers/<int:customer_id>/approve_ticket/<int:ticket_id>",methods=['POST'])
def approve_ticket(customer_id, ticket_id):
    result, status_code = customer_service.approve_ticket(customer_id, ticket_id)
    return jsonify(result), status_code

@app_customer.route("/customers/<int:customer_id>/close_ticket/<int:ticket_id>",methods=['POST'])
def close_ticket(customer_id, ticket_id):
    result, status_code = customer_service.close_ticket(customer_id, ticket_id)
    return jsonify(result), status_code