from flask import Flask
from flask_swagger_ui import get_swaggerui_blueprint
from apps.core.db import db
from apps.paciente.views import views as paciente_views
from apps.core.views import views as core_views
from config import Config


app = Flask(__name__)
app.config.from_object('config.Config')
db.init_app(app)

swaggerui_blueprint = get_swaggerui_blueprint(
    Config.SWAGGER_URL,
    Config.API_URL,
)

app.register_blueprint(core_views)
app.register_blueprint(swaggerui_blueprint)
app.register_blueprint(paciente_views)



with app.app_context():
    db.create_all()

if __name__ == '__main__':    
    app.run(host="0.0.0.0", debug=True)
