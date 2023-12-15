from enum import Enum

class SupportRank(Enum):
    A = 'A'
    B = 'B'
    C = 'C'
    D = 'D'
class Support:
    def __init__(self, id=None, name=None, email=None, ranking=None, ticket=None):
        self.id = id
        self.name = name
        self.email = email
        self.ranking = ranking
        self.ticket = ticket