import os
from dotenv import load_dotenv
from flask import Flask
from flask_cors import CORS
from utils.limiter import limiter
from blueprints.vehicles import vehicles_bp
from blueprints.users import users_bp
from blueprints.company import companies_bp
from blueprints.service_center import service_centers_bp
from blueprints.service import services_bp
from blueprints.appointment import appointments_bp
from blueprints.permission import permissions_bp
from blueprints.review import reviews_bp
from blueprints.mechanic import mechanics_bp
from blueprints.specialization import specializations_bp
from blueprints.service_bay import service_bays_bp
from blueprints.config import config_bp
from utils.auth import auth_required, get_user_or_ip

# Load environment variables
load_dotenv()

app = Flask(__name__)
CORS(app)

# Initialize the limiter with the Flask app
limiter.init_app(app)

# Register blueprints
app.register_blueprint(vehicles_bp, url_prefix="/vehicles")
app.register_blueprint(users_bp, url_prefix="/users")
app.register_blueprint(companies_bp, url_prefix="/companies")
app.register_blueprint(service_centers_bp, url_prefix="/service-centers")
app.register_blueprint(services_bp, url_prefix="/services")
app.register_blueprint(appointments_bp, url_prefix="/appointments")
app.register_blueprint(permissions_bp, url_prefix="/permissions")
app.register_blueprint(reviews_bp, url_prefix="/reviews")
app.register_blueprint(mechanics_bp, url_prefix="/mechanics")
app.register_blueprint(specializations_bp, url_prefix="/specializations")
app.register_blueprint(service_bays_bp, url_prefix="/service-bays")
app.register_blueprint(config_bp, url_prefix="/config")


@app.route("/")
def health_check():
    return {"status": "API is running!", "message": "Servislah Gateway API"}


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port, debug=True)
