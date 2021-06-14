from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app(config=None):
    app = Flask(__name__)
    
    if app.config["ENV"] == 'production': #config는 dictionary의 서브클래스, 다른 딕셔너리처럼 수정될 수 있음
        app.config.from_object('config.ProductionConfig') #환경변수 config.py파일에 정의된 ProductionConfig을 환경변수로 사용하고자 함
    else:
        app.config.from_object('config.DevelopmentConfig')

    if config is not None:
        app.config.update(config) #한번에 다수의 키를 업데이트하는 dict.update함수

    db.init_app(app)
    migrate.init_app(app, db)
    from . import models
    from project import routes
    app.register_blueprint(routes.bp)
    #app.register_blueprint(analyze_route.bp, url_prefix='/api')

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)