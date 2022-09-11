run-dev:
	 poetry run python manage.py runserver

run:
	export DJANGO_SETTINGS_MODULE=task_manager.settings
	gunicorn task_manager.wsgi

translate-make:
	django-admin makemessages -l ru

translate-compile:
	django-admin compilemessages

migrations-create:
	python ./manage.py makemigrations

migrations-run:
	python ./manage.py migrate

lint:
	poetry run flake8 task_manager

test:
	./manage.py test

install:
	poetry install

deploy:
	git push heroku main
