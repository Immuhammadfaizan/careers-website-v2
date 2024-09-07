from flask import Flask
from .routes import analytics, security, seo, performance

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')

    app.register_blueprint(analytics.bp)
    app.register_blueprint(security.bp)
    app.register_blueprint(seo.bp)
    app.register_blueprint(performance.bp)

    return app
