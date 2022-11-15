from app import db

# db.Model 클래스를 상속한 클래스
class Question(db.Model):
    # db.Column(데이터 타입, primary_key: 각 데이터를 구분하는 id, nullable: 빈 값 허용 여부)
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False) # db.Text(): 글자 수 제한이 없는 텍스트
    create_date = db.Column(db.DateTime(), nullable=False) # db.DateTime(): 날짜와 시각
    
class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # db.ForeignKey: 모델을 서로 연결할 때 사용
    # question.id와 연동됨
    # ondelete: 삭제 연동 설정, 질문이 삭제되면 답변도 함께 삭제되도록 설정함(CASCADE)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id', ondelete='CASCADE')) 
    # 답변 모델에서 질문 모델을 참조하기 위해 추가
    # db.relationship으로 답변 모델에서 질문 모델 제목을 참조할 수 있음
    question = db.relationship('Question', backref=db.backref('answer_set', cascade='all, delete-orphan'))
    content = db.Column(db.Text(), nullable=False) # db.Text(): 글자 수 제한이 없는 텍스트
    create_date = db.Column(db.DateTime(), nullable=False) # db.DateTime(): 날짜와 시각   