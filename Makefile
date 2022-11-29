migration:
	alembic revision --autogenerate -m "create article model"

migrate:
	alembic upgrade heads

seeds:
	python3 script.py

server:
	python3 server.py
