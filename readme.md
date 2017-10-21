# Что сделал:
	- Редактировать, создавать и удалять записи можно в админке
	- Скрипт create_users_and_entries.py создает только 10 пользователей и 100 записей, потому что я не смог ускорить этот процесс

# Как запустить:
	- python install -r requirements.txt
	- python manage.py makemigrations
	- python manage.py migrate
	- python manage.py shell
		- import create_users_and_entries
	- python manage.py runserver