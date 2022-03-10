# Variables
DOCKER_IMAGE_LINTER=alvarofpp/python-linter
ROOT=$(shell pwd)
LINT_COMMIT_TARGET_BRANCH=origin/main

# Commands
.PHONY:
down:
	@docker-compose down

.PHONY:
up-base:
	@docker-compose up rabbitmq restaurant-database

.PHONY:
up-restaurant:
	@docker-compose up restaurant-frontend restaurant-backend

.PHONY:
up-silent:
	@docker-compose up -d

.PHONY: lint
lint:
	@docker pull ${DOCKER_IMAGE_LINTER}
	@docker run --rm -v ${ROOT}:/app ${DOCKER_IMAGE_LINTER} " \
		lint-commit ${LINT_COMMIT_TARGET_BRANCH} \
		&& lint-yaml \
		&& lint-markdown \
		&& lint-python"

.PHONY: logs
logs:
	@docker-compose logs --follow

##############
# RESTAURANT #
##############

.PHONY:
restaurant-db-reset: restaurant-db-rollback restaurant-db-create restaurant-db-seed

.PHONY:
restaurant-db-create:
	@docker-compose exec restaurant-backend alembic upgrade head

.PHONY:
restaurant-db-rollback:
	@docker-compose exec restaurant-backend alembic downgrade base

.PHONY:
restaurant-db-seed:
	@docker-compose exec restaurant-backend python database/seeders/database_seeder.py