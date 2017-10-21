# Что сделал:
	- Редактировать, создавать и удалять записи можно в админке
	- Скрипт create_users_and_entries.py создает только 100 пользователей и 1000 записей, потому что создание 1000 пользователей занимает ~15 мин

# Как запустить:
	- python install -r requirements.txt
	- python manage.py makemigrations
	- python manage.py migrate
	- python manage.py shell
		- import create_users_and_entries
	- python manage.py runserver