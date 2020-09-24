include .env
microservice_empty_pythontag=latest

all: up

up: prune
	microservice_empty_pythontag=$(microservice_empty_pythontag) docker-compose up -d

changemicroservice_empty_pythonVersion: prune
	microservice_empty_pythontag=$(microservice_empty_pythontag) docker-compose up -d microservice_empty_python

down: 
	docker-compose down

prune:
	docker image prune -af

dumppostgres:
	docker-compose exec db pg_dump -U $(POSTGRES_USER) $(POSTGRES_DB) > dump_$(shell basename $(shell pwd))_$(shell date +%Y-%m-%d_%H:%M).sql 

createsuperuser:
	docker-compose exec back python3 manage.py createsuperuser

initflaskdb:
	docker-compose exec microservice_empty_python bash -c "flask db init && flask db migrate && flask db upgrade"

build:
	docker-compose build

ps:
	docker-compose ps

logs:
	docker-compose logs

restart: down
	make up
