# Lexicon
echo "# mallikaravi" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mallikaravi/mallikaravi.git
git push -u origin main

#DJango Environment installation and configuration
- Install miniconda windows version python 3.7 Ref: https://docs.conda.io/en/latest/miniconda.html
- Check the version miniconda --version (conda --version)
    '# Django>conda --version
       conda 4.11.0'
- Create environemnt with conda for DJango installation.
     '# python --version ()
      #conda create --name DjangoENV python=3.5'
- Activate the conda environement
     '# conda activate DjangoEnv'
- Check the installed libraries using pip command
     '# pip list
      #python -m pip install --upgrade pip'
      Do again command 'pip list'
- Install django with 'pip install django==1.11'
- Create your project with 'django-admin startproject first_project'

-for the password authentications ,we need to write following commands 
#pip install bcrypt
#pip install pillow
#pip install django[argon2]



#FlaskEnvironment installation and configurationi
- Open run as administartor window in cmd
- Create environemnt with conda for Flask installation.
      #conda create --name FlaskENV python=3.5'

- Activate the conda environement
     '# conda activate FlaskEnv'
 -Check the installed libraries using pip command
     '# pip list'
- Run your programm using command
  #python app.py 
  #set FLASK_APP = "file" and type
  #FLASK run
- Instead of restarting server always,setup env variable

  #set FLASK_DEBUG =1

- create database by using extension by command
  #python
  #from filename import db
  #db.create_all() 

-to go to database shell
   #sqlite3 database.db 
   #select * from user

- when doing login pages we need to install 
    #pip install Flask_SQLAlchemy
    #pip install Flask_Bootstrap
    #pip install flask_wtf
    #pip insatll email_validator 
    #pip install flask_login 

-API python

-Activate API environment by using the command
  #conda create --name APIEnv python=3.5
  #activate APIEnv-
-you need to install api restframework
    #pip install djangorestframework


