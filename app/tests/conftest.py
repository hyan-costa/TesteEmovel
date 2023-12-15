import pytest
from dotenv import load_dotenv
import os
from ..connection.db import get_db
from ..config import TestConfig
from app.app import create_app  # Substitua 'your_app_module' pelo módulo real do seu aplicativo

load_dotenv()

# @pytest.fixture
# def app():
#     # Use as configurações de teste para o aplicativo
#     test_app = create_app(test_config="test")
#
#     # Crie um contexto de aplicativo para os testes
#     with test_app.app_context():
#         yield test_app
@pytest.fixture
def app():
    test_app = create_app(TestConfig)
    test_app.config['TESTING'] = True
    with test_app.app_context():
        yield test_app

@pytest.fixture
def client(app):
    return app.test_client()


@pytest.fixture
def db(app):
    with app.app_context():
        db = get_db()

        # Inicia uma transação antes de cada teste
        db.autocommit = False

        yield db

        # Realiza o rollback ao final de cada teste
        db.rollback()
        db.autocommit = True
        db.close()

