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




Make a new Django app.
wantedly_virtual_env> django-admin.py startproject wantedly_webapp

Install rest-auth , jwt and allauth package
>pip install django-rest-auth
>pip install djangorestframework-jwt
>pip install django-allauth






Remember to keep the install_requires section of your setup.py file up-to-date with the latest installed dependencies. You can do this by running the following:
> pip freeze

certifi==2017.11.5
chardet==3.0.4
defusedxml==0.5.0
Django==2.0
django-allauth==0.34.0
django-rest-auth==0.9.2
djangorestframework==3.7.7
djangorestframework-jwt==1.11.0
idna==2.6
oauthlib==2.0.6
PyJWT==1.5.3
python3-openid==3.1.0
pytz==2017.3
requests==2.18.4
requests-oauthlib==0.8.0
six==1.11.0
urllib3==1.22


Run >python manage.py migrate 
to make all the necessary database changes, and then you will be able to start using these.

jQuery JWT localStorage implementation -
https://github.com/chaofz/jquery-jwt-auth/blob/master/index.html



Database model :
User , Skill , User_to_Skill  (Foreign key - user_id , skill_id, recommendation_id_array(comma seprated)) -  trade offs between creating a new table to store +1 on skill done by users in network vs O(20,0000) operartions processing  

https://stackoverflow.com/questions/40125110/using-multiple-columns-as-foreignkey-to-return-in-another-table
https://stackoverflow.com/questions/40125110/using-multiple-columns-as-foreignkey-to-return-in-another-table

Scotch.io tutorials
https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-1
https://scotch.io/tutorials/build-a-rest-api-with-django-a-test-driven-approach-part-2

Django Queries
https://docs.djangoproject.com/en/2.0/topics/db/queries/


Create a user using Django shell
from django.contrib.auth.models import User
user = User.objects.create_user(username='foo', email='foo@bar.com', password='bar')
user.save()
