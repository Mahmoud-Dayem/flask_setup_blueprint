from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    
    from app.blueprints.simple_page import simple_page
    app.register_blueprint(simple_page)
    
    return app