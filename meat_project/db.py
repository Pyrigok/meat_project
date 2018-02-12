import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

DATABASES = {
	'default':{
		'ENGINE': 'django.db.backends.mysql',
		'HOST': 'localhost',
		'USER': 'meat_db_user',
		'PASSWORD': '1592648',
		'NAME': 'meat_db',
	}
	
}