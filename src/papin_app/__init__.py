from flask import Flask

app = Flask(__name__)

# Import and register blueprints
from papin_app.routes import main_bp
app.register_blueprint(main_bp)