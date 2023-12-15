from flask import Flask
from .connection import db
from .controllers import register_router
from .config import TestConfig

def create_app(test_config=None):
    app = Flask(__name__)
    # Configurações específicas para ambientes (por exemplo, 'development', 'test', 'production')
    if test_config:
        # load the test config if passed in
        app.config.from_object(TestConfig)

    # Inicializacao dos blueprints
    register_router(app)

    # Adicione lógica de inicialização e fechamento do banco de dados
    @app.before_request
    def before_request():
        db.get_db()

    # @app.teardown_appcontext
    # def teardown_appcontext(exception=None):
    #     db.close_db(app, exception)

    return app

if __name__ == '__main__':
    # Se for, inicializa o aplicativo
    app = create_app()
    app.run(debug=True)
