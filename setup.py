from distutils.core import setup

setup(
    name='wantedly_skill_list_webapp',
    version='0.1',
    description='A Wantedly skill list webapp with Django REST Framework',
    author='Divyanshu Divyanshu',
    author_email='divyanshu17x@gmail.com',
    url='https://github.com/jimmy17x/wantedly_skill_list.git',
    packages=find_packages(),
    install_requires=[
    	'certifi==2017.11.5',
		'chardet==3.0.4',
		'defusedxml==0.5.0',
		'Django==2.0',
		'django-allauth==0.34.0',
		'django-rest-auth==0.9.2',
		'djangorestframework==3.9.1',
		'djangorestframework-jwt==1.11.0',
		'idna==2.6',
		'oauthlib==2.0.6',
		'PyJWT==1.5.3',
		'python3-openid==3.1.0',
		'pytz==2017.3',
		'requests==2.18.4',
		'requests-oauthlib==0.8.0',
		'six==1.11.0',
		'urllib3==1.22'
    ],
    
)

