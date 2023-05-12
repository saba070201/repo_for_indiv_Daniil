### comment
from app import db ,app
class Notes(db.Model):
    __tablename__='notes'
    id=db.Column(db.Integer,primary_key=True)
    title=db.Column(db.String(250),nullable=False)
    memo=db.Column(db.String(5000),nullable=False)
    important=db.Column(db.Boolean)
with app.app_context():
    db.create_all()




    
 