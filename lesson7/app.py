from flask import Flask,render_template,redirect,request,url_for
app=Flask(__name__)
@app.route('/',methods=['GET', 'POST'])
def home():
      return render_template('index.html')


@app.route('/result',methods=['GET', 'POST'])
def result():
    message=request.args.get('message')
    return str(message)
app.run()
