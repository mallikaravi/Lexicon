from flask import Flask,render_template,request,redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)

#connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'

db = SQLAlchemy(app)


#create a class

class ToDo(db.Model):
     id = db.Column(db.Integer,primary_key =True)
     content = db.Column(db.String(200),nullable=False)
     date_created = db.Column(db.DateTime,default = datetime.utcnow)
    

def __repr__(self):
    return'<task %r>' %self.id



#@app.route('/Home/< int:Id>')
#return "<h1>Hello Welcome</h1>"
    #return "Hello %d" %Id

@app.route('/',methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        task_content = request.form['content']
        new_task = ToDo(content = task_content)

        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')

        except:
            return 'There is an issue in adding the task'

    else:
        tasks = ToDo.query.order_by(ToDo.date_created).all()

        return render_template('index.html',tasks=tasks)

    
    return render_template('index.html')

@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = ToDo.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There is issue in deleting data'

@app.route('/update/<int:id>', methods = ['POST','GET'])
def update(id):
    task_to_update = ToDo.query.get_or_404(id)
    if request.method == 'POST':
        task_to_update.content = request.form['content']

        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue in updating'
    else:
        return render_template('update.html',task_to_update = task_to_update)

if __name__ == "__main__":

    app.run(debug = True)