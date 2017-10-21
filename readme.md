# Что сделал:
	- Редактировать, создавать и удалять записи можно в админке
	- Скрипт create_users_and_entries.py создает только 100 пользователей  
	  и 1000 записей, потому что создание 1000 пользователей занимает ~15 мин
	- Все остальное реализовано

# Как запустить:
	- python install -r requirements.txt
	- python manage.py makemigrations
	- python manage.py migrate
	- python manage.py shell
		- import create_users_and_entries
	- python manage.py runserver

# Как протестить API:
	- curl --data "password=user_0&username=user_0" http://localhost:8000/api-token-auth/
	- Поместить полученный токен в скрипт test_api.py
	- `python3 test_api.py`