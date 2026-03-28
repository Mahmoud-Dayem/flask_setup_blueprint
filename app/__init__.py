from flask import Flask

def create_app():
    app = Flask(__name__)
    
    app.config.from_object('config.Config')
    
    from app.blueprints.simple_page import simple_page
    from app.blueprints.games import games
    
    app.register_blueprint(simple_page,url_prefix=('/'))
    app.register_blueprint(games,url_prefix=('/games'))
    
    return app