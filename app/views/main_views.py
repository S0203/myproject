from flask import Blueprint, url_for
from werkzeug.utils import redirect

# 'main': 현재 블루프린트의 별칭(나중에 자주 사용할 url_for 함수에서 사용됨)
# __name__: 모듈명인 main_views가 전달됨
# url_prefix: 라우팅 함수의 애너테이션 URL앞에 기본으로 붙일 접두어 URL -> localhost:5000 + url_prefix
# https://scribblinganything.tistory.com/178
bp = Blueprint('main', __name__, url_prefix='/')



@bp.route('/hello') # 여기만 바뀜
def hello_pybo():
    return 'Hello, Pybo!'

@bp.route('/')
def index():
    return redirect(url_for('question._list'))




