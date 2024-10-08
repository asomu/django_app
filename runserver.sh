#!bash
VENV_PATH="c:/Python/Project/django_app/.django_env/Scripts/activate"
DJANGO_PATH="c:/Python/Project/django_app/manage.py"
echo $VENV_PATH
source "$VENV_PATH"


python $DJANGO_PATH runserver --settings=config.settings.local 8080