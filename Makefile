migrations:
	alembic upgrade heads

seeds:
	python3 script.py

server:
	python3 server.py
