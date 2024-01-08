# Define variables
APP_NAME=utils-ai-plugin
NGINX_CONF=nginx.conf
NGINX_SITES_ENABLED=/etc/nginx/sites-enabled
GHCR_USERNAME=workouse
IMAGE_TAG=latest  # or specify a specific tag
GHCR_IMAGE=ghcr.io/$(GHCR_USERNAME)/$(APP_NAME):$(IMAGE_TAG)


-include .env

# Build the Docker image
build:
	docker build -t $(APP_NAME) .

# Pull the Docker image from GHCR
pull:
	docker pull $(GHCR_IMAGE)

# Run the Docker container
run:
	docker run -d -p 5000:5000 --name $(APP_NAME) $(APP_NAME)

login:
ifndef GHCR_TOKEN
	$(error GHCR_TOKEN is undefined. Create an .env file with your token.)
endif
	@echo "Logging in to GitHub Container Registry..."
	@docker login ghcr.io -u $(GHCR_USERNAME) --password=$(GHCR_TOKEN)


# Install NGINX configuration
install:
	sudo ln -sf $(NGINX_CONF).conf $(NGINX_SITES_ENABLED)/$(APP_NAME).conf
	sudo nginx -t && sudo systemctl reload nginx

.PHONY: build run install pull login

