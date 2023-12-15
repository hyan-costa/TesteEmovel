from enum import Enum, auto
from datetime import datetime

class TicketStatus(Enum):
    PENDING = auto()
    REVIEW = auto()
    SOLVED = auto()
    CLOSED = auto()

    def get_ticket_status_by_id(status_id):
        for status in TicketStatus:
            if status.value == status_id:
                return status
        return None
class Ticket:
    def __init__(self,id=None, title=None, description=None, status=TicketStatus.PENDING.value,date=None, closed_by=None):
        self.id = id # Pode ser gerado automaticamente ou configurado de alguma maneira específica
        self.title = title
        self.description = description
        self.status = status
        self.date = date or datetime.now()
        self.closed_by = closed_by

    def approve(self):
        if self.status == TicketStatus.REVIEW:
            self.status = TicketStatus.SOLVED
        else:
            raise ValueError("O ticket não está no status de revisão para ser aprovado.")

    def close(self, closed_by):
        if self.status == TicketStatus.SOLVED and closed_by:
            self.status = TicketStatus.CLOSED
            self.closed_by = closed_by
        else:
            raise ValueError(
                "O ticket não está no status resolvido ou não foi fornecido um identificador válido para quem o fechou.")
