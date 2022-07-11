run-dev:
	 poetry run python manage.py runserver

run:
	export DJANGO_SETTINGS_MODULE=task_manager.settings
	gunicorn task_manager.wsgi

translate-make:
	django-admin makemessages -l ru

translate-compile:
	django-admin compilemessages
