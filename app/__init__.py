from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

# 애플리케이션 팩토리: app 객체를 생성하는 함수를 의미
# 플라스크 내부에서 정의된 함수명이므로 이름 변경 불가
def create_app():
    app = Flask(__name__)  # 플라스크 애플리케이션을 생성하는 코드
    app.config.from_object(config)  # config.py 파일에 작성한 항목을 읽어줌

    # ORM 객체 등록
    db.init_app(app)
    migrate.init_app(app, db)
    # db 모델 import
    from . import models

    # 애너테이션: 주석처럼 프로그램에 영향을 미치지 않으면서, 유용한 정보를 제공하는 것
    # 주석처럼 특별한 의미나 기능을 제공
    # 현재는 URL을 매핑해 줌
    # @app.route('/')
    # def hello_pybo(): # /URL과 매핑하는 함수
    #     return 'Hello, Pybo!^^'

    # 블루 프린트
    from .views import main_views, question_views, answer_views
    app.register_blueprint(main_views.bp) # bp: main_views 파일에서 생성한 블루프린트 객체 이름
    app.register_blueprint(question_views.bp)
    app.register_blueprint(answer_views.bp)

    return app
