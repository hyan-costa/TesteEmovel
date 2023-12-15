from .support_controller import app_support
from .customer_controller import app_customer
from .ticket_controller import app_ticket
def register_router(app):
    app.register_blueprint(app_support)
    app.register_blueprint(app_customer)
    app.register_blueprint(app_ticket)