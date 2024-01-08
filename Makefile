# Define variables
APP_NAME=utilsworkouse
NGINX_CONF=nginx.conf
NGINX_SITES_ENABLED=/etc/nginx/sites-enabled

# Build the Docker image
build:
	docker build -t $(APP_NAME) .

# Run the Docker container
run:
	docker run -d -p 5000:5000 --name $(APP_NAME) $(APP_NAME)

# Install NGINX configuration
install:
	sudo ln -sf $(NGINX_CONF).conf $(NGINX_SITES_ENABLED)/$(APP_NAME).conf
	sudo nginx -t && sudo systemctl reload nginx

.PHONY: build run install

