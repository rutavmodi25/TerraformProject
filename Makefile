# Variables
IMAGE_NAME = terraform-python
CONTAINER_NAME = terraform-python-container
WORKDIR = /workspace

# Build the Docker image
docker-build:
	docker build -t $(IMAGE_NAME):latest .

# Run the Docker container
docker-run:
	docker run --rm -it -v "$(shell pwd)":$(WORKDIR) --name $(CONTAINER_NAME) $(IMAGE_NAME):latest

docker-shell:
	docker run --rm -it -v "$(shell pwd)":${WORKDIR} --name ${CONTAINER_NAME} ${IMAGE_NAME}:latest /bin/sh

# Clean up the Docker image
docker-clean:
	docker rmi $(IMAGE_NAME):latest
