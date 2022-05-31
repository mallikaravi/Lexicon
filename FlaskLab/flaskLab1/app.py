from flask import Flask,render_template,redirect,url_for,request
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired,Email,Length

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash,check_password_hash

from flask_login import LoginManager,UserMixin,login_user,login_required,logout_user,current_user



app = Flask(__name__)
app.config['SECRET_KEY'] = 'This is secret'


#connecting to database
app.config['SQLALCHEMY_DATABASE_URI'] ='sqlite:///test.db'
Bootstrap(app)

db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


#create a class

class student(db.Model):
     id = db.Column(db.Integer,primary_key =True)
     name = db.Column(db.String(200)) 
     age = db.Column(db.Integer) 
     group = db.Column(db.String(225)) 
     collegename = db.Column(db.String)  
 

     def __repr__(self):
      return'<task %r>' %self.id

@app.route('/index', methods = ['POST','GET'])
@login_required
def index():
    if request.method == 'POST':
        student_id = request.form['id']
        student_name = request.form['name']
        student_age= request.form['age']
        student_group = request.form['group']
        student_collegename = request.form['collegename']
        studentinfo = student(id =student_id,name =student_name,age=student_age,group=student_group,collegename=student_collegename)
        


        try:
            db.session.add(studentinfo)
            db.session.commit()
            return redirect('/index')

        except:
            return 'There is an issue in adding the information'

    else:
        students = student.query.order_by(student.id).all()

        return render_template('index.html',students=students)




@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = student.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'There is issue in deleting data'


@app.route('/update/<int:id>', methods = ['POST','GET'])
def update(id):
    task_to_update = student.query.get_or_404(id)
    if  request.method == 'POST':

        task_to_update.id = request.form['id']

        task_to_update.name = request.form['name']

        task_to_update.age = request.form['age']

        task_to_update.group = request.form['group']

        task_to_update.collegename= request.form['collegename']


        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Issue in updating'
    else:
        return render_template('update.html',task_to_update = task_to_update)

#create class for login page

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key =True)
    username = db.Column(db.String(15),unique= True)
    email = db.Column(db.String(50),unique= True)
    password = db.Column(db.String(80))

@login_manager.user_loader
def load_user(user_id):
    return  User.query.get(int(user_id))


class LoginForm(FlaskForm):
    username = StringField('username',validators = [InputRequired(),Length(min=4,max=15)])
    password = PasswordField('password',validators =[InputRequired(),Length(min=8,max=80)])
    remember = BooleanField('remember me')

@app.route('/')
def base():
    return render_template('base.html')

@app.route('/login',methods =['GET','POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user= User.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password,form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect('/index')
                
        return '<h1> Invalid username and password </h1>'
        #return '<h1>' + form.username.data + ''+ form.password.data + '</h1>'
    return render_template('login.html',form =form)

class RegistrationForm(FlaskForm):
    email = StringField('email',validators=[InputRequired(),Email(message = 'Invalid')])
    username = StringField('username', validators=[InputRequired(),Length(min=4,max=15)])
    password = PasswordField('password',validators =[InputRequired(),Length(min=8,max=80)])

@app.route('/signup',methods =['GET','POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data,method ='sha256')
        new_user = User(username = form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New User has been added</h1>'

       # return '<h1>' + form.username.data + ''+ form.password.data + form.email.data + '</h1>'
    return render_template('signup.html',form=form)



@app.route('/dashboard')

@login_required
def dashboard():
    return render_template('index.html')

if __name__== '__main__':
    app.run(debug=True)


    
    