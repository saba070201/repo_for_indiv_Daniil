from flask import Flask,render_template,redirect,request,url_for
from flask_sqlalchemy import SQLAlchemy
from models import *


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///notes_app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db=SQLAlchemy()
db.init_app(app)
@app.route('/',methods=['GET', 'POST'])
def home():
      notes=db.session.execute(db.select(Notes).order_by(Notes.important.desc())).scalars()
      return render_template('home.html',notes=notes)

@app.route('/note-<int:note_pk>',methods=['GET', 'POST'])
def note(note_pk):
      note=db.get_or_404(Notes,note_pk)
      return render_template('note.html',note=note)
@app.route('/create-note')
def create_note():
     note=Notes(title='title',memo='memo',important=1)
     db.session.add(note)
     db.session.commit()
     return redirect(url_for('note',note_pk=note.id))
@app.route('/delete-note-<int:note_pk>')
def delete_note(note_pk):
     note=db.get_or_404(Notes,note_pk)
     db.session.delete(note)
     db.session.commit()
     return redirect(url_for('home'))
@app.route('/change-note-<int:note_pk>',methods=['GET', 'POST'])
def change_note(note_pk):
     note=db.get_or_404(Notes,note_pk)
     if request.method=='POST':
        note.title=request.form.get('title')
        note.memo=request.form.get('memo')
        db.session.commit()
        return redirect(url_for('home'))
if __name__ == '__main__':
    app.run(debug=True) # debug = True очень важен !!!!!! и if __name__ на всякий тоже надо!!!!