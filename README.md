Learning Python Django framework by implementing Wanteldy Skill list and skill recommendation REST webapp 


Commands : 

Install Virtual Enviornment :
>pip install virtualenv


Create Virtual Enviornment
>mkvirtualenv wantedly_virtual_env
Difference between virtualenv and mkvirtualenv - https://stackoverflow.com/a/44063472/2442565
This will generate a virtual environment directory which is essentially a sandboxed Python environment. Any python packages you install when this virtual environment is activated will only be installed into this folder. Likewise, you will need to use this virtual environment to run your application. Note that the “venv/” directory should already be added to your .gitignore file; virtual environments should never be committed to version control. While we’re on the subject of the .gitignore though, you should also add db.sqlite3 at the top of your .gitignore file. This will make it so the development database is not committed to the repository.

Select virtual env 
>workon <environemnt name - in our case its wantedly_virtual_env >

Install django
>pip install django
django version installed - 2.0 , pytz-2017.3

Initialize this Project as a Python Package
>pip install -e .

Install Django rest framework
>pip install django djangorestframework


Remember to keep the install_requires section of your setup.py file up-to-date with the latest installed dependencies. You can do this by running the following:
> pip freeze
Django==2.0
djangorestframework==3.7.7
pytz==2017.3

Make a new Django app.
wantedly_virtual_env> django-admin.py startproject wantedly_webapp





