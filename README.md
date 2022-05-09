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
      # conda create --name DjangoENV python=3.5'
- Activate the conda environement
     '# conda activate DjangoEnv'
- Check the installed libraries using pip command
     '# pip list
      # python -m pip install --upgrade pip'
      Do again command 'pip list'
- Install django with 'pip install django==1.11'
- Create your project with 'django-admin startproject first_project'
