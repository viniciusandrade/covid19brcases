default: dev_compose_up

COMPOSE_FILE_DEV = docker-compose-dev.yml
COMPOSE_FILE_BUILD = docker-compose-build.yml

export APP_BUILD_DATE=$(shell date -u +"%Y-%m-%dT%H:%M:%SZ")

build_date:
	@echo "Build date: " $(APP_BUILD_DATE)

############################################
## atalhos docker-compose desenvolvimento ##
############################################

dev_compose_build:
	@docker-compose -f $(COMPOSE_FILE_DEV) build

dev_compose_up:
	@docker-compose -f $(COMPOSE_FILE_DEV) up -d

dev_compose_logs:
	@docker-compose -f $(COMPOSE_FILE_DEV) logs -f $(SERVICE)

dev_compose_stop:
	@docker-compose -f $(COMPOSE_FILE_DEV) stop

dev_compose_ps:
	@docker-compose -f $(COMPOSE_FILE_DEV) ps



