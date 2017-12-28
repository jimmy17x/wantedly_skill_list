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
    	'Django==2.0',
		'djangorestframework==3.7.7',
		'pytz==2017.3'
    ],
    INSTALLED_APPS = (
    'rest_framework',
	)
)